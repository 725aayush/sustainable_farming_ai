import sqlite3
from utils.ollama_utils import query_ollama

class FarmerAdvisorAgent:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_advice(self, farm_id, crop):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT Sustainability_Score FROM farmer_data WHERE Farm_ID=?", (farm_id,))
            row = cursor.fetchone()

            if row and row[0] is not None:
                sustainability_score = row[0]
            else:
                sustainability_score = query_ollama(f"Estimate the sustainability score for a farm growing {crop}.")
            
            advice = f"For crop {crop}, the sustainability score is {sustainability_score}. Consider using organic fertilizers and optimized irrigation."

            return advice

        except Exception as e:
            raise Exception(f"Error fetching farmer advice: {e}")

        finally:
            conn.close()
