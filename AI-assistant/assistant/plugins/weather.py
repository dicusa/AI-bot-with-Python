import python_weather
import asyncio

async def get_weather(city: str) -> str:
    # Use metric units by default
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
        current = weather.current
        if current:
            return (f"The current temperature in {city} is {current.temperature}°C "
                    f"with {current.sky_text.lower()}.")
        else:
            return f"Sorry, I couldn't get the weather for {city}."

def fetch_weather(city: str) -> str:
    # Helper to run async function in sync code
    try:
        return asyncio.run(get_weather(city))
    except Exception:
        return "Sorry, I couldn't fetch the weather right now."
