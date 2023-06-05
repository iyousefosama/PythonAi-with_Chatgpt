import openai

openai.api_key = "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"
Type = "Virtual assistant called jarvis"

MAX_TOKENS = 200
messages = [{"role": "system", "content": Type}]

print("Send a message.\n")

while True:
    user_input = input()

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
