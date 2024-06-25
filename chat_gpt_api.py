from openai import OpenAI

# Create an OpenAPI client using the key from our environment variable
client = OpenAI(
    api_key='sk-proj-cJF9AeiORlMyN8UEgwK2T3BlbkFJMiH9AqCNnJTjCmX6No1T',
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

curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-proj-cJF9AeiORlMyN8UEgwK2T3BlbkFJMiH9AqCNnJTjCmX6No1T" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
    }'
