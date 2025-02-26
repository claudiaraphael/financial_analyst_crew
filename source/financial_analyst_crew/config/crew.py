from crewai import Agent, Crew, Process, Task # 4 main pillars of a crewai process. + Teams?
from crewai.project import CrewBase, Agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class FinancialAnalystCrew():
    # describe what it is
    """"FinancialAnalystCrew crew"""

    # load up the agents and tasks you set up
    agents_config = 'config/agents.yaml'
    task_config = 'config/task.yaml'

def __init__(self) -> None:
    self.groq_llm = ChatGroq(temperature=0, model_name = "mixtral-8x7b-32768")