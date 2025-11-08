# 🛠️ BMW Sales Data Processing with Pandas
A comprehensive ETL (Extract, Transform, Load) pipeline for processing and analyzing BMW sales data. This project demonstrates data cleaning, transformation, and loading into multiple formats including SQL database.


📊 Project Overview
This ETL pipeline processes BMW vehicle sales data to extract meaningful business insights. The system cleanses raw sales data, enriches it with calculated fields, and loads it into both file formats and SQL database for analysis.


![Python](https://img.shields.io/badge/Python-3.13-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Status](https://img.shields.io/badge/Status-Active-success)


## 🏗️ Tech Stack
- **Language:** Python. Pandas
- **Database:** SQLite
- **Libraries:** pandas, sqlite



## 🗂️ Database Schema

Table: `bmw_sales`

| Column              | Type    | Description                        |
|---------------------|---------|------------------------------------|
| Model               | TEXT    | BMW model name                     |
| Year                | INTEGER | Manufacturing year of the vehicle  |
| Region              | TEXT    | Sales region                       |
| Color               | TEXT    | Vehicle color                      |
| Fuel_Type           | TEXT    | Type of fuel                       |
| Sales_Classification| TEXT   | Sales volume category               |
| Vehicle_Age         | INTEGER | Age of vehicle in years            |
| Age_Category        | TEXT    | Categorized age                    |
| Price_Category      | TEXT    | Price tier                         |
| Collection_Million  | REAL    | Total revenue in millions USD      |
| Collection_Category | TEXT    | Profit classification              |
| Avg KM              | REAL    | Average kilometers driven per year |
| Engine_Size         | TEXT    | Categorized engine size            |


🚀 Features
1. Data Extraction: Read and validate raw CSV data
2. Data Transformation:
   a.  Vehicle age categorization
   b. Price tier classification
   c.Revenue and profit calculations
   d. Engine size categorization
   e.  Regional market analysis
3.Data Loading: Export to multiple formats
   a. Excel files
   b. CSV files
   c. SQLite database


## 🚧 Future Improvements
- Add error handling for ETL failures.
- Support cloud databases (AWS RDS, PostgreSQL).
- Automate scheduling using Airflow.
