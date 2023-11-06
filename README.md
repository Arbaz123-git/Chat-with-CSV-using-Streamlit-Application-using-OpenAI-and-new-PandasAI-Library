creating a Streamlit web application that allows users to upload a CSV file, query the data in the CSV file using the OpenAI GPT-3 model (LLM), and view the model's responses on the web page. It provides an interactive way to interact with and extract information from CSV data using natural language queries.

Building chat with CSV file ChatBOT which uses latest advances in Generative AI with the help of PandasAI, a new library that helps you chat with your CSV Files. 

First create your new virtual environment using this command in your projects folder
>>python -m venv venv

You can give any name to your virtual environment I have given venv in my case 

To make this project first install all the dependencies which I have mentioned in my requirements.txt file by typing in project folders command prompt 
>>pip install -r reqirements.txt

After installing all the dependencies create two more files 
.env 
app.py
to add your secret key OPenAI API Key in it and use it in your code 

Then Start writing the your code in your app.py file 

To run the Streamlit app write in your cmd this command 
>>streamlit run app.py 

