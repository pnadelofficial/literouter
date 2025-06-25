import gradio as gr
from litellm import completion
import os
import yaml

# Load configuration from YAML file
config_path = "config.yaml"
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file {config_path} not found.") 
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

os.environ["OPENAI_API_KEY"] = config.get("model_list", "")[0].get("litellm_params", "").get("api_key", "")
# os.environ["GEMINI_API_KEY"] = config.get("model_list", "")[1].get("litellm_params", "").get("api_key", "")

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
    outputs="text"
)

iface.launch()