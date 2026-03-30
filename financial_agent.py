from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv() 

# create web search agent

web_search_agent= Agent(
    name=" Web Search Agent",
    role = "Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_call=True,
    markdown=True,
)

#create financial agent

finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[ YFinanceTools(stock_price=True, analyst_recommendations=True, 
                           stock_fundamentals=True, company_news=True)
    ],
    instructions=["Use tables to display the data"],
    show_tool_call=True,
    markdown=True, 
)


#create Multi model ai agent
multi_ai_agent= Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["All financial queries go to Finance AI Agent using YFinanceTools",
                  "All web search queries go to Web Search Agent using DuckDuckGo",
                  "Only call YFinanceTools for financial data queries (stock price, analyst recommendations, company news)",
                  "Only call DuckDuckGo for general web search or news not available from YFinanceTools",
                  "Always include sources",
                  "use table to display the data"
    ],
    show_tool_call=True,
    markdown=True
)

#multi_ai_agent.print_response("summerize analyst recommendation and share the latest newsfor Tesla",stream=True)

multi_ai_agent.print_response(f"Summarize analyst recommendations and share the latest news for {company}")