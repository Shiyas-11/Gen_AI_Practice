import streamlit as st
from prompt import chain,info_input,sprompt,dprompt,tprompt
from streamlit import markdown




st.title(body="AIRPORT CHAT BOT")
st.write("YOUR AI ASSIST-BOT")

if "messages" not in st.session_state:
	st.session_state.messages=[]

with open("static/style.css","r") as f:
	css=f"<style>{f.read()}</style>"
	st.markdown(css,unsafe_allow_html=True)		


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

try:
	print(sc)
except NameError:
	sc=''
try:
	print(dc)
except NameError:
	dc=''
try:
	print(tc)
except NameError:
	tc=''


inputmsg="Type here"
response=''
if query:=st.chat_input(inputmsg):
	divicon=f'''<div class="icon" id="hicon">👤</div>'''
	div=f'''<div class="hquery" id="human"><div class="text" id="htext">{query.capitalize()}</div>{divicon}<div>'''
	st.markdown(div,unsafe_allow_html=True)
	st.session_state.messages.append({"role":"user","message":query})
	response=chain.invoke({"query":query,"Source City":sc,"Destination City":dc,"travel class":tc})
	if sc=="":	sc=info_input(sprompt,query)
	if dc=="":	dc=info_input(dprompt,query)
	if tc=="":	tc=info_input(tprompt,query)

if response:
	divicon=f'''<div class="icon" id="aicon">🤖</div>'''
	div=f'''<div class="aquery" id="aitext" >{divicon}<div class="text">{response}</div></div>'''
	st.markdown(div,unsafe_allow_html=True)
	st.session_state.messages.append({"role":"ai","message":response})
	response=''



	





	
	
	