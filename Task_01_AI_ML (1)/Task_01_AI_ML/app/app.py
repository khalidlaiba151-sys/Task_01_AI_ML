import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="India Air Quality Dashboard", layout="wide")

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "dataset", "cleaned_city_day.csv")
POLLUTANTS = ["PM2_5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2", "O3", "Benzene", "Toluene", "AQI"]
ORDER = ["Good", "Satisfactory", "Moderate", "Poor", "Very Poor", "Severe"]


@st.cache_data
def load():
    d = pd.read_csv(DATA, parse_dates=["Date"])
    return d


df = load()

st.title("India Air Quality Dashboard (2015-2020)")
st.caption("Devixo AI/ML Internship, Task 01 | Data: Kaggle 'Air Quality Data in India' (cleaned)")

# ---- Filters
st.sidebar.header("Filters")
cities = sorted(df["City"].unique())
sel_cities = st.sidebar.multiselect("City", cities, default=cities)
y_min, y_max = int(df["Year"].min()), int(df["Year"].max())
sel_years = st.sidebar.slider("Year range", y_min, y_max, (y_min, y_max))
sel_cat = st.sidebar.multiselect("AQI category", ORDER, default=ORDER)

f = df[df["City"].isin(sel_cities) & df["Year"].between(*sel_years) & df["AQI_Category"].isin(sel_cat)]
if f.empty:
    st.warning("No data for the selected filters.")
    st.stop()

# ---- Overview and KPIs
st.subheader("Dataset overview")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total records", f"{len(f):,}")
c2.metric("Total columns", f.shape[1])
c3.metric("Average AQI", f"{f['AQI'].mean():.1f}")
c4.metric("Median AQI", f"{f['AQI'].median():.1f}")
worst = f.groupby("City")["AQI"].mean().idxmax()
c5.metric("Most polluted city", worst)

tab1, tab2, tab3, tab4 = st.tabs(["Trends", "Cities", "Pollutants", "Key insights"])

with tab1:
    st.markdown("**Monthly average AQI**")
    monthly = f.groupby(f["Date"].dt.to_period("M"))["AQI"].mean()
    monthly.index = monthly.index.to_timestamp()
    st.line_chart(monthly)
    a, b = st.columns(2)
    with a:
        st.markdown("**Average AQI by month of the year**")
        st.bar_chart(f.groupby("Month")["AQI"].mean())
    with b:
        st.markdown("**Days per AQI category**")
        st.bar_chart(f["AQI_Category"].value_counts().reindex(ORDER).fillna(0))

with tab2:
    st.markdown("**Average AQI by city**")
    st.bar_chart(f.groupby("City")["AQI"].mean().sort_values(ascending=False))
    st.markdown("**Summary statistics by city**")
    st.dataframe(f.groupby("City")["AQI"].agg(["count", "mean", "median", "min", "max"]).round(1)
                 .sort_values("mean", ascending=False))

with tab3:
    a, b = st.columns(2)
    with a:
        st.markdown("**Correlation heatmap**")
        fig, ax = plt.subplots(figsize=(7, 5.5))
        sns.heatmap(f[POLLUTANTS].corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, ax=ax, annot_kws={"size": 7})
        st.pyplot(fig)
    with b:
        st.markdown("**Summary statistics**")
        st.dataframe(f[POLLUTANTS].describe().round(2))

with tab4:
    st.markdown("""
- Ahmedabad, Delhi and Patna have the highest average AQI in the full dataset.
- Pollution is about twice as high in winter (Nov to Jan) as in July.
- PM2.5 (0.83) and PM10 (0.65) are the pollutants most correlated with AQI.
- About 24% of days are Poor, Very Poor or Severe; only 5.5% are Good.
- Mean AQI (153) is above the median (116): a few very polluted days raise the average.
- Note: the number of cities grows from 7 (2015) to 26 (2020), so yearly trends are not like-for-like.
    """)
    st.caption("These insights describe the full dataset and do not change with the filters.")
