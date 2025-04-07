import sqlite3
from utils.ollama_utils import query_ollama

class SoilAnalyzerAgent:
    def __init__(self, db_path):
        self.db_path = db_path

    def fetch_soil_data(self, farm_id):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT Soil_pH, Soil_Moisture, Temperature_C, Rainfall_mm, Fertilizer_Usage_kg, Pesticide_Usage_kg
                FROM farmer_data WHERE Farm_ID=?
            """, (farm_id,))
            row = cursor.fetchone()

            if row and all(row):
                return {
                    "soil_ph": row[0],
                    "moisture": row[1],
                    "temperature": row[2],
                    "rainfall": row[3],
                    "fertilizer_kg": row[4],
                    "pesticide_kg": row[5]
                }
            else:
                response = query_ollama(f"Generate sample soil data for farm ID {farm_id}")
                return {"ollama_generated": response}

        except Exception as e:
            raise Exception(f"Error fetching soil data: {e}")
        finally:
            conn.close()

    def check_irrigation_need(self, moisture):
        return moisture < 40
