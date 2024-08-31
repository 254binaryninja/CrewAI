from crewai import Crew,Process
from tasks import research_task,writing_task
from agents import news_researcher,news_writer


## Forming the tech focused team with some enhanced configurations

crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,writing_task],
    process=Process.sequential,
)


## Starting the task execution process with enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)