#Copyright MicroLearn, Aryan Arora

#This program takes in a csv file

import os
import openai
import re

# Initialize an empty array to store the numbers
unformatted = []

# Open the file and read its content
with open('practice.txt', 'r') as f:
    content = f.read()
    content = content.replace('\n', '')

    # Split the content by the "|" delimiter
    items = re.split('\|', content)

    # Iterate over each item
    for item in items:
        # Try to convert the item to a number
        try:
            unformatted.append(item)
        except ValueError:
            # If not successful, skip the item
            pass

print(unformatted)


#AI Automation of unstructured data
openai.api_key = "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"

sample_input = ""
sample_output = ""
my_input = ""

sample_input = "\n\n5.1      The requesting entity has to set up an effective grievance handling mechanism and provide the same via multiple channels.   Yes Grievance handling mechanism was available, and channels used for customer grievances were via email, telephonic and SMS. Grievance handling screenshot"
sample_output = "'\n\n\\medskip\n\n\\noindent\\uuline{\\textbf{\\textit{Condition 5.1:}}} \n\n\\noindent The requesting entity has to set up an effective grievance handling mechanism and provide the same via multiple channels.\n\n\\medskip\n\n\\noindent\\uuline{\\textbf{\\textit{Assessor's Comments:}}} \n\n\\noindent Grievance handling mechanism was available, and channels used for customer grievances were via email, telephonic, and SMS.\n\n\\medskip\n\n\\noindent\\uuline{\\textbf{\\textit{Evidence Verified:}}} \n\n\\noindent \n\n\\begin{itemize} \n \\item Grievance handling screenshot\n\\end{itemize}\n\n\\medskip\n\n\\noindent\\uuline{\\textbf{\\textit{Conclusion:}}} The control is operating as intended.\n\n\\medskip\n\\medskip\n\n"

for curr in unformatted:
    my_input = curr

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= """I will give you sample unstructured data, and how that data should be structured in LaTeX. Your job is to structure the Input data afterwards. Include all relevant areas of consideration. INPUT:""" + sample_input + """ \n\n OUTPUT:""" + sample_output + """ INPUT: """ + my_input + """OUTPUT: """,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response['choices'][0]['text'])