from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#prompt





sys_template='''
you are running a fictional pizzeria,you are a chat bot that takes orders  from the customers based on a menu {menu} you have
,based on the chats you need to provide the total amount back to the customer when they say they are done ordering or when they ask you how much 
has the total become now,if the item is not in the menu then say that the item is unavailabale
for pizzas and drinks like coke,sprite  the menu contains price for each size large,medium,small respectively ,fries have large and small respectively and 
bottled water & toppings have their own prices
provide a decent looking menu template for the menu i provide each time the customer asks for the menu.
chat history is provided as {chats}.
'''

menu={"Pizza":{
    "pepperoni pizza" :[ 12.95, 10.00, 7.00] ,
	"cheese pizza" :  [10.95, 9.25, 6.50] ,
	"eggplant pizza"  : [11.95, 9.75, 6.75] ,
	"fries": [4.50, 3.50] ,
	"greek salad": 7.25 },
"Toppings": {
	"extra cheese": 2.00, 
	'mushrooms' :1.50 ,
	'sausage' :3.00 ,
	'canadian bacon': 3.50 ,
	"AI sauce" :1.50 ,
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


while True:
    item=input("You >>")
    if item=="quit":
        break
    chats.append(HumanMessage(content=item))
    response=chain.invoke({"chats":chats,"menu":menu,"item":item})
    print("AI >>",response)
    chats.append(AIMessage(content=response))


