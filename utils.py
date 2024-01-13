from openai import OpenAI
from keys import API_KEY

client = OpenAI(api_key=API_KEY)

def emailFormatting(description, template, name):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Your task is to craft a personalized email based on the provided template and specific details. The template includes placeholders that should be filled with the given information. Please replace the placeholders in the email template:\n\nTemplate: " + template + "\nRecipient Name: " + name + "\nDescription: " + description
        },
        {
            "role": "user",
            "content": ""
        }
    ],
    temperature=0.7,  # You can adjust temperature as needed
    max_tokens=200,   # Adjust max_tokens according to your email's expected length
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    generated_text = response.choices[0].message.content
    return generated_text
