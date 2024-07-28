import streamlit as st
from prompt import chain
from streamlit import markdown

st.header("AIRPORT CHAT BOT")
st.write("YOUR AI ASSIST-BOT")

if "messages" not in st.session_state:
	st.session_state.messages=[]

with open("static/style.css","r") as f:
	css=f"<style>{f.read()}</style>"
	st.markdown(css,unsafe_allow_html=True)		


for message in st.session_state.messages:
	divmsg=f'''<div id="{message["role"]}">
	{message["message"]}</div>'''
	divicon="🤖" if message["role"]=="ai" else "👤"
	div=f'''<div class="query" id="{message["role"]}>{divicon}</div>'''
	st.markdown(div,unsafe_allow_html=True)



inputmsg="Type here"
response=''
traveltype=""
if query:=st.chat_input(inputmsg):
	col=st.columns((1,10))
	div=f'''<div class="query">
	{query}</div>'''
	col[0].chat_message("ai",avatar="👤")
	col[1].markdown(div,unsafe_allow_html=True)
	st.session_state.messages.append({"role":"user","message":query})
	response=chain.invoke({"chats":st.session_state.messages,"query":query})
	

if response:
	col=st.columns((1,10))
	div=f'''<div class="query" id="ai">
	{response}</div>'''
	col[0].chat_message("ai",avatar="👤")
	col[1].markdown(div,unsafe_allow_html=True)
	st.session_state.messages.append({"role":"ai","message":response})
	response=''
	

	





	
	
	