import os
import openai
import config

PrivateKey = config.api_key or os.environ.get('OPENAI_API_KEY')

if not PrivateKey:
    raise ValueError("OpenAI API key not found in the environment variable.\nCreate an config.py file with "
                     "api_key=YOUR_KEY\n\n")
else:
    print(f"Logged with key \"{PrivateKey}\"\n\n")

openai.api_key = PrivateKey
Type = "Virtual assistant called jarvis"

MAX_TOKENS = 200
messages = [{"role": "system", "content": Type}]

print("Send a message.\n")

while True:
    user_input = str(input())

    messages.append({"role": "user", "content": user_input})

    prompt = "\n".join([f"{message['role']}: {message['content']}" for message in messages])
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=MAX_TOKENS
    )
    ResTxt = response.choices[0].text.strip()

    if response.choices[0].finish_reason == "length":
        ResTxt = ResTxt[:MAX_TOKENS]

    messages.append({"role": "assistant", "content": ResTxt})

    print(ResTxt)
