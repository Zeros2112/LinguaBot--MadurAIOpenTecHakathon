from langchain.tools import tool
import requests
from pydantic import BaseModel, Field
from datetime import datetime
import wikipedia
import requests
import os

# Define the input schema
class OpenMeteoInput(BaseModel):
    latitude: float = Field(..., description="Latitude of the location to fetch weather data for")
    longitude: float = Field(..., description="Longitude of the location to fetch weather data for")

@tool(args_schema=OpenMeteoInput)
def get_current_temperature(latitude: float, longitude: float) -> dict:
    """Fetch current temperature for given coordinates."""
    
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    
    # Parameters for the request
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': 'temperature_2m',
        'forecast_days': 1,
    }

    # Make the request
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        results = response.json()
    else:
        raise Exception(f"API Request failed with status code: {response.status_code}")

    current_utc_time = datetime.datetime.utcnow()
    time_list = [datetime.datetime.fromisoformat(time_str.replace('Z', '+00:00')) for time_str in results['hourly']['time']]
    temperature_list = results['hourly']['temperature_2m']
    
    closest_time_index = min(range(len(time_list)), key=lambda i: abs(time_list[i] - current_utc_time))
    current_temperature = temperature_list[closest_time_index]-273.15
    
    return f'The current temperature is {current_temperature}°C'



@tool
def search_wikipedia(query: str) -> str:
    """Run Wikipedia search and get page summaries."""
    page_titles = wikipedia.search(query)
    summaries = []
    for page_title in page_titles[: 3]:
        try:
            wiki_page =  wikipedia.page(title=page_title, auto_suggest=False)
            summaries.append(f"Page: {page_title}\nSummary: {wiki_page.summary}")
        except (
            self.wiki_client.exceptions.PageError,
            self.wiki_client.exceptions.DisambiguationError,
        ):
            pass
    if not summaries:
        return "No good Wikipedia Search Result was found"
    return "\n\n".join(summaries)





#This example converts 100 US Dollars (USD) to Euros (EUR). The result will be printed to the console.
class CurrencyConversionInput(BaseModel):
    amount: float = Field(..., description="Amount to convert")
    from_currency: str = Field(..., description="Currency code to convert from")
    to_currency: str = Field(..., description="Currency code to convert to")

