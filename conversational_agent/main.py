from flask import Flask, render_template, request, send_file
import panel as pn
from bokeh.embed import server_document
from dotenv import load_dotenv, find_dotenv
from tool import *
import os
import openai
from utils import *
from google_tools import *
_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

app = Flask(__name__)

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
    weather_forecast,
    geocode_address,
    reverse_geocode_coordinates,
    calculate_distance_matrix,
    place_search,
    get_elevation,
    get_time_zone,
    get_directions,
    generate_static_map,
    get_place_details,
    autocomplete_places,
    calculate_distance_matrix_extended,
    get_nearby_places,
    generate_static_street_view,
    
]

cb = cbfs(tools)
button_clearhistory = pn.widgets.Button(name="Clear History", button_type='warning')
button_clearhistory.on_click(cb.clr_history)
inp = pn.widgets.TextInput(placeholder='Enter text here…')

conversation = pn.bind(cb.convchain, inp) 

tab1 = pn.Column(
    pn.Row(button_clearhistory, pn.pane.Markdown("Clears chat history. Can use to start a new topic")),
    pn.Row(inp),
    pn.layout.Divider(),
    pn.panel(conversation,  loading_indicator=True, height=400),

)

dashboard = pn.Column(
    pn.Row(pn.pane.Markdown('# QnA_Bot')),
    pn.Tabs(('Conversation', tab1))
)

# Serve the Panel app
panel_server = pn.serve(dashboard, show=False,port=0)

@app.route('/')
def index():
    # Get the Bokeh script
    bokeh_script=server_document(url='http://localhost:{}'.format(panel_server.port), relative_urls=True)
    return render_template('index.html', bokeh_script=bokeh_script)

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)