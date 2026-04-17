from huggingface_hub import InferenceClient
from config import HF_TOKEN

# Free Inference API client
client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN)

def get_ai_response(prompt: str):
    try:
        # AI ko prompt bhejna
        response = client.text_generation(
            prompt, 
            max_new_tokens=200, 
            temperature=0.7
        )
        return response
    except Exception as e:
        return f"Error: AI service is busy right now. ({str(e)})"