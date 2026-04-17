from fastapi import FastAPI, Request
from pydantic import BaseModel
from ai_services import get_ai_response
from slack_services import handle_mentions

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

# 1. Health Check
@app.get("/")
def health_check():
    return {"status": "API is running"}

# 2. Direct API Testing (Isse aap Postman ya Swagger se test kar sakte hain)
@app.post("/generate")
async def generate_text(request: PromptRequest):
    answer = get_ai_response(request.prompt)
    return {"result": answer}

# 3. Slack Events (Slack se message aane par ye chalega)
@app.post("/slack/events")
async def slack_events(request: Request):
    data = await request.json()
    
    # Slack Verification (Sirf setup ke waqt)
    if "challenge" in data:
        return {"challenge": data["challenge"]}
    
    # Slack Event Handling
    if "event" in data:
        event = data["event"]
        # Agar bot ko mention kiya jaye ya koi message aaye
        if event.get("type") == "app_mention":
            user_text = event.get("text")
            channel = event.get("channel")
            
            # AI se jawab lo
            ai_answer = get_ai_response(user_text)
            if ai_answer:
            # Slack par jawab bhejo
                handle_mentions(channel, ai_answer)
            
    return {"status": "ok"}