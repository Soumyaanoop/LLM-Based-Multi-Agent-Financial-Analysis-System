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
           
           
           User Input
              ↓
      Multi AI Agent (Coordinator)
         ↙             ↘
Web Search Agent     Finance Agent
   (DuckDuckGo)      (YFinanceTools)


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


![1st_fin](https://github.com/user-attachments/assets/38b9bbc4-d573-48ca-ab39-0c70ab4d2f33)



Groq → Large Language Model (LLM) provider

YFinanceTools → Fetches stock & financial data

DuckDuckGo → Web search tool

dotenv → Loads environment variables (e.g., API keys)


## Load Environment Variables


![2nd_fin](https://github.com/user-attachments/assets/bf795844-fe0d-4645-ba4b-6ba9de49c6dc)



## Create Web Search Agent

Responsibilities:

Performs general web searches

Retrieves latest news & information

Always includes sources


![3rd_fin](https://github.com/user-attachments/assets/f70a87af-9c70-48bf-b1fc-670fe3409d36)




## Create Finance Agent

Responsibilities:

Fetches stock prices

Provides analyst recommendations

Retrieves company fundamentals

Shows financial news

Outputs data in table format


![4th_fin](https://github.com/user-attachments/assets/7b7cecfb-b04d-4759-b6bd-313f7dee1551)




## Create Multi-Agent

What it does:

Acts as a controller/orchestrator

Routes queries to the correct agent:
                                   Finance -> finance_agent
                                   General Search -> web_search_agent

Ensures:

Proper tool usage, Structured output and Source attribution.



![5th_fin](https://github.com/user-attachments/assets/27a654c2-709d-4cf5-9f02-aae3ae094da7)








![6th_fin](https://github.com/user-attachments/assets/e9d9667a-6111-4191-aacb-5b8e1109fbc7)




What happens:

The query is analyzed and routed to Finance AI Agent

Pulls analyst recommendations and latest company news

Outputs :
         Analyst recommendation summary (Buy/Hold/Sell).
         
         Stock Fundamentals (Revenue, Market cap, etc).

         Latest Company News.

         Sources for verification







# Streamlit User Interface



![9th_fin](https://github.com/user-attachments/assets/bd229e85-c502-423b-9739-b1ccbb7a9ab9)







Run the Streamlit app

streamlit run app.py


Interact with the AI

Enter a company name (e.g., Tesla, Apple, Microsoft)

Click Analyze


View:

     Analyst recommendation summary, Stock Fundamentals, Latest News and Sources for verification

     

    

# OUTPUT




![fin_output](https://github.com/user-attachments/assets/eace831a-166c-41dd-b049-18ee6091ccc2)









![fin_output1](https://github.com/user-attachments/assets/e66999c2-677f-4d92-a7ae-e00f474e1f3d)







# Configuration

Change the Groq model ID to use different LLMs

Modify the tools or instructions for agents

Customize the Streamlit layout or components


# Notes

Ensure the .env file contains your Groq API key

Internet connection is required for all tools to function

Proper error handling included for streaming output


