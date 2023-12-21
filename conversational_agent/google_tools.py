import os
import requests
from pydantic import BaseModel, Field
from langchain.tools import tool
class GeocodingInput(BaseModel):
    address: str = Field(..., description="Address to geocode")
@tool(args_schema=GeocodingInput)
def geocode_address(address) -> dict:
    """Geocode an address using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": address,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            location = data["results"][0]["geometry"]["location"]
            result = {"latitude": location["lat"], "longitude": location["lng"]}
        else:
            raise Exception("Error geocoding address.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return result


import os
import requests
from pydantic import BaseModel, Field

class ReverseGeocodingInput(BaseModel):
    latitude: float = Field(..., description="Latitude")
    longitude: float = Field(..., description="Longitude")
@tool(args_schema=ReverseGeocodingInput)
def reverse_geocode_coordinates(latitude, longtitude) -> str:
    """Reverse geocode coordinates using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "latlng": f"{latitude},{longtitude}",
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            address = data["results"][0]["formatted_address"]
        else:
            raise Exception("Error reverse geocoding coordinates.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return address


import os
import requests
from pydantic import BaseModel, Field

class DistanceMatrixInput(BaseModel):
    origin: str = Field(..., description="Origin address or coordinates")
    destination: str = Field(..., description="Destination address or coordinates")
@tool(args_schema=DistanceMatrixInput)
def calculate_distance_matrix(origin, destination) -> dict:
    """Calculate distance matrix using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {
        "origins": origin,
        "destinations": destination,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            distance_matrix = data["rows"][0]["elements"][0]
            result = {
                "distance": distance_matrix.get("distance", {}).get("text", ""),
                "duration": distance_matrix.get("duration", {}).get("text", ""),
            }
        else:
            raise Exception("Error calculating distance matrix.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return result

import os
import requests
from pydantic import BaseModel, Field

class PlaceSearchInput(BaseModel):
    query: str = Field(..., description="Search query")
    location: str = Field(..., description="Location coordinates")
    radius: int = Field(1000, description="Search radius in meters")
@tool(args_schema=PlaceSearchInput)
def place_search(query, location, radius) -> list:
    """Search for places using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "query": query,
        "location": location,
        "radius": radius,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            places = data.get("results", [])
        else:
            raise Exception("Error searching for places.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return places


import os
import requests
from pydantic import BaseModel, Field

class ElevationInput(BaseModel):
    location: str = Field(..., description="Location coordinates")
@tool(args_schema=ElevationInput)
def get_elevation(location) -> float:
    """Get elevation data using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/elevation/json"

    params = {
        "locations": location,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            elevation = data["results"][0]["elevation"]
        else:
            raise Exception("Error retrieving elevation data.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return elevation


import os
import requests
from pydantic import BaseModel, Field

class TimeZoneInput(BaseModel):
    location: str = Field(..., description="Location coordinates")
    timestamp: int = Field(..., description="Unix timestamp")
@tool(args_schema=TimeZoneInput)
def get_time_zone(location, timestamp) -> str:
    """Get time zone data using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/timezone/json"

    params = {
        "location": location,
        "timestamp": timestamp,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            time_zone_id = data["timeZoneId"]
        else:
            raise Exception("Error retrieving time zone data.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return time_zone_id

import os
import requests
from pydantic import BaseModel, Field

class DirectionsInput(BaseModel):
    origin: str = Field(..., description="Origin coordinates")
    destination: str = Field(..., description="Destination coordinates")
@tool(args_schema=DirectionsInput)
def get_directions(origin, destination) -> dict:
    """Get directions using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
        "origin": origin,
        "destination": destination,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            directions = data["routes"][0]["legs"][0]
        else:
            raise Exception("Error retrieving directions.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return directions


import os
from pydantic import BaseModel, Field

class StaticMapInput(BaseModel):
    center: str = Field(..., description="Center coordinates")
    zoom: int = Field(12, description="Zoom level")
    size: str = Field("400x400", description="Image size in pixels")
@tool(args_schema=StaticMapInput)
def generate_static_map(center, zoom, size) -> str:
    """Generate a static map using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/staticmap"

    params = {
        "center": center,
        "zoom": zoom,
        "size": size,
        "key": api_key,
    }

    static_map_url = f"{api_url}?{'&'.join(f'{key}={value}' for key, value in params.items())}"
    return static_map_url

import os
import requests
from pydantic import BaseModel, Field

class PlaceDetailsInput(BaseModel):
    place_id: str = Field(..., description="Place ID")
@tool(args_schema=PlaceDetailsInput)
def get_place_details(place_id) -> dict:
    """Get place details using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/place/details/json"

    params = {
        "place_id": place_id,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            place_details = data["result"]
        else:
            raise Exception("Error retrieving place details.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return place_details


import os
import requests
from pydantic import BaseModel, Field

class AutocompleteInput(BaseModel):
    input_text: str = Field(..., description="User input for autocomplete")
@tool(args_schema=AutocompleteInput)
def autocomplete_places(input_text) -> list:
    """Autocomplete places using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"

    params = {
        "input": input_text,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            predictions = data["predictions"]
        else:
            raise Exception("Error retrieving place predictions.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return predictions


import os
import requests
from pydantic import BaseModel, Field

class DistanceMatrixExtendedInput(BaseModel):
    origins: list = Field(..., description="List of origin addresses or coordinates")
    destinations: list = Field(..., description="List of destination addresses or coordinates")
@tool(args_schema=DistanceMatrixExtendedInput)
def calculate_distance_matrix_extended(origins, destinations) -> dict:
    """Calculate distance matrix for multiple origins and destinations using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {
        "origins": "|".join(origins),
        "destinations": "|".join(destinations),
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            distance_matrix = data["rows"]
        else:
            raise Exception("Error calculating distance matrix.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return distance_matrix


import os
import requests
from pydantic import BaseModel, Field

class NearbyPlacesInput(BaseModel):
    location: str = Field(..., description="Location coordinates")
    radius: int = Field(1000, description="Search radius in meters")
    type: str = Field("restaurant", description="Place type")
@tool(args_schema=NearbyPlacesInput)
def get_nearby_places(location, radius, type) -> list:
    """Get nearby places using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": location,
        "radius": radius,
        "type": type,
        "key": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            places = data.get("results", [])
        else:
            raise Exception("Error retrieving nearby places.")

    except requests.RequestException as e:
        raise Exception(f"Error during API request: {str(e)}")

    return places


import os
from pydantic import BaseModel, Field

class StaticStreetViewInput(BaseModel):
    location: str = Field(..., description="Location coordinates")
    size: str = Field("400x400", description="Image size in pixels")
@tool(args_schema=StaticStreetViewInput)
def generate_static_street_view(location, size) -> str:
    """Generate a static Street View image using Google Maps API."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google Maps API key not found in environment variables.")

    api_url = "https://maps.googleapis.com/maps/api/streetview"

    params = {
        "location": location,
        "size": size,
        "key": api_key,
    }

    static_street_view_url = f"{api_url}?{'&'.join(f'{key}={value}' for key, value in params.items())}"
    return static_street_view_url
