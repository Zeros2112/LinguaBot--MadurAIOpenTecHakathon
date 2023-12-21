from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from typing import List
from pydantic import BaseModel, Field
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
import os
import openai
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser
from langchain.document_loaders import WebBaseLoader
from langchain.schema.runnable import RunnableLambda
from typing import Optional
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


model = ChatOpenAI(temperature=0)

app = Flask(__name__)
CORS(app)

def flatten(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list

template = """A article will be passed to you. Extract from it all papers that are mentioned by this article. 

Do not extract the name of the article itself. If no papers are mentioned that's fine - you don't need to extract any! Just return an empty list.

Do not make up or guess ANY extra information. Only extract what exactly is in the text."""

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", "{input}")
])


def extracting(link):
    loader = WebBaseLoader(link)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_overlap=0)
    
    paper_extraction_function = [
        convert_pydantic_to_openai_function(Info)
    ]
    extraction_model = model.bind(
        functions=paper_extraction_function, 
        function_call={"name":"Info"}
    )
    extraction_chain = prompt | extraction_model | JsonKeyOutputFunctionsParser(key_name="papers")
    prep = RunnableLambda(
        lambda x: [{"input": doc} for doc in text_splitter.split_text(x)]
    )
    chain = prep | extraction_chain.map() | flatten
    return chain.invoke(documents[0].page_content)
    
    
    
    
    
    
    
class Paper(BaseModel):
    """Information about papers mentioned."""
    title: str
    author: Optional[str]



class Info(BaseModel):
    """Information to extract"""
    papers: List[Paper]



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_response', methods=['POST'])
def generate_response():
    link = request.form.get('link') 
    
    response = extracting(link)


    return render_template('results.html', link=link, response=response)

if __name__ == '__main__':
    app.run(debug=True)
