import pdfplumber
import pandas as pd
def extract_pdf(pdf_path="G:\\30 Days ML Projects\\HR-Outreach-Automation\\data\\HR Contacts.pdf"):

    rows = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()

            for table in tables:
                for row in table:
                    rows.append(row)

    df = pd.DataFrame(rows)

    df.columns = ["SNo","Name","Email","Title","Company"]

    return df



df = extract_pdf()
print(df.head())

print(df["Company"].head(10))
print("Emails count:", len(df))
print("Unique Emails count:", len(df["Email"].unique()))

def clean_data(df):

    df = df[df["Email"] != "Email"]

    df = df.dropna()
    df = df.drop_duplicates(subset=["Email"])

    return df