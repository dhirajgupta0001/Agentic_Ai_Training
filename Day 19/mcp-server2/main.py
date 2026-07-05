from fastmcp import FastMCP
import httpx

mcp = FastMCP("Weather's_Server")


@mcp.tool()
async def get_weather(city: str) -> dict:
    """
    Get current weather for any city in the world.
    """

    async with httpx.AsyncClient(timeout=20) as client:

        # Step 1: Get coordinates
        geo = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json",
            },
        )

        geo.raise_for_status()

        results = geo.json().get("results")

        if not results:
            return {
                "error": f"City '{city}' not found."
            }

        place = results[0]

        lat = place["latitude"]
        lon = place["longitude"]

        # Step 2: Current weather

        weather = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "wind_speed_10m",
                    "weather_code",
                ],
            },
        )

        weather.raise_for_status()

        current = weather.json()["current"]

        return {
            "city": place["name"],
            "country": place["country"],
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind_speed": current["wind_speed_10m"],
            "weather_code": current["weather_code"],
        }


if __name__ == "__main__":
    mcp.run()
