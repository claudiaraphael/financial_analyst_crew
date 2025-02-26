from crewai import Agent, Crew, Process, Task # 4 main pillars of a crewai process. + Teams?
from crewai.project import CrewBase, Agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class FinancialAnalystCrew():
    # describe what it is
    """"FinancialAnalystCrew crew"""

    # load up the agents and tasks you set up
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/task.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, model_name = "mixtral-8x7b-32768")

    @agent 
    def financial_researcher(self) -> Agent:
        return Agent(
            config = self.agents_config['financial_researcher'],
            llm = self.groq_llm
        )
     @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config = self.agents_config['financial_analyst'],
            llm = self.groq_llm
        )
    
    @task
    def research_company(self) -> Task:
        return Task(
            config = self.tasks_config['financial_research'],
            agent = self.financial_researcher()

        )
    @crew
        def crew(self) -> Crew:
            """Creates the FinancialAnalystCrew crew"""
            return Crew(
                agents = self.agents,
                tasks = self.tasks,
                process = Process.sequential,
                verbose = 2
            )
