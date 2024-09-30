from crewai import Task
from tools import search_tool
from agents import software_tool_researcher, software_tool_content_creator

## Research Task for Software Tools

software_tool_research_task = Task(
    description=(
        "Identify and analyze the top 3 most cost-effective tools for {software_project_type} while being as fast as possible. For each tool:\n"
        "1. Name and brief description (1 sentence)\n"
        "2. Top 3 key features\n"
        "3. Pricing model (focus on free tier or lowest cost option)\n"
        "4. User rating (if available, or general sentiment)\n"
        "5. One major advantage for {software_project_type}\n"
        "6. One potential limitation\n"
        "Prioritize tools with free tiers or low-cost options. Use only reputable sources for information."
    ),
    expected_output = "A concise report on 3 cost-effective tools for {software_project_type}, structured as a markdown list with 6 points per tool.",
    tool=[search_tool],
    agent=software_tool_researcher
)

## Content Creation Task for Software Tools

software_tool_content_task = Task(
    description=(
        "Create a brief, engaging blog post about the 3 most cost-effective tools for {software_project_type}. Structure as follows:\n"
        "1. Introduction (2 sentences): Highlight the importance of cost-effective tools in {software_project_type}\n"
        "2. For each tool (3 paragraphs, one per tool):\n"
        "   a. Tool name and its primary function\n"
        "   b. Key cost-saving feature\n"
        "   c. Brief use case or success story (1 sentence)\n"
        "3. Conclusion (2 sentences): Summarize the benefits of these tools and encourage readers to explore them\n"
        "Keep the content concise, informative, and focused on cost-effectiveness."
    ),
    expected_output="A 5-paragraph blog post about cost-effective tools for {software_project_type}, formatted as markdown, optimized for quick reading and social media sharing.",
    tools=[search_tool],
    agent=software_tool_content_creator,
    async_execution=False,
    output_file='cost-effective-software-tools.md'
)