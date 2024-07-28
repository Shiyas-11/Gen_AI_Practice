import streamlit as st

st.header("AIRPORT CHAT BOT")

def init_session():
	if "history" not in st.session_state:
		st.session_state.history=[]
		

chat_placeholer=st.container()
prompt_placeholder=st.form("chat-form")
credit_card_placeholer=st.empty()

with prompt_placeholder:
	col=st.columns((6,1))
	col[0].text_input("CHAT",placeholder="ASK ME HERE",label_visibility="collapsed")
	col[1].form_submit_button("SUBMIT",type="primary")
