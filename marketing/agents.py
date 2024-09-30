from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from tools import search_tool,yt_tool

load_dotenv()

##Initialize your LLM

llm=ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

## Initialize agents 

product_researcher=Agent(
  role="Product Researcher",
  goal='gather information about {product} in the {country} it is in  and the various competitors it has using online sources',
  backstory=(
      "Driven by the desire to improve businesses using information ,"
      "you are an expert product research specialist with over 10 years experience."
  ),
  llm=llm,
  verbose=True,
  memory=True,
  tools=[search_tool],
  allow_delegation=True,
)


content_creator=Agent(
  role="Content Creator",
  goal='create blog content for the purpose of marketing {product} on social media platforms such as Instagram , LinkedIn and tiktok',
  backstory=(
      "You are a renonwed Kenyan content creator with over 5 years of experience ,"
      "you are driven by desire to improve business by creating content that they can post ,"
      "on their various social media platforms and analyzing various youtube videos for inspiration."
  ),
  llm=llm,
  verbose=True,
  allow_delegation=True,
  tools=[search_tool,yt_tool],
)