from simplegmail import Gmail
from simplegmail.query import construct_query
import csv
import pandas as pd   

# Initialize the Gmail client
gmail = Gmail()

# Define the query to filter messages in the "Updates" category
query = construct_query({'newer_than': (6, "month"), 'label': 'UPDATES'})


# Fetch messages matching the query
messages = gmail.get_messages(query=query)

df = pd.DataFrame([
    {
        'From': message.sender,
        'Subject': message.subject,
        'Read': 'UNREAD' not in message.label_ids,
        'Body': message.plain,
        'Date': message.date
    } for message in messages
])

# Save to csv
df.to_csv('data/gmail_data-6-months-rag.csv', index=False)

# print(df.head(50))
