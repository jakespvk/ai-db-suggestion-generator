import sqlite3
from openai import OpenAI
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

client = OpenAI(
    api_key = os.getenv("openai_test_key")
)

def chat_with_gpt(input_prompt):
    completion = client.chat.completions.create(
            model='gpt-4o-mini', 
            messages=[
                {
                    "role": "user",
                    "content": input_prompt
                }
            ]
        )
    return completion.choices[0].message.content
    #print(dict(completion).get('usage'))
    #print(completion.model_dump_json(indent=2))

db = sqlite3.connect('mydatabase.db')

cursor = db.cursor()

"""cursor.execute('''CREATE TABLE IF NOT EXISTS people (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    desc TEXT)''')

cursor.execute('''INSERT INTO people (name, desc) VALUES (?, ?)''', ('John', 'likes planes'))
cursor.execute('''INSERT INTO people (name, desc) VALUES (?, ?)''', ('Jane', 'likes planes'))

db.commit()"""

cursor.execute('''SELECT * FROM people''')

str_db_stuff = "Please take this data, and return names of people with similar\
    backgrounds or interests in their description fields (the field just following\
    the name). Please only return if you would rate the similarity score above 70%: \n"
for row in cursor.fetchall():
    str_db_stuff = str_db_stuff + "\n" + "Name: " + row[1] + "Description: " + row[2]
    print(row)

db.close()

gpt_output = chat_with_gpt(str_db_stuff)

print(gpt_output)