@tool(args_schema=CurrencyConversionInput)
def currency_conversion(amount, from_currency, to_currency) -> str:
    """Convert currency based on the provided input using Open Exchange Rates API."""
    api_key = os.getenv("OPEN_EXCHANGE_RATES_API_KEY")  # Replace with your Open Exchange Rates API key
    base_url = "https://open.er-api.com/v6/latest"
    params = {"base": from_currency, "apikey": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if "error" in data:
            raise Exception(f"Error from API: {data['error']['info']}")

        exchange_rate = data["rates"][to_currency]
        converted_amount = amount * exchange_rate

        result_message = (
            f"{amount} {from_currency} is equal to "
            f"{converted_amount:.2f} {to_currency}"
        )
    except requests.RequestException as e:
        result_message = f"Error during API request: {str(e)}"
    except Exception as e:
        result_message = f"An unexpected error occurred: {str(e)}"

    return result_message



#This example converts 1 Bitcoin (BTC) to Ethereum (ETH).
class CryptoConversionInput(BaseModel):
    amount: float = Field(..., description="Amount to convert")
    from_currency: str = Field(..., description="Cryptocurrency symbol to convert from (e.g., BTC)")
    to_currency: str = Field(..., description="Cryptocurrency symbol to convert to (e.g., ETH)")
@tool(args_schema=CryptoConversionInput)
def crypto_conversion(amount, from_currency, to_currency) -> str:
    """Convert cryptocurrency based on the provided input using CoinGecko API."""
    api_url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": from_currency.lower(),
        "vs_currencies": to_currency.lower(),
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if not data or "error" in data:
            raise Exception("Error fetching cryptocurrency data.")

        exchange_rate = data[from_currency.lower()][to_currency.lower()]
        converted_amount = amount * exchange_rate

        result_message = (
            f"{amount} {from_currency} is equal to "
            f"{converted_amount:.6f} {to_currency}"
        )
    except requests.RequestException as e:
        result_message = f"Error during API request: {str(e)}"
    except Exception as e:
        result_message = f"An unexpected error occurred: {str(e)}"

    return result_message


from typing import Dict
import pytz
from datetime import datetime
from pydantic import BaseModel, Field

class TimeZoneConversionInput(BaseModel):
    from_timezone: str = Field(..., description="Source time zone")
    to_timezone: str = Field(..., description="Target time zone")

@tool(args_schema=TimeZoneConversionInput)
def current_time_zone_conversion(from_timezone, to_timezone) -> str:
    """Convert current time between time zones based on the provided input."""
    try:
        from_timezone = pytz.timezone(from_timezone)
        to_timezone = pytz.timezone(to_timezone)

        source_current_time = datetime.now(from_timezone)
        target_current_time = source_current_time.astimezone(to_timezone)

        result_message = (
            f"Current time in {from_timezone}: {source_current_time.strftime('%Y-%m-%d %H:%M:%S')} \n"
            f"Converted time in {to_timezone}: {target_current_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
    except pytz.exceptions.UnknownTimeZoneError:
        result_message = "Invalid time zone provided."
    except Exception as e:
        result_message = f"An unexpected error occurred: {str(e)}"

    return result_message




class TranslationInput(BaseModel):
    text: str = Field(..., description="Text to translate")
    source_language: str = Field(..., description="Source language code (e.g., en for English)")
    target_language: str = Field(..., description="Target language code")
@tool(args_schema=TranslationInput)
def language_translation(text, source_language, target_language) -> str:
    """Translate text based on the provided input using Google Cloud Translation API."""
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    if not api_key:
        raise ValueError("Google Cloud Translation API key not found in environment variables.")

    api_url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "key": api_key,
        "q": text,
        "source": source_language,
        "target": target_language,
    }

    try:
        response = requests.post(api_url, data=params)
        data = response.json()

        if "error" in data:
            raise Exception(f"Error from API: {data['error']['message']}")

        translated_text = data["data"]["translations"][0]["translatedText"]
        result_message = f"Translation: {translated_text}"
    except requests.RequestException as e:
        result_message = f"Error during API request: {str(e)}"
    except Exception as e:
        result_message = f"An unexpected error occurred: {str(e)}"

    return result_message

# This example converts 10 miles to kilometers.
import pint
from pint import UnitRegistry
from pydantic import BaseModel, Field

ureg = UnitRegistry()

class UnitConversionInput(BaseModel):
    value: float = Field(..., description="Value to convert")
    from_unit: str = Field(..., description="Source unit")
    to_unit: str = Field(..., description="Target unit")
@tool(args_schema=UnitConversionInput)
def unit_conversion(value, from_unit, to_unit) -> str:
    """Convert units based on the provided input using the pint library."""
    try:
        # Create quantity with source unit
        quantity = value * ureg(from_unit)

        # Convert to the target unit
        result_quantity = quantity.to(to_unit)

        result_message = f"Converted value: {result_quantity.magnitude} {result_quantity.units}"
    except pint.UndefinedUnitError as e:
        result_message = f"Error during unit conversion: {str(e)}"
    except Exception as e:
        result_message = f"An unexpected error occurred: {str(e)}"

    return result_message



class StockInfoInput(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")
@tool(args_schema=StockInfoInput)
def get_stock_info(symbol) -> str:
    """Fetch stock information based on the provided input using Alpha Vantage API."""
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    symbol = symbol

    api_url = f"https://www.alphavantage.co/query"
    function = "GLOBAL_QUOTE"

    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if "Global Quote" not in data:
            raise Exception("Error fetching stock information.")

        stock_info = data["Global Quote"]
        result_message = (
            f"Stock Symbol: {stock_info['01. symbol']}\n"
            f"Open Price: {stock_info['02. open']}\n"
            f"High Price: {stock_info['03. high']}\n"
            f"Low Price: {stock_info['04. low']}\n"
            f"Current Price: {stock_info['05. price']}\n"
            f"Previous Close: {stock_info['08. previous close']}\n"
            f"Change: {stock_info['09. change']}\n"
            f"Change Percent: {stock_info['10. change percent']}"
        )
    except requests.RequestException as e:
        result_message = f"Error during API request: {str(e)}"
    except Exception as e:
        result_message = f"An unexpected error occurred: {str(e)}"

    return result_message





import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from pydantic import BaseModel, Field

class StockVisualizationInput(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")
    api_key: str = Field(..., description="Alpha Vantage API key")
@tool(args_schema=StockVisualizationInput)
def visualize_stock(symbol,api_key) -> str:
    """Visualize historical stock data based on the provided input using Alpha Vantage API."""
    api_key = api_key
    symbol = symbol

    api_url = f"https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY"
    
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if "Time Series (Daily)" not in data:
            raise Exception("Error fetching historical stock data.")

        # Convert data to a DataFrame for easier manipulation
        time_series_data = data["Time Series (Daily)"]
        df = pd.DataFrame(time_series_data).T
        df.index = pd.to_datetime(df.index)

        # Plot the closing prices
        plt.figure(figsize=(10, 6))
        plt.plot(df.index, df['4. close'], label='Closing Price', color='blue')
        plt.title(f"{symbol} Stock Price Over Time")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save the plot
        plot_filename = "stock_plot.png"
        plt.savefig(plot_filename)
        plt.close()

        result_message = f"Stock plot saved as {plot_filename}"
    except requests.RequestException as e:
        result_message = f"Error during API request: {str(e)}"
    except Exception as e:
        result_message = f"An unexpected error occurred: {str(e)}"

    return result_message



import requests
from pydantic import BaseModel, Field
from datetime import datetime

class WeatherForecastInput(BaseModel):
    city: str = Field(..., description="City name")
    country: str = Field(..., description="Country code")

@tool(args_schema=WeatherForecastInput)
def weather_forecast(city,country) -> str:
    """Fetch weather forecast for a given city and country."""
    api_key = os.getenv('OPENWEATHER_FORCAST_API')
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'

    params = {
        'q': f"{city},{country}",
        'appid': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            forecast_list = data.get('list', [])
            
            if forecast_list:
                # Get the forecast for the next 3 days
                forecast_message = "Weather Forecast:\n"
                for forecast in forecast_list[:8]:  # Assuming 3-hour intervals, 8 entries represent 24 hours
                    timestamp = forecast['dt']
                    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    temperature = forecast['main']['temp']-273.15
                    description = forecast['weather'][0]['description']

                    forecast_message += f"{date}: {temperature}°C, {description}\n"

                return forecast_message
            else:
                return "No forecast data available."

        else:
            return f"API Request failed with status code: {response.status_code}"

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"






tools = [
    get_current_temperature, 
    search_wikipedia, 
    currency_conversion, 
    crypto_conversion, 
    current_time_zone_conversion, 
    language_translation,
    unit_conversion, 
    get_stock_info,
    visualize_stock,
    weather_forecast
]





