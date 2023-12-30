from openai import *
import os   # used for local environmental variables

# Pass the api key
# Get the key from environmental variable. Instructions:
# 1 generate an API key from platform.openai.com
# 2. open "Show Advanced System Settings" in the windows search bar (swe: "Visa Avancerade Systeminställningar")
# 3. click Environmental Variables button (swe: Miljövariabler)
# 4. Under System Variables click new and set Variable name as OPENAI_API_KEY and your openAI API key as value
# if you want to call the variable something else, like TEST_KEY, then change the string literal below to
# Note: NEVER share your openAI API key with anyone. Treat it like you would treat your wallet or bankcard

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# define prompt
message = {"role": "user", "content": "Why is my website down?"}
messages = []
messages.append(message)

# make an api
response = client.chat.completions.create(
    messages=messages,
    model="gpt-3.5-turbo"
)

# print the response
print(response)