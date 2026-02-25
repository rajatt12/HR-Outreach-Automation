import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

FROM_EMAIL = ""
APP_PASSWORD = ""

RESUME_PATH = "G:\\30 Days ML Projects\\HR-Outreach-Automation\\attachments\\CVNew.pdf"

def send_email(to_email, name, company):

    with open("G:\\30 Days ML Projects\\HR-Outreach-Automation\\templates\\email_template.txt", "r") as f:
        template = f.read()

    body = template.format(name=name, company=company)

    msg = MIMEMultipart()
    msg["Subject"] = "Opportunity Inquiry"
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email

    msg.attach(MIMEText(body, "plain"))

    try:
        with open(RESUME_PATH, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename=Rajatveer_Singh_Resume.pdf"
            )
            msg.attach(part)
    except FileNotFoundError:
        return "Resume file not found"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)   # Gmail SMTP server and port
        server.starttls()                              # Start TLS encryption
        server.login(FROM_EMAIL, APP_PASSWORD)         # Login using app password
        server.send_message(msg)                       # Send the email
        server.quit()                                  # Quit SMTP session
        return "SUCCESS"

    except Exception as e:

        return str(e)
