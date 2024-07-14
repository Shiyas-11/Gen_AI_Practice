import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#prompt
sys_template='''
you are running a fictional pizzeria,
you are a chat bot that takes orders from the customers based on a menu {menu} 
and a chat history  provided as {chats}.
based on the chats when they say they are done ordering or when they ask you how much has the total become now,
you need to provide the total amount back to the customer,
if the item is not in the menu then say that the item is unavailabale,
for pizzas and drinks like coke,sprite etc where i provided multiple rates:the menu contains price for each size large,medium,small respectively ,
same goes for fries but have large and small respectively , 
bottled water & toppings have their own prices per piece/topping,
provide a decent looking menu template for the menu i provided when customer asks for the menu.
When user say they want any kind of pizza do remind them that they can shoose toppings and stuff
when toppings are mentioned along with the pizza account the cost for the total amount
'''

menu={"Pizza":{
		"pepperoni pizza" :[ 12.95, 10.00, 7.00] ,
		"cheese pizza" :  [10.95, 9.25, 6.50] ,
		"eggplant pizza"  : [11.95, 9.75, 6.75] },
	"Extras":{
        "fries": [4.50, 3.50] ,
		"greek salad": 7.25 },
	"Toppings": {
		"extra cheese": 2.00, 
		'mushrooms' :1.50 ,
		'sausage' :3.00 ,
		'canadian bacon': 3.50 ,
		"sauce" :1.50 ,
		"peppers": 1.00 ,
		},
	"Drinks": {
		"coke": [3.00, 2.00, 1.00 ],
		"sprite": [3.00, 2.00, 1.00 ],
		"bottled water" :5.00 ,
		}
}

Prompt=ChatPromptTemplate.from_messages(
    [
        ("system",sys_template),
        ("user","{item}")
    ]
)

out=StrOutputParser()
chain= Prompt | llm | out
chats=[]


st.header("Fantzia-Pizzeria")
st.write("YOUR AI ASSIST-BOT")

if "messages" not in st.session_state:
	st.session_state.messages=[]

for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["message"])

inputmsg="Type here"
response=''
if item:=st.chat_input(inputmsg):
	with st.chat_message("User"):
		st.markdown(item)
	chats.append(HumanMessage(content=str(item)))
	st.session_state.messages.append({"role":"user","message":item})
	response=chain.invoke({"chats":chats,"menu":menu,"item":item})

if response:
	with st.chat_message("ai"):
		st.markdown(response)
	chats.append(AIMessage(content=str(response)))
	st.session_state.messages.append({"role":"ai","message":response})
	response=''
print(chats)



	
	
	