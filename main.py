import streamlit as st

from emailHelper import send_custom_email
from langchain_helper import get_eligible_customer_chain

st.title("Missing Customers..")

question = st.text_input("Question: ")

if st.button:
    send_custom_email()

if question:
    chain = get_eligible_customer_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
    st.button("Send Email")






