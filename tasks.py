from crewai import Task
from tools import search_tool
from agents import news_researcher , news_writer

## Research Task

research_task = Task(
    description=(
        "Identify the next big trend in {topic}"
        "Focus on identifying the pros and cons ."
        "Your final report should clearly indicate the key points,"
        "its market opportunities and potential risks."
    ),
    expected_output = "A comprehensive 3 paragraph long report on the latest AI trends",
    tool=[search_tool],
    agent=news_researcher
)


## Writing Task 

writing_task=Task(
    description=(
        "Compose an insightfull article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand engaging and positive."
    ),
    expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
    tools=[search_tool],
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)