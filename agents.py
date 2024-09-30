import os
from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))

software_tool_researcher = Agent(
    role="Software Tool Researcher",
    goal='Uncover and analyze cutting-edge tools for {software_project_type}',
    backstory=(
        "As a seasoned software engineer with a passion for efficiency, "
        "you're always on the lookout for the best tools to streamline "
        "development processes and boost productivity."
    ),
    llm=llm,
    verbose=True,
    memory=True,
    max_retry_limit=25,
    max_iter=None,
    max_execution_time=None,
    max_rpm=15,
    tools=[search_tool],
    allow_delegation=True
)

software_tool_content_creator = Agent(
    role="Software Tool Content Creator",
    goal="Create compelling content about top tools for {software_project_type}",
    backstory=(
        "With a knack for explaining complex technical concepts in simple terms, "
        "you craft engaging content that helps developers and project managers "
        "make informed decisions about the tools they use."
    ),
    llm=llm,
    verbose=True,
    memory=True,
    max_retry_limit=25,
    max_iter=None,
    max_execution_time=None,
    max_rpm=15,
    tools=[search_tool],
    allow_delegation=False
)