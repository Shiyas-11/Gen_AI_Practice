from Analyzer import Analyzer
import streamlit as st
from ReviewSystem import Email,Review
from json import dump

st.header("Review Bot")
st.write("YOUR AI ASSIST-BOT")

st.caption("NAME")
name=st.text_input("INPUT NAME")
st.caption("EMAIL")
email=st.text_input("INPUT EMAIL")
st.caption("Review")
rev=st.text_area("INPUT REVIEW")
button=st.button("Submit")

AI_sorted={}
Emails={}
if button:
	if name and email and rev:
		out=Analyzer(name,email,rev,Email,Review)
		AI_sorted[email]=out["Rating"]
		Emails[email]=out["Mail"]
		st.caption("Rating")
		st.write(out["Rating"]["review"])
		st.write(out["Mail"][email])

with open("mails.json","a") as E:
	dump(Emails,E,indent=4)
with open("reviews.json","a") as R:
	dump(AI_sorted,R,indent=4)



	
	
	