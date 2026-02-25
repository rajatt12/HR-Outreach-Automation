from extract import extract_pdf
from mailer import send_email
import os
import pandas as pd
from datetime import datetime

df = extract_pdf("G:\\30 Days ML Projects\\HR-Outreach-Automation\\data\\HR Contacts.pdf")

logs = []

df = df.sample(n=10, random_state=42).reset_index(drop=True)   

for index,row in df.iterrows():

    name = row["Name"]
    email = row["Email"]
    company = row["Company"]

    status = send_email(email, name, company)

    logs.append({
        "email": email,
        "status": status,
        "time": datetime.now()
    })

log_df = pd.DataFrame(logs)

os.makedirs("logs", exist_ok=True)
log_df.to_csv("logs/send_log.csv", index=False)

print("DONE")