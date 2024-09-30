from crewai import Crew,Process
from tasks import software_tool_research_task,software_tool_content_task
from agents import software_tool_researcher,software_tool_content_creator


## Forming the tech focused team with some enhanced configurations

crew=Crew(
    agents=[software_tool_researcher,software_tool_content_creator],
    tasks=[software_tool_research_task,software_tool_content_task],
    process=Process.sequential,
)


## Starting the task execution process with enhanced feedback

result=crew.kickoff(inputs={'software_project_type':'Ufahamu AI is an AI-driven educational application being developed by you and your team. The app is Kenyan-based and is aimed at addressing gaps between teachers and pupils by helping teachers improve their teaching strategies through AI. It focuses on analyzing student performance and assisting teachers in planning course content and generating specialized continuous assessment tests (CATs). The app also provides students with personalized learning experiences and feedback on their performance. It will utilize next JS and langchain for llm wrapping since the app will be powered by an llm either gemini or openai'},)
print(result)