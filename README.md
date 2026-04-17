# AI-Slack-Connect - MyDevBot
---
## Project Description
* This project is a real-time AI-powered Slack bot designed to automate workspace interactions. It leverages FastAPI for high-performance request handling and the Slack SDK to communicate seamlessly within Slack channels.
---

## Objective
### The main goal is to build an intelligent assistant that:
* Monitors Slack channel activities in real-time.
* Responds to user queries (e.g., "How are you") automatically.
* Provides a scalable foundation for adding AI/LLM capabilities later.
---

## Core Components
### The project is structured into modular services:
* app.py: The main FastAPI entry point that handles Slack Event API requests.
* slack_services.py: Contains logic for sending messages and interacting with Slack WebClient.
* ai_services.py: Dedicated space for future AI/Machine Learning logic integration.
---

##  Functional Requirements
### 1. Slack Event Integration
* URL Verification: Handles Slack's challenge request to verify the server.
* Event Filtering: Specifically listens for message events while ignoring bot-generated messages to prevent infinite loops.
### 2. Message Processing
* Text Normalization: Converts incoming text to lowercase for consistent keyword matching.
* Conditional Logic: Triggers specific responses based on keywords like "hello" or "how are you".
### 3. Connection & Security
* ngrok Tunneling: Creates a secure public URL for Slack to reach the local development server.
* Token Authentication: Uses SLACK_BOT_TOKEN for secure API authorization.
---

## Technical Workflow
### Event Handling Logic
* Step   Action          Description
1      Request         Slack sends a POST request with message data.
2      Validation       Server checks if the message is from a human user.
3       Logic            Code matches keywords (e.g., "How are you").
4       Response          Bot sends a reply via chat.postMessage API.
---
## How to run
### * Install Dependencies: pip install fastapi uvicorn slack_sdk python-dotenv
### * Setup ngrok: ngrok http 8000
### * Run Application: uvicorn app:app --reload
### * Configure Slack: Update the Event Subscriptions URL in Slack Dashboard with your ngrok address.
---
## Author
### Palak Rathor
---
