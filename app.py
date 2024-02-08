import os
import openai
import gradio as gr
import logging

import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load API key from environment or config file
api_key = os.getenv('OPENAI_API_KEY') or config.api_key
if not api_key:
    raise ValueError("OpenAI API key not found. Set it in your environment variables.")

# Configure OpenAI
openai.api_key = api_key
model_name = "gpt-3.5-turbo-instruct"
max_tokens = 200


# Main function to handle user input
def start_input(message):
    try:
        user_input = str(message)
        messages.append({"role": "user", "content": user_input})
        prompt = "\n".join([message['content'] for message in messages])

        response = openai.Completion.create(
            model=model_name,
            prompt=prompt,
            temperature=0.5,
            max_tokens=max_tokens
        )

        res_txt = response.choices[0].text.strip()

        if response.choices[0].finish_reason == "length":
            res_txt = res_txt[:max_tokens]

        messages.append({"role": "assistant", "content": res_txt})
        return str(res_txt)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return "An error occurred. Please try again later."


# Initialize Gradio interface
interface = gr.Interface(
    fn=start_input,
    inputs="text",
    outputs="text",
    title="Virtual Assistant - Jarvis"
)

# Define system message
system_message = "Virtual assistant called Jarvis"

# Initialize messages list with the system message
messages = [{"role": "system", "content": system_message}]

if __name__ == "__main__":
    logger.info(f"Logged in with API key: {api_key}")
    interface.launch()
