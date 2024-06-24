from openai import OpenAI

# Create an OpenAPI client using the key from our environment variable
client = OpenAI(
    api_key=my_api_key,
)

# Specify the model to use and the messages to send
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a university instructor and can explain programming concepts clearly in a few words."},
        {"role": "user", "content": "What are the advantages of pair programming?"}
    ]
)
print(completion.choices[0].message.content) 
