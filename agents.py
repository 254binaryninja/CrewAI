import os
from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
## Call the gemini models

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))


# Creating a senior research agent with verbose and memory

news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    backstory=(
        "Driven by curiosity, you are at the forefront of,"
        "innovation, eager to explore and share knowledge that could change ,"
        "the world . "
    ),
    llm=llm,
    verbose=True,
    memory=True,
    tools=[search_tool],
    allow_delegation=True
)

#Creating a writer agent that will be responsible in writing news blog

news_writer=Agent(
   role="Writer",
   goal="Narrate compelling tech stories about {topic}",
   backstory=(
       "With a flair for simplifying complex topics , you craft"
       "engaging narratives that captivate and educate bringing new,"
       "discoveries to life in an accessible manner."
   ),
    llm=llm,
    verbose=True,
    memory=True,
    tools=[search_tool],
    allow_delegation=False
)