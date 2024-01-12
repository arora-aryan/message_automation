#Copyright MicroLearn, Aryan Arora

#This program takes in a csv file

import os
from openai import OpenAI
from keys import API_KEY
import re

client = OpenAI(API_KEY)

# Initialize an empty array to store the numbers
unformatted = []

# Open the file and read its content
with open('input.txt', 'r') as f:
    content = f.read()
    content = content.replace('\n', '')

    # Split the content by the "," delimiter
    items = re.split(',', content)
   
    # Iterate over each item
    for item in items:
        # Try to convert the item to a number
        try:
            unformatted.append(item)
        except ValueError:
            # If not successful, skip the item
            pass

print(unformatted)


sample_input = ""
my_input = ""

for curr in unformatted:
    my_input = curr

    print(my_input)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "Your task is to craft a personalized email based on the provided template and specific details. The template includes placeholders that should be filled with the given information. If any detail necessary for a placeholder is not provided, adjust the template by removing or smoothly rephrasing the relevant part, ensuring the email remains coherent and professional.\n\nThe following is the template:\n\nAnd this is the data to fill in the template: "
        },
        {
        "role": "user",
        "content": ""
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response.choices[0].text)