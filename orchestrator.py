from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.tools import BaseTool

from agents.code_review_agent import code_review_agent
from agents.email_analyzer_agent import analyze_email
from agents.calendar_agent import schedule_meeting
from agents.audio_transcriber_agent import transcribe_audio
from agents.summary_agent import generate_summary

from prompts import (
    CODE_REVIEW_PROMPT,
    EMAIL_ANALYZER_PROMPT,
    AUDIO_TRANSCRIBER_PROMPT,
    CALENDAR_AGENT_PROMPT,
    SUMMARY_PROMPT
)

# Tools
class CodeReviewTool(BaseTool):
    name = "code_review_tool"
    description = CODE_REVIEW_PROMPT
    def _run(self, input_text: str):
        if "http" in input_text:
            return str(code_review_agent(repo_url=input_text))
        else:
            return str(code_review_agent(file_path=input_text))

class EmailAnalyzerTool(BaseTool):
    name = "email_analyzer_tool"
    description = EMAIL_ANALYZER_PROMPT
    def _run(self, text: str):
        return str(analyze_email(text))

class CalendarTool(BaseTool):
    name = "calendar_scheduler_tool"
    description = CALENDAR_AGENT_PROMPT
    def _run(self, details: str):
        return schedule_meeting(["Alice", "Bob"], details)

class AudioTool(BaseTool):
    name = "audio_transcriber_tool"
    description = AUDIO_TRANSCRIBER_PROMPT
    def _run(self, audio_file: str):
        return transcribe_audio(audio_file)

class SummaryTool(BaseTool):
    name = "summary_tool"
    description = SUMMARY_PROMPT
    def _run(self, text: str):
        return generate_summary(text)

def get_orchestrator():
    tools = [CodeReviewTool(), EmailAnalyzerTool(), CalendarTool(), AudioTool(), SummaryTool()]
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    llm = OpenAI(temperature=0)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory)
    return agent
