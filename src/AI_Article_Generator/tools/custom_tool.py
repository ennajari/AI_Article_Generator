"""Custom tools for AI Article Generator."""

import os
from typing import Type, List, Optional
import google.generativeai as genai
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

class GeminiResearchToolInput(BaseModel):
    """Input schema for GeminiResearchTool."""
    query: str = Field(..., description="The research query or topic to investigate")
    additional_context: Optional[str] = Field(None, description="Additional context or constraints for the research")

class GeminiResearchTool(BaseTool):
    """Tool for performing research using Gemini AI."""
    
    name: str = "Gemini Research Tool"
    description: str = (
        "Uses Gemini 2.0 Flash to perform in-depth research on a topic. "
        "Provide a query and any additional context to get comprehensive information."
    )
    args_schema: Type[BaseModel] = GeminiResearchToolInput

    def _run(self, query: str, additional_context: Optional[str] = None) -> str:
        """Run the tool to perform research using Gemini."""
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            prompt = f"I need comprehensive research on the following topic: {query}."
            if additional_context:
                prompt += f"\nAdditional context: {additional_context}"
            prompt += (
                "\nPlease provide a detailed response covering key aspects, main concepts, "
                "relevant data points, and expert opinions if available. Format the response "
                "in a well-structured manner suitable for article research."
            )
            
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error performing research: {str(e)}"


class GeminiFeedbackAnalysisToolInput(BaseModel):
    """Input schema for GeminiFeedbackAnalysisTool."""
    feedback_data: str = Field(..., description="The feedback data or metrics to analyze")
    article_topic: str = Field(..., description="The topic of the article the feedback relates to")

class GeminiFeedbackAnalysisTool(BaseTool):
    """Tool for analyzing feedback using Gemini AI."""
    
    name: str = "Gemini Feedback Analysis Tool"
    description: str = (
        "Uses Gemini 2.0 Flash to analyze feedback and performance metrics for articles. "
        "Provide the feedback data and article topic to get insights for improvement."
    )
    args_schema: Type[BaseModel] = GeminiFeedbackAnalysisToolInput

    def _run(self, feedback_data: str, article_topic: str) -> str:
        """Run the tool to analyze feedback using Gemini."""
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            prompt = (
                f"I need to analyze the following feedback and performance metrics for an article "
                f"on the topic of '{article_topic}':\n\n{feedback_data}\n\n"
                f"Please analyze this feedback and provide:\n"
                f"1. Key insights from the feedback\n"
                f"2. Patterns or trends in user responses\n"
                f"3. Specific areas for improvement\n"
                f"4. Actionable recommendations to enhance future articles on this or similar topics\n"
                f"5. Data points that should be updated in our knowledge base"
            )
            
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error analyzing feedback: {str(e)}"