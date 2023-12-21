# LangChain Toolset Documentation

## Overview

This Python code defines a set of tools utilizing different APIs for various purposes, such as fetching weather data, currency conversion, language translation, and more. The tools are designed to be used within a conversational agent framework to provide responses based on user queries.

## Tools

### 1. get_current_temperature

- **Description:** Fetches the current temperature for a given set of coordinates using the Open Meteo API.
- **Input Schema:** `OpenMeteoInput`
- **Usage:** `get_current_temperature(latitude: float, longitude: float) -> dict`

### 2. search_wikipedia

- **Description:** Runs a Wikipedia search and retrieves page summaries for the given query.
- **Input Schema:** `query: str`
- **Usage:** `search_wikipedia(query: str) -> str`

### 3. currency_conversion

- **Description:** Converts currency based on the provided input using the Open Exchange Rates API.
- **Input Schema:** `CurrencyConversionInput`
- **Usage:** `currency_conversion(amount, from_currency, to_currency) -> str`

### 4. crypto_conversion

- **Description:** Converts cryptocurrency based on the provided input using the CoinGecko API.
- **Input Schema:** `CryptoConversionInput`
- **Usage:** `crypto_conversion(amount, from_currency, to_currency) -> str`

### 5. current_time_zone_conversion

- **Description:** Converts the current time between time zones based on the provided input.
- **Input Schema:** `TimeZoneConversionInput`
- **Usage:** `current_time_zone_conversion(from_timezone, to_timezone) -> str`

### 6. language_translation

- **Description:** Translates text based on the provided input using the Google Cloud Translation API.
- **Input Schema:** `TranslationInput`
- **Usage:** `language_translation(text, source_language, target_language) -> str`

### 7. unit_conversion

- **Description:** Converts units based on the provided input using the Pint library.
- **Input Schema:** `UnitConversionInput`
- **Usage:** `unit_conversion(value, from_unit, to_unit) -> str`

### 8. get_stock_info

- **Description:** Fetches stock information based on the provided input using the Alpha Vantage API.
- **Input Schema:** `StockInfoInput`
- **Usage:** `get_stock_info(symbol) -> str`

### 9. visualize_stock

- **Description:** Visualizes historical stock data based on the provided input using the Alpha Vantage API.
- **Input Schema:** `StockVisualizationInput`
- **Usage:** `visualize_stock(symbol, api_key) -> str`

### 10. weather_forecast

- **Description:** Fetches weather forecast for a given city and country using the OpenWeatherMap API.
- **Input Schema:** `WeatherForecastInput`
- **Usage:** `weather_forecast(city, country) -> str`

## Usage

The tools can be imported and used individually in your Python scripts or integrated into a larger conversational agent framework. The `ConversationBufferMemory` class and other utility functions are used to store and manage conversation history.

## Dependencies

- `requests`
- `pydantic`
- `wikipedia`
- `pint`
- `pandas`
- `matplotlib`
- `pytz`
- `panel`
- `bokeh`
- `dotenv`

## Configuration

Ensure that the necessary API keys (e.g., OpenAI API key) are set up in the environment variables or the `.env` file.

## Examples

The code includes examples of using each tool. Refer to the respective function docstrings for detailed information on input parameters and usage.

## Contributions

Contributions are welcome! Feel free to add new tools or improve existing ones. Please follow the coding style and documentation conventions.

## License

This code is provided under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the developers of the APIs used in these tools.

## Contact

For any inquiries or feedback, contact [Your Name](mailto:your.email@example.com).

## Changelog

### Version 1.0.0 (Date)

- Initial release with a set of tools for various purposes.

## Known Issues

Document any known issues or limitations of the tools.
