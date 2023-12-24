# LinguaBot @MadurAIOpenTecHakthon

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

### 11. geocode_address

- **Description:** Geocode an address using Google Maps API.
- **Input Schema**: `GeocodingInput`
- **Usage:** `geocode_address(address: str) -> dict`

### 12. reverse_geocode_coordinates

- **Description:** Reverse geocode coordinates using Google Maps API.
- **Input Schema:** `ReverseGeocodingInput`
- **Usage:** `reverse_geocode_coordinates(latitude: float, longitude: float) -> str`

### 13. calculate_distance_matrix

- **Description:** Calculate distance matrix using Google Maps API.
- **Input Schema:** `DistanceMatrixInput`
- **Usage:** `calculate_distance_matrix(origin: str, destination: str) -> dict`

### 14. place_search

- **Description:** Search for places using Google Maps API.
- **Input Schema:** `PlaceSearchInput`
- **Usage:** `place_search(query: str, location: str, radius: int) -> list`

### 15. get_elevation

- **Description:** Get elevation data using Google Maps API.
- **Input Schema:** `ElevationInput`
- **Usage:** `get_elevation(location: str) -> float`

### 16. get_time_zone

- **Description:** Get time zone data using Google Maps API.
- **Input Schema:** `TimeZoneInput`
- **Usage:** `get_time_zone(location: str, timestamp: int) -> str`

### 17. get_directions

- **Description:** Get directions using Google Maps API.
- **Input Schema:** `DirectionsInput`
- **Usage:** `get_directions(origin: str, destination: str) -> dict`

### 18. generate_static_map

- **Description:** Generate a static map using Google Maps API.
- **Input Schema:** `StaticMapInput`
- **Usage:** `generate_static_map(center: str, zoom: int, size: str) -> str`

### 19. get_place_details

- **Description:** Get place details using Google Maps API.
- **Input Schema:** `PlaceDetailsInput`
- **Usage:** `get_place_details(place_id: str) -> dict`

### 20. autocomplete_places

- **Description:** Autocomplete places using Google Maps API.
- **Input Schema:** `AutocompleteInput`
- **Usage:** `autocomplete_places(input_text: str) -> list`

### 21. calculate_distance_matrix_extended

- **Description:** Calculate distance matrix for multiple origins and destinations using Google Maps API.
- **Input Schema:** `DistanceMatrixExtendedInput`
- **Usage:** `calculate_distance_matrix_extended(origins: list, destinations: list) -> dict`

### 22. get_nearby_places

- **Description:** Get nearby places using Google Maps API.
- **Input Schema:** `NearbyPlacesInput`
- **Usage:** `get_nearby_places(location: str, radius: int, type: str) -> list`

### 23. generate_static_street_view

- **Description:** Generate a static Street View image using Google Maps API.
- **Input Schema:** `StaticStreetViewInput`
- **Usage:** `generate_static_street_view(location: str, size: str) -> str`

### 24. post_on_twitter

- **Description:** Post a message on Twitter.
- **Input Schema:** `TwitterInteractionInput`
- **Usage:** `post_on_twitter(input_data: TwitterInteractionInput) -> str`

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
