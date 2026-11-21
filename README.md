# Air Quality Analysis of 26 Indian Cities (2015-2020)

**Devixo Solutions AI/ML Internship Program, Task 01: Python Programming, Data Analysis & Visualization**

Author: **Laiba Khalid**

## Project Objective
Analyse real air-quality data with Python to find out which Indian cities are the most polluted, how air quality changes across seasons and years, and which pollutants are most closely linked with the Air Quality Index (AQI).

## Dataset Description
Daily air-quality readings for 26 Indian cities, from 1 January 2015 to 1 July 2020. Each row is one city on one day, with 12 pollutant measurements, the AQI and the AQI category.

| | Rows | Columns |
|---|---|---|
| Original (`city_day.csv`) | 29,531 | 16 |
| Cleaned (`cleaned_city_day.csv`) | 24,307 | 17 |

## Dataset Source
Kaggle: [Air Quality Data in India (2015 - 2020)](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india) by Rohan Rao (data from the Central Pollution Control Board, India). Only `city_day.csv` is used.

## Technologies Used
Python 3, Jupyter Notebook / Google Colab, Streamlit (bonus dashboard)

## Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, Streamlit

## Project Workflow
1. Dataset selection and loading
2. Data understanding (shape, types, missing values)
3. Data cleaning: dropped the Xylene column (61% missing), removed rows without AQI, filled other missing values with city-wise medians, converted `Date` to datetime, removed 543 rows with invalid AQI (above 500), renamed columns
4. Exploratory data analysis and statistics (mean, median, mode, std, variance, correlation)
5. Ten visualizations (histogram, bar, pie, count, line, scatter, box, heatmap, pair plot, violin)
6. Insights, conclusion, PDF report, Streamlit dashboard

## Major Findings
- Ahmedabad (291.7), Delhi (252.1) and Patna (235.6) have the highest average AQI; Aizawl (34.8) and Shillong (53.8) the lowest.
- Pollution is about twice as high in winter (Nov to Jan) as in July.
- PM2.5 (0.83) and PM10 (0.65) are the pollutants most correlated with AQI.
- About 24% of days are Poor, Very Poor or Severe; only 5.5% are Good.
- Mean AQI (153) is above the median (116): a few very polluted days raise the average.
- Limitations: many Ahmedabad rows were invalid and removed, and the number of cities with data grows from 7 (2015) to 26 (2020), so yearly trends are not fully like-for-like.

## Project Structure
```
Task_01_AI_ML/
  dataset/    city_day.csv, cleaned_city_day.csv
  notebook/   Task_01_Data_Analysis.ipynb
  images/     visualization_01.png ... visualization_10.png
  report/     Task_01_Report.pdf
  app/        app.py (Streamlit dashboard)
  requirements.txt
  README.md
```

## How to Run the Project
```bash
pip install -r requirements.txt

# 1. Notebook
jupyter notebook notebook/Task_01_Data_Analysis.ipynb

# 2. Streamlit dashboard (run from the project folder)
streamlit run app/app.py
```
The notebook also runs in Google Colab: upload `city_day.csv` next to the notebook and run all cells.

## Student / Author
Laiba Khalid
