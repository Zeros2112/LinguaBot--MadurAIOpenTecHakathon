from app import *

def extracting(link):
    # Create a WebBaseLoader instance to load documents from the given link
    loader = WebBaseLoader(link)
    # Load documents from the web page
    documents = loader.load()

    # Initialize a RecursiveCharacterTextSplitter with a specified chunk overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_overlap=0)

    # Define a list of extraction functions, in this case, a single function to convert Pydantic model to OpenAI function
    paper_extraction_function = [
        convert_pydantic_to_openai_function(Info)
    ]

    # Create an instance of the model and bind it to the specified extraction function
    extraction_model = model.bind(
        functions=paper_extraction_function,
        function_call={"name": "Info"}
    )

    # Define an extraction chain that includes a prompt, the extraction model, and a JsonKeyOutputFunctionsParser
    extraction_chain = prompt | extraction_model | JsonKeyOutputFunctionsParser(key_name="papers")

    # Define a RunnableLambda that prepares the input data for the extraction chain
    prep = RunnableLambda(
        lambda x: [{"input": doc} for doc in text_splitter.split_text(x)]
    )

    # Define a chain of operations using the prep, extraction_chain.map(), and flatten functions
    chain = prep | extraction_chain.map() | flatten

    # Invoke the extraction chain on the page content of the first document
    return chain.invoke(documents[0].page_content)
