import streamlit as st
import requests

def get_chatbot_response(message):
    url = "http://127.0.0.1:8000/chat"
    body = {
        "message": message
    }

    response = requests.post(url, json=body)

    if response.status_code == 200:
        return response.json().get("answer", "No response from chatbot.")
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.title("Chatbot Interaction")
    
    user_message = st.text_input("You:", "")
    if st.button("Send"):
        st.text("Chatbot:")
        with st.spinner('generating answer') as spinner :
            if user_message:
                st.write(get_chatbot_response(user_message))

if __name__ == "__main__":
    main()