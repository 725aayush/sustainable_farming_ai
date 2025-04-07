import sqlite3

# Connect to your database
conn = sqlite3.connect("farm.db")
cursor = conn.cursor()

# Show column info for the farmer_data table
cursor.execute("PRAGMA table_info(farmer_data);")
columns = cursor.fetchall()

print("📋 Columns in 'farmer_data':")
for col in columns:
    print(f"• {col[1]} ({col[2]})")  # col[1] = column name, col[2] = data type

conn.close()
