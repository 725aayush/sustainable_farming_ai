from agents.farmer_agent import advise_farmer
from agents.market_agent import predict_demand
from agents.soil_agent import SoilAgent
from agents.weather_agent import WeatherAgent
import json

def run_system(farm_id=1, crop="Wheat", location="Nashik,IN"):
    print(f"🚜 Running system for farm_id={farm_id}, crop={crop}, location={location}...\n")

    soil_agent = SoilAgent()
    weather_agent = WeatherAgent(model="llama2")  # Using LLaMA2 via Ollama

    try:
        print("📡 Gathering soil data...")
        soil = soil_agent.get_soil_status(farm_id)
        print(f"✅ Soil: {soil}")

        print("💧 Checking irrigation...")
        irrigation = soil_agent.check_irrigation(farm_id)
        print(f"✅ Irrigation: {'Yes' if irrigation else 'No'}")

        print("🌦️ Fetching weather...")
        forecast = weather_agent.fetch_forecast(location)
        weather = weather_agent.analyze_impact(location, crop)
        drought = weather_agent.drought_risk(location)

        print("🧑‍🌾 Getting farmer advice...")
        farmer = advise_farmer(farm_id)

        print("📈 Analyzing market...")
        market = predict_demand(crop)

        report = {
            "farm_id": farm_id,
            "location": location,
            "crop": crop,
            "soil": soil,
            "irrigation": irrigation,
            "weather_forecast": forecast,
            "weather_impact": weather,
            "drought_risk": drought,
            "farmer_advice": farmer,
            "market_outlook": market
        }

        with open(f"reports/farm_{farm_id}_report.json", "w") as f:
            json.dump(report, f, indent=2)

        print("\n✅ Report generated successfully!")
        return report

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return {"error": str(e)}

    finally:
        soil_agent.close()
        weather_agent.close()

if __name__ == "__main__":
    run_system(farm_id=1, crop="Quinoa", location="Pune,IN")
