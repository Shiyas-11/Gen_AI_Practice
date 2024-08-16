import streamlit as st
from prompt import chain
from streamlit import markdown
from langchain_core.messages import HumanMessage,AIMessage



st.title(body="AIRPORT CHAT BOT")
st.write("YOUR AI ASSIST-BOT")

if "messages" not in st.session_state:
	st.session_state.messages=[]

with open("static/style.css","r") as f:
	css=f"<style>{f.read()}</style>"
	st.markdown(css,unsafe_allow_html=True)		

chats=[]
for message in st.session_state.messages:
	icon="🤖" if message["role"]=="ai" else "👤"
	align="htext" if message["role"]!="ai" else "aitext"
	if message["role"]=="ai":
		divicon=f'''<div class="icon" id="aicon">{icon}</div>'''
		div=f'''<div class="aquery" id="{message["role"]}">{divicon}<div class="text" id="{align}">{message["message"]}</div></div>'''
	else:
		divicon=f'''<div class="icon" id="hicon">{icon}</div>'''
		div=f'''<div class="hquery" id="{message["role"]}"><div class="text" id="{align}">{message["message"].capitalize()}</div>{divicon}</div>'''
	st.markdown(div,unsafe_allow_html=True)


inputmsg="Type here"
response=''
if query:=st.chat_input(inputmsg):
	divicon=f'''<div class="icon" id="hicon">👤</div>'''
	div=f'''<div class="hquery" id="human"><div class="text" id="htext">{query.capitalize()}</div>{divicon}<div>'''
	st.markdown(div,unsafe_allow_html=True)
	st.session_state.messages.append({"role":"user","message":query})
	response=chain.invoke({"chats":st.session_state.messages,"query":query})

if response:
	divicon=f'''<div class="icon" id="aicon">🤖</div>'''
	div=f'''<div class="aquery" id="aitext" >{divicon}<div class="text">{response}</div></div>'''
	st.markdown(div,unsafe_allow_html=True)
	st.session_state.messages.append({"role":"ai","message":response})
	response=''




	


	





	
	
	