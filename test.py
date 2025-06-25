from gradio_client import Client

client = Client("pnadel/literouter-hf-test")
result = client.predict(
		model="gpt-4.1",
		messages="Hello!!",
		api_key="your-class-key",
		api_name="/chat"
)
print(result)