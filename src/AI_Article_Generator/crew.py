"""Crew module for AI Article Generator."""

import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from crewai.agents.cache import CacheHandler
from langchain_google_genai import ChatGoogleGenerativeAI
from .tools import GeminiResearchTool, GeminiFeedbackAnalysisTool

# Configure the agent cache
cache_handler = CacheHandler(enabled=True)
@CrewBase
class AI_Article_Generator():
    """CrewAutomationWithMultiAiAgentsForArticleGeneration crew"""

    def __init__(self):
        """Initialize the crew with Gemini LLM."""
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            verbose=True,
            temperature=0.7
        )

    @agent
    def article_researcher(self) -> Agent:
        """Create the article researcher agent."""
        return Agent(
            config=self.agents_config['article_researcher'],
            tools=[ScrapeWebsiteTool(), GeminiResearchTool()],
            llm=self.llm,
            verbose=True
        )

    @agent
    def article_outline_designer(self) -> Agent:
        """Create the article outline designer agent."""
        return Agent(
            config=self.agents_config['article_outline_designer'],
            tools=[],
            llm=self.llm,
            verbose=True
        )

    @agent
    def article_writer(self) -> Agent:
        """Create the article writer agent."""
        return Agent(
            config=self.agents_config['article_writer'],
            tools=[],
            llm=self.llm,
            verbose=True
        )

    @agent
    def article_editor(self) -> Agent:
        """Create the article editor agent."""
        return Agent(
            config=self.agents_config['article_editor'],
            tools=[],
            llm=self.llm,
            verbose=True
        )

    @agent
    def data_flywheel_coordinator(self) -> Agent:
        """Create the data flywheel coordinator agent."""
        return Agent(
            config=self.agents_config['data_flywheel_coordinator'],
            tools=[GeminiFeedbackAnalysisTool()],
            llm=self.llm,
            verbose=True
        )

    @task
    def research_article_task(self) -> Task:
        """Create the research article task."""
        return Task(
            config=self.tasks_config['research_article_task'],
            tools=[ScrapeWebsiteTool(), GeminiResearchTool()],
            agent=self.article_researcher
        )

    @task
    def outline_article_task(self) -> Task:
        """Create the outline article task."""
        return Task(
            config=self.tasks_config['outline_article_task'],
            tools=[],
            agent=self.article_outline_designer,
            context=[self.research_article_task]
        )

    @task
    def draft_article_task(self) -> Task:
        """Create the draft article task."""
        return Task(
            config=self.tasks_config['draft_article_task'],
            tools=[],
            agent=self.article_writer,
            context=[self.research_article_task, self.outline_article_task]
        )

    @task
    def edit_article_task(self) -> Task:
        """Create the edit article task."""
        return Task(
            config=self.tasks_config['edit_article_task'],
            tools=[],
            agent=self.article_editor,
            context=[self.draft_article_task]
        )

    @task
    def data_flywheel_task(self) -> Task:
        """Create the data flywheel task."""
        return Task(
            config=self.tasks_config['data_flywheel_task'],
            tools=[GeminiFeedbackAnalysisTool()],
            agent=self.data_flywheel_coordinator,
            context=[self.edit_article_task]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewAutomationWithMultiAiAgentsForArticleGeneration crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            manager_llm=self.llm
        )