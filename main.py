from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
import os

os.environ["GOOGLE_API_KEY"]="AIzaSyCpqiYuGaEk-1NBdM_8W9zh31coti3oPZk"

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    markdown=True,
)
agent.print_response("hi", stream=True)
