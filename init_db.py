import sqlite3
import pandas as pd
import os

# Paths
db_path = "database/farm.db"
farmer_csv = "data/farmer_advisor_dataset.csv"
market_csv = "data/market_researcher_dataset.csv"

# Ensure database folder exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Delete the existing database if it exists
if os.path.exists(db_path):
    os.remove(db_path)

# Connect to SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create farmer_data table
cursor.execute("""
CREATE TABLE farmer_data (
    Farm_ID INTEGER PRIMARY KEY,
    Crop TEXT,
    Soil_Type TEXT,
    Rainfall REAL,
    Temperature REAL,
    Humidity REAL,
    Soil_pH REAL,
    Organic_Matter REAL,
    Pest_Infestation_Level TEXT,
    Land_Size REAL,
    Budget REAL,
    Goal TEXT
)
""")

# Create market_data table
cursor.execute("""
CREATE TABLE market_data (
    Market_ID INTEGER PRIMARY KEY,
    Product TEXT,
    Market_Price_per_ton REAL,
    Demand_Index REAL,
    Supply_Index REAL,
    Competitor_Price_per_ton REAL,
    Economic_Indicator REAL,
    Weather_Impact_Score REAL,
    Seasonal_Factor TEXT,
    Consumer_Trend_Index REAL
)
""")

# Load data from CSVs
farmer_df = pd.read_csv(farmer_csv)
market_df = pd.read_csv(market_csv)

# Insert into tables
farmer_df.to_sql("farmer_data", conn, if_exists="append", index=False)
market_df.to_sql("market_data", conn, if_exists="append", index=False)

print("✅ Database initialized successfully.")

conn.commit()
conn.close()



