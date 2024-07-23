from Analyzer import Analyzer
import streamlit as st
from ReviewSystem import Email,Review
from json import dump,load

st.header("Review Bot")
st.write("YOUR AI ASSIST-BOT")

st.caption("NAME")
name=st.text_input("INPUT NAME")
st.caption("EMAIL")
email=st.text_input("INPUT EMAIL")
st.caption("Review")
rev_text=st.text_area("INPUT REVIEW")
button=st.button("Submit")
rev=st.file_uploader("OR \n Upload JSON file of reviews here for analysis:",type="json")
button2=st.button("Submit Json")
AI_sorted={}
Emails={}
if button:
	if name !='' and email !='' and rev_text !='':
		out=Analyzer(name,email,rev_text,Email,Review)
		AI_sorted[email]=out["Rating"]
		Emails[email]=out["Mail"]
		st.caption("Rating")
		print("done")
		st.write(out["Rating"]["review"])
		st.write(out["Mail"][email])
		st.success("YOUR REVIEW HAVE BEEN SUBMITTED SUCCESSFULLY")
		with open("mails.json","w") as E:
			dump(Emails,E,indent=4)
		with open("reviews.json","w") as R:
			dump(AI_sorted,R,indent=4)

	else:
		st.warning("NOT ENOUGH INFORMATION")
elif button2:
	rev=load(rev)
	for r in rev:
		out=Analyzer(name,email,rev[r],Email,Review)
		AI_sorted[email]=out["Rating"]
		Emails[email]=out["Mail"]
		# st.caption("Rating")
		# st.write(out["Rating"]["review"])
		# st.write(out["Mail"][email])
	st.success("THE REVIEWS HAVE BEEN SEND FOR ANALYSIS  SUCCESSFULLY")
	with open("mails.json","w") as E:
		dump(Emails,E,indent=4)
	with open("reviews.json","w") as R:
		dump(AI_sorted,R,indent=4)



	
	
	