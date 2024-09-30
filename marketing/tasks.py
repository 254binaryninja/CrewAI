from crewai import Task
from agents import product_researcher,content_creator
from tools import search_tool,yt_tool
##Research Task

product_research=Task(
     description=(
         "Focus on gathering detailed information about {product} in {country}, including market share,"
          " key features, pricing, and main competitors."
     ),
        agent=product_researcher,
        expected_output="A comprehensive report on the product, its market position, and competitors",
        tool=[search_tool],
        async_execution=True,
    )


### Content creation

content_creation_task = Task(
        description=(
            "Use the research information to create engaging content for {product}. Include hashtags," 
            "captions, and content ideas for each platform."),
        agent=content_creator,
        expected_output="A set of social media posts for Instagram, LinkedIn, and TikTok",
        async_execution=False,
        tool=[search_tool,yt_tool],
        output_file='content-blog.md'
    )
