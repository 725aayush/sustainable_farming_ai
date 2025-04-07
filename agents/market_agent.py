import sqlite3
from utils.ollama_utils import query_ollama

class MarketResearchAgent:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_market_trends(self, crop):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT AVG(Demand_Index), AVG(Price_per_kg) FROM market_data WHERE Crop=?", (crop,))
            row = cursor.fetchone()

            if row and all(row):
                demand_index, price_per_kg = row
            else:
                response = query_ollama(f"What are the market trends (demand index and average price) for {crop}?")
                return f"📈 Market Trends (via Ollama): {response}"

            return f"📊 Demand Index: {demand_index:.2f}, Avg Price: ₹{price_per_kg:.2f}/kg"

        except Exception as e:
            raise Exception(f"Error fetching market trends: {e}")
        finally:
            conn.close()

