from crewai import Crew,Process
from tasks import product_research,content_creation_task
from agents import product_researcher,content_creator

crew=Crew(
    agents=[product_researcher,content_creator],
    tasks=[product_research,content_creation_task],
    process=Process.sequential,
)

result=crew.kickoff(inputs={'product':'Landcruiser Toyota','country':'Kenya'})
print(result)
