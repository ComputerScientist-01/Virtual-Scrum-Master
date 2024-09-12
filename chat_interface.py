# chat_interface.py

import streamlit as st

def init_chat_history():
    """Initialize session state to store chat history if not already initialized"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def chatbot_response(user_input):
    """Function to mimic chatbot response"""
    # This is a placeholder response; replace with actual chatbot logic.
    return f"Chatbot: I received '{user_input}'"

def display_chat_interface():
    """Display chat interface with bubbles inside a scrollable container"""
    chat_css = """
    <style>
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        padding-right: 20px;
    }

    .chat-bubble {
        max-width: 60%;
        padding: 10px;
        border-radius: 15px;
        margin: 10px 0;
        line-height: 1.6;
    }

    .user-bubble {
        background-color: #DCF8C6;
        margin-left: auto;
        text-align: right;
        color: black;
    }

    .bot-bubble {
        background-color: #ECECEC;
        margin-right: auto;
        color: black;
    }
    </style>
    """

    st.markdown(chat_css, unsafe_allow_html=True)

    user_input = st.text_input("You:", key="user_input")

    if user_input:
        init_chat_history()
        st.session_state.chat_history.append({"message": f"You: {user_input}", "is_user": True})
        response = chatbot_response(user_input)
        st.session_state.chat_history.append({"message": response, "is_user": False})
        st.session_state.user_input = ""

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["is_user"]:
            st.markdown(f'<div class="chat-bubble user-bubble">{chat["message"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble bot-bubble">{chat["message"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)