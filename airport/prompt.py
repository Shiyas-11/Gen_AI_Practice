from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#prompt
sys_template='''
'''

Prompt=ChatPromptTemplate.from_messages(
    [
        ("system",sys_template),
        ("user","{query}")
    ]
)

out=StrOutputParser()
chain= Prompt | llm | out
chats=[]
