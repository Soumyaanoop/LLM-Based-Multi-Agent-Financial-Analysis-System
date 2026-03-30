import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# Create Agents (same)
# -------------------------

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["Use tables to display the data"],
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["All financial queries go to Finance AI Agent using YFinanceTools",
                  "All web search queries go to Web Search Agent using DuckDuckGo",
                  "Only call YFinanceTools for financial data queries (stock price, analyst recommendations, company news)",
                  "Only call DuckDuckGo for general web search or news not available from YFinanceTools",
                  "Always include sources", 
                  "Use tables to display the data"],
    markdown=True
)

# -------------------------
# Streamlit UI
# -------------------------

st.set_page_config(page_title="Financial AI Agent", layout="wide")

st.title("📈 Financial AI Agent")
st.write("Get stock insights, analyst recommendations, and latest news")

# User input
company = st.text_input("Enter Company Name (e.g., Tesla, Apple, Microsoft)")

# Button
if st.button("Analyze"):

    if company.strip() == "":
        st.warning("Please enter a company name.")
    else:
        query = f"Summarize analyst recommendations and share the latest news for {company}"

        st.info(f"Analyzing {company}...")

        # Streaming output
        response_container = st.empty()
        output = ""

        try:
            response_stream = multi_ai_agent.run(query, stream=True)

            for chunk in response_stream:
                if hasattr(chunk, "content"):
                    output += chunk.content
                else:
                    output += str(chunk)

                response_container.markdown(output)

        except Exception as e:
            st.error(f"Error: {e}")