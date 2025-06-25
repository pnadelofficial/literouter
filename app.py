import gradio as gr
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def route_llm_request(model, messages, api_key):
    # Verify the class API key
    if api_key != "your-class-key":
        return "Invalid API key"
    
    try:
        response = completion(
            model=model,
            messages=[{"role": "user", "content": messages}],

        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Simple interface
iface = gr.Interface(
    fn=route_llm_request,
    inputs=[
        gr.Dropdown(
            [
             "gpt-4.1", 
             # "gemini-2.0-flash"
             ]
            , label="Model"),
        gr.Textbox(label="Message"),
        gr.Textbox(label="API Key", type="password")
    ],
    outputs="text",
    api_name="chat" 
)

iface.launch()