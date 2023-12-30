from openai import *
import os   # used for local environmental variables
from wikipedia import *

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

# get user input
title = input("title of the Wikipedia page: ")

# get the wikipedia content
page = wikipedia.page(
    title=title,
    auto_suggest=False
)

# define prompt
prompt = "Write a summary of the following article: " + page.content[:10000]
messages = []
messages.append({"role": "user", "content": prompt})

try:
    # make an api
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo"
    )

    # print the response
    print(response.choices[0].message.content)

# authentication issue
except OpenAI.AuthenticationError:
    print("no valid token / authentication error")

except OpenAI.BadRequestError as e:
    print("invalid request, read the manual!")
    print(e)
