# Flask Paper Extraction App

## Overview

The Flask Paper Extraction App is a web application that utilizes the OpenAI Chat-based language model to extract information about papers mentioned in an article from a given link. It provides an intuitive web interface for users to input a link, and the application, powered by OpenAI's language model, extracts relevant paper information from the provided article.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd your-repo
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key:**

   Create a `.env` file in the project directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Access the application:**

   Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to interact with the application.

3. **Input a link:**

   Enter a link to an article in the provided form and submit it.

4. **View results:**

   The application will extract information about papers mentioned in the article and display the results on the web page.

## Code Structure

- **`app.py`**: Contains the main Flask application code, including route definitions.
- **`langchain/`**: Directory containing modules related to the language model and text processing.
- **`templates/`**: Contains HTML templates for rendering web pages.
- **`static/`**: Directory for static files (CSS, JavaScript, etc.).

## Dependencies

- Flask
- Flask-CORS
- Pydantic
- OpenAI
- langchain (custom module)
- dotenv

## Configuration

Ensure that you have set up your OpenAI API key in the `.env` file.

## Examples

### Basic Example

```python
from app import extracting

link = "https://example.com"
result = extracting(link)
print(result)
```

## Contributing

Contributions are welcome!

## License

This project is licensed under the MIT License.

## Acknowledgments

- Special thanks to OpenAI for providing the Chat-based language model.
- Additional credits to any external libraries or resources used in the project.
