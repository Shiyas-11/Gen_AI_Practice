from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage
import json
from reviewdata import *
from Analyzer import Analyzer


load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")
out=StrOutputParser()


#prompt
rev_template='''You are a Bot that Accepts a review {review} about a product;
				You as an AI you are to classify these as Positive or Negative review.
				Review stricly should constain only single word value of .
				whether the review is positive or negative.
				'''
email_template='''
				You are an AI that is going to help me write emails.
				I will provide you a review {review} and some details {details}.
				Your objective is to draft emails depending on whether the review is positive or negative.
				For positive review,  a thank you email to customer and also, 
				recommend a new product for them to try.
				Use company Name as XYZ,Draft random name for the product name if not specified in the review
   				For negative review, draft an apology email to customer and also,
				an internal mail to a senior customer service representative to address customer concern
'''

Prompt=ChatPromptTemplate.from_messages(
    [
        ("system",rev_template),
        ("user","{review}")
    ]
)

Review= Prompt | llm | out



Prompt=ChatPromptTemplate.from_messages(
    [
        ("system",email_template),
        ("user","{review}")
    ]
)
Email= Prompt | llm | out



if __name__=="__main__":
	E=open("mails.json","w")
	Emails={}


	R=open("reviews.json","w")
	AI_sorted={}

	for r in Sample_Reviews:
		x=Analyzer(r["customer_name"],r["customer_email"],r["text"],Email,Review)
		AI_sorted[r["customer_name"]]=x["Rating"]
		Emails[r["customer_email"]]=x["Mail"]


	json.dump(Emails,E,indent=4)
	json.dump(AI_sorted,R,indent=4)
	R.close()
	E.close()

