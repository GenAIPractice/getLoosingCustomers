## getLoosingCustomers
In this repo we will be adding a code to get the list of customers which are going to miss their rewards

## We will be using below components - 
  - CSVLoader class from langchain
  - Huggingface instructor embeddings: Text embeddings
  - FAISS: Vector databse (Facebook AI Similarity Search)
  - RetrivalQA class of Langchain
  - For prompting : Google Palm- LLM based Q&A
  - Streamlit: UI

## Installation and Local setup
  - Install git on local system
  - Install python 3.11 <DO NOT INSTALL LATEST, I faced lot of copmatibility issues with latest version>
  - git clone https://github.com/GenAIPractice/getLoosingCustomers/edit/main/README.md
  - CD into the directory where you cloned the project and run below command to install all required tools/models for this project
      pip: pip install -r requirements.txt
  - Acquire an api key through makersuite.google.com and put it in .env file
      GOOGLE_API_KEY="your_api_key_here"
    
## How to run on local
  - execute below command for your main.py file
    streamlit run main.py
  - The web app will open in your browser.
  - Type your question/prompt to get the response.
  - Eg. Question : Get me the customer list which are about to missing SLA.

### Note - I am facing issue to store the Vector data base on local, so I have used the in memory/chache database. While tring to save the vector database on local its just running forever.. 
