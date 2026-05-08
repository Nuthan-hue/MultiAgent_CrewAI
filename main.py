import os
from crewai import Agent, Task, Crew, Process, LLM

# WARNING: Never hardcode your API key when sharing to a Git repo!
# Set it in your terminal instead: export GROQ_API_KEY="your-key-here"
# os.environ['GROQ_API_KEY'] = 'your-key-here'

def main():
    # Initialize the LLM using CrewAI's built-in wrapper (powered by LiteLLM)
    llm = LLM(model="groq/llama-3.3-70b-versatile")

    # Define the Agents
    researcher = Agent(
        role='Senior Tech Researcher',
        goal='Uncover groundbreaking technologies in AI',
        backstory='You are a curious researcher, always looking for the latest advancements in artificial intelligence.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    writer = Agent(
        role='Tech Content Writer',
        goal='Write an engaging blog post about the latest AI technologies',
        backstory='You are a skilled writer who simplifies complex tech concepts into engaging articles for the general public.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # Define the Tasks
    research_task = Task(
        description='Identify the top 3 most promising AI trends of the current year. Focus on real-world applications and potential impact.',
        expected_output='A bulleted list of the top 3 AI trends with a brief description and their real-world impact.',
        agent=researcher
    )

    write_task = Task(
        description='Using the insights from the researcher, write a short, engaging blog post (around 300 words) summarizing these AI trends.',
        expected_output='A blog post of approximately 300 words, with a catchy title and an engaging tone, summarizing the AI trends.',
        agent=writer
    )

    # Assemble the Crew
    tech_crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential, # Tasks will be executed one after another
        verbose=True
    )

    # Run the Crew
    print("Starting the Crew execution...")
    result = tech_crew.kickoff()
    
    print("\n######################")
    print("FINAL RESULT")
    print("######################\n")
    print(result)

if __name__ == "__main__":
    main()
