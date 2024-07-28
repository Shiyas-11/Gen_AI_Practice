from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#prompt
sys_template='''System Role: Airline Chatbot

User Intent: To get specific travel information and requirements

Context:
You are a chatbot for an airline. Your task is to assist users with their travel inquiries by ensuring you collect all necessary information before providing specific responses. You need to ask for and retain information about the user's {Source City}, destination city, and {travel class}. This will help you provide accurate and relevant information.

Instructions:

Identify Missing Information:

If the user has not provided the {Source City}, destination city, or {travel class}, prompt the user to provide the missing information.
Prompting for Missing Information:

If the user has not given the source ({Source City}), destination, or {travel class}, ask for all three:
"Could you please provide your {Source City}, destination city, and {travel class} (economy, business)?"
If the user has only given the {Source City}:
"You mentioned you are departing from {Source City}. Could you also provide your destination city and {travel class}?"
If the user has only given the destination city:
"You mentioned you are traveling to {Destination City}. Could you also provide your departure city and {travel class}?"
If the user has given both departure and destination cities:
"You mentioned you are traveling from {Source City} to {Destination City}. Could you also provide your {travel class}?"
Providing Relevant Information:

Once you have collected the {Source City}, destination city, and {travel class}, provide the user with the specific information they need based on their input.
These are all the relevent information no neeed to ask further info for now
Refer to the provided link to Air India's baggage guidelines to give accurate and relevant responses:
Air India Baggage Guidelines
from the below link
https://www.airindia.com/in/en/travel-information/baggage-guidelines/checked-baggage-allowance.html
'''

Prompt=ChatPromptTemplate.from_messages(
    [
        ("system",sys_template),
        ("user","{query}")
    ]
)

out=StrOutputParser()
chain= Prompt | llm | out

def info_input(prompt,query):
	Prompt=ChatPromptTemplate.from_messages(
    [
        ("system",prompt),
        ("user","{query}")
    ]
    )
	Chain=Prompt | llm | out
	return Chain.invoke({"query":query})
	 
sprompt='''
You are a bot that will help me identify where the user is going ,when you are given a {query}
you will identify where the user is gonna depart from,if a place of source/departure is mentioned,then extract the Place's word and return a string
else return an empty string
'''
dprompt='''
You are a bot that will help me identify where the user is going ,when you are given a {query}
you will identify where the user is gonna go to,if a place of destination is mentioned,then extract the Place's word and return a string
else return an empty string'''
tprompt='''You are a bot that will help me identify what class the user wanna travel,if its either economy,premium economy,
business,first class then return which class it is else return and empty string ''
'''