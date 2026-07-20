from fastmcp import FastMCP
import requests

mcp = FastMCP("Weather_Server")


def get_coordinates(city: str):
    """
    Convert city name to latitude and longitude.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        url,
        params={
            "name": city,
            "count": 1
        },
        timeout=10
    )

    data = response.json()

    if "results" not in data:
        return None

    location = data["results"][0]

    return (
        location["latitude"],
        location["longitude"],
        location["name"],
        location.get("country", "")
    )


@mcp.tool()
def current_weather(city: str) -> dict:
    """
    Get current weather for a city.
    """

    location = get_coordinates(city)

    if location is None:
        return {
            "error": f"City '{city}' not found."
        }

    latitude, longitude, name, country = location

    url = "https://api.open-meteo.com/v1/forecast"

    response = requests.get(
        url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m,relative_humidity_2m"
        },
        timeout=10
    )

    weather = response.json()["current"]

    return {
        "city": name,
        "country": country,
        "temperature": weather["temperature_2m"],
        "humidity": weather["relative_humidity_2m"],
        "wind_speed": weather["wind_speed_10m"]
    }


if __name__ == "__main__":
    mcp.run()
