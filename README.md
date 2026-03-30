# LLM-Based-Multi-Agent-Financial-Analysis-System

Built an Multi-Agent AI system using LLMs (Groq LLaMA 3) and the phi AI framework integrating specialized tools such as YFinance for financial data and DuckDuckGo for web search to retrieve stock prices, analyst recommendations and real-time company news. Designed a multi-agent architecture to coordinate specialized agents for financial analysis and information retrieval.
The system has been deployed as a Streamlit web application, allowing users to interactively query company data and receive real time, formatted AI-generated responses.



# Features
 
 Web Search Agent – Retrieves real-time information from the web
 
 Finance Agent – Fetches stock data, analyst recommendations, and company news
 
 Multi-Agent Orchestration – Automatically routes queries to the right agent
 
 Structured Outputs – Tables for financial data
 
 Source Attribution – Always includes references
 
 Streaming Support – Real-time response generation


# Architecture
           
           User Query
                ↓
        Multi AI Agent (Controller)
           ↙           ↘
 Web Search Agent   Finance Agent
   (DuckDuckGo)     (YFinanceTools)

# How It Works

The system consists of three agents:

 ## Web Search Agent

Uses DuckDuckGo

Handles general queries and news

Always includes sources

## Finance AI Agent

Uses YFinanceTools

Handles Stock prices, Analyst recommendations, Company fundamentals, Financial news

Outputs data in table format

## Multi AI Agent (Coordinator)

Routes queries intelligently:

Financial queries → Finance Agent

General queries → Web Search Agent

Enforces tool usage rules

Combines responses into a final answer


# Installation

1. Clone the repository

git clone https://github.com/username/multi-agent-ai.git
cd multi-agent-ai

2. Install dependencies
pip install -r requirements.txt

3. Setup environment variables

Create a .env file in the root directory:

GROQ_API_KEY= my_api_key_here


# Code Overview

## Import Dependencies



Groq → Large Language Model (LLM) provider

YFinanceTools → Fetches stock & financial data

DuckDuckGo → Web search tool

dotenv → Loads environment variables (e.g., API keys)


## Load Environment Variables






## Create Web Search Agent

Responsibilities:

Performs general web searches

Retrieves latest news & information

Always includes sources







## Create Finance Agent

Responsibilities:

Fetches stock prices

Provides analyst recommendations

Retrieves company fundamentals

Shows financial news

Outputs data in table format






## Create Multi-Agent

What it does:

Acts as a controller/orchestrator

Routes queries to the correct agent:
                                   Finance → finance_agent
                                   
                                   General search → web_search_agent
Ensures:

Proper tool usage, Structured output and Source attribution














What happens:

The query is analyzed and routed to Finance AI Agent

Pulls analyst recommendations and latest company news

Outputs :
         Analyst recommendation summary (Buy/Hold/Sell)
         
         Stock fundamentals (Revenue, Market Cap, etc.)
         
         Latest company news
         
         Sources for verification






# Streamlit User Interface









Run the Streamlit app

streamlit run app.py


Interact with the AI

Enter a company name (e.g., Tesla, Apple, Microsoft)

Click Analyze

View:

Analyst recommendation summary

Stock fundamentals

Latest news

Sources for verification




# OUTPUT












# Configuration

Change the Groq model ID to use different LLMs

Modify the tools or instructions for agents

Customize the Streamlit layout or components


# Notes

Ensure the .env file contains your Groq API key

Internet connection is required for all tools to function

Proper error handling included for streaming output


