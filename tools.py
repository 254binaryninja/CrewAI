from crewai_tools import SerperDevTool,LinkedInProfileTool
import os
from dotenv import load_dotenv


os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


## Initialize the serper dev tool

search_tool = SerperDevTool()
linkedin_tool = LinkedInProfileTool()