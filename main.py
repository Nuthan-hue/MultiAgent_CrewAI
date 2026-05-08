import os
from crewai import Agent, Task, Crew, Process, LLM
from langchain_community.tools import DuckDuckGoSearchRun

# WARNING: Never hardcode your API key when sharing to a Git repo!
# Set it in your terminal instead: export GROQ_API_KEY="your-key-here"
# os.environ['GROQ_API_KEY'] = 'your-key-here'

def main():
    # Initialize the LLM using CrewAI's built-in wrapper
    llm = LLM(model="groq/llama-3.3-70b-versatile")
    
    # Initialize a free web search tool by creating a native CrewAI tool
    from crewai.tools import BaseTool
    from langchain_community.tools import DuckDuckGoSearchRun
    
    class WebSearchTool(BaseTool):
        name: str = "Web Search"
        description: str = "Search the web for current events or recent information."
        
        def _run(self, search_query: str) -> str:
            duckduckgo_search = DuckDuckGoSearchRun()
            return duckduckgo_search.run(search_query)

    search_tool = WebSearchTool()

    # ==========================================
    # 1. DEFINE THE AGENTS (The "Employees")
    # ==========================================
    
    researcher = Agent(
        role='Senior Tech Researcher',
        goal='Uncover groundbreaking technologies in AI by actively searching the web',
        backstory='You are a curious researcher, always looking for the latest advancements in artificial intelligence. You dive deep into the internet to find cutting-edge trends and refuse to rely purely on your training data.',
        verbose=True,
        allow_delegation=False,
        tools=[search_tool], # Giving the agent the ability to use tools
        llm=llm
    )

    writer = Agent(
        role='Tech Content Writer',
        goal='Write an engaging, long-form blog post about the latest AI technologies based on research',
        backstory='You are a skilled writer who simplifies complex tech concepts into highly engaging articles for the general public.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    editor = Agent(
        role='Editor-in-Chief',
        goal='Ensure the blog post is perfectly formatted, highly engaging, and grammatically flawless.',
        backstory='You are a meticulous editor with years of experience in tech journalism. You accept nothing but the absolute best quality content and will aggressively re-format drafts.',
        verbose=True,
        allow_delegation=True, # The editor can delegate tasks or ask questions back to the writer/researcher!
        llm=llm
    )

    # ==========================================
    # 2. DEFINE THE TASKS (The "Assignments")
    # ==========================================
    
    research_task = Task(
        description='Search the web to identify the top 3 most promising AI trends happening RIGHT NOW. You must use your search tool to find recent information. Focus on real-world applications and potential impact.',
        expected_output='A detailed research report of the top 3 AI trends with a brief description, sources found via search, and their real-world impact.',
        agent=researcher
    )

    write_task = Task(
        description='Using the insights from the researcher, write a comprehensive, engaging blog post (around 500 words) summarizing these AI trends. Include catchy headings and bullet points.',
        expected_output='A drafted blog post of approximately 500 words, with a catchy title and an engaging tone.',
        agent=writer,
        context=[research_task] # Explicitly stating it relies on the output of the research task
    )

    edit_task = Task(
        description='Review the drafted blog post from the writer. Check for clarity, engagement, formatting (Markdown), and impact. Make edits to improve the flow and punchiness of the article.',
        expected_output='The final, polished blog post ready for publication in Markdown format.',
        agent=editor,
        context=[write_task]
    )

    # ==========================================
    # 3. ASSEMBLE THE CREW (The "Company")
    # ==========================================
    
    tech_crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, write_task, edit_task],
        process=Process.sequential, 
        verbose=True
    )

    # ==========================================
    # 4. KICKOFF
    # ==========================================
    
    print("Starting the Complex Crew execution...")
    result = tech_crew.kickoff()
    
    print("\n######################")
    print("FINAL PUBLISHED ARTICLE")
    print("######################\n")
    print(result)

if __name__ == "__main__":
    main()
