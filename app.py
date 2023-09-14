import streamlit as st 
import pandas as pd 
import os 
from dotenv import load_dotenv 
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI

# Open AI API Key
load_dotenv()

openai_api_key =os.getenv("OPENAI_API_KEY")

# Function for pandas ai to query CSV File
def chat_with_csv(df, prompt):
    llm = OpenAI(api_token=openai_api_key)
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt= prompt)
    print(result)
    return result 
  
st.set_page_config(layout='wide')

st.title("Chat with CSV using LLM")

input_csv = st.file_uploader("Upload your CSV File", type = ["csv"])

if input_csv is not None:
    col1, col2 = st.columns([1,1])

    with col1:
        st.info("CSV Uploaded successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data, use_container_width=True)

    with col2:
        st.info("Chat with CSV File")

        input_text = st.text_area("Enter your query")

        if input_text is not None:
            if st.button("Chat with CSV"):
                st.info("Your Query: "+ input_text)
                result = chat_with_csv(data, input_text)
                st.success(result)


    
