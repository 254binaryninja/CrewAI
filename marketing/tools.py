from crewai_tools import SerperDevTool
import os
from langchain_community.tools import YouTubeSearchTool
from dotenv import load_dotenv


os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


## Initialize the serper dev tool

search_tool = SerperDevTool()
yt_tool=YouTubeSearchTool()