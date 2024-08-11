from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#prompt

sys_template='''

Instructions:

Identify Missing Information:

If the user has not provided the Source City, destination city, or travel class, check if user mentioned any information on previous chat {chats}.

User Input:

Source City: {chats}[?].content.extract("Source City:(.*?)[\\n\\r|\\r|\\n| ]")|first,
Destination City: {chats}[?].content.extract("Destination City:(.*?)[\\n\\r|\\r|\\n| ]")|first,
Travel Class: {chats}[?].content.extract("Travel Class:(.*?)[\\n\\r|\\r|\\n| ]")|first,

Note: If the above values are not present in the chat history, prompt the user to provide missing information.

Prompting for Missing Information (If any):

DO NOT PROMPT THE USER FOR THE ABOVE IF THE DETAILS ARE PRESENT IN {chats}.

Providing Relevant Information:
Once you have collected the Source City, destination city, and travel class, provide the user with the specific information they need based on their input.
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
