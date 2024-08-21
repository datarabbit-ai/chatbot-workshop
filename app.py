import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

st.title("ChatGPT-like clone")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

model = ChatOpenAI(model=st.session_state["openai_model"], api_key=st.secrets["OPENAI_API_KEY"])

config = {"configurable": {"session_id": f"demo"}}

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = model.stream(
            [
                (
                    HumanMessage(content=message["content"])
                    if message["role"] == "user"
                    else AIMessage(content=message["content"])
                )
                for message in st.session_state.messages
            ],
            config=config,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
