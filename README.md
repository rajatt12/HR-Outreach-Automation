# 🚀 HR Outreach Automation Pipeline

An automated email outreach system that extracts HR contact information from PDF files and sends personalized emails with resume attachments using Python.

This project demonstrates automation pipelines, data extraction, email automation, and workflow orchestration suitable for real-world outreach automation and portfolio projects.

---

## 📌 Project Overview

This automation pipeline performs the following tasks:

* Extract HR contact data from structured PDF files
* Clean and process extracted data
* Generate personalized email content using templates
* Automatically attach resume files
* Send emails using Gmail SMTP
* Log sending status for tracking and debugging

---

## 🧠 Workflow Architecture

```
PDF HR Contacts
      ↓
PDF Parsing (pdfplumber)
      ↓
Data Processing (pandas)
      ↓
Email Personalization (template engine)
      ↓
SMTP Email Automation
      ↓
Logging & Tracking
```

---

## ⚙️ Tech Stack

* Python
* Pandas
* pdfplumber
* smtplib (SMTP Email Automation)
* email.mime (Email attachments and formatting)

---

## 📁 Project Structure

```
HR-Outreach-Automation/
│
├── attachments/
│   └── resume.pdf
│
├── templates/
│   └── email_template.txt
│
├── extract.py        # Extract data from PDF
├── mailer.py         # Email sender with resume attachment
├── main.py           # Automation pipeline controller
│
├── logs/
│   └── send_log.csv
│
└── README.md
```

---

## 🚀 Installation

Clone repository:

```
git clone https://github.com/rajatt12/HR-Outreach-Automation.git
cd HR-Outreach-Automation
```

Install dependencies:

```
pip install pandas pdfplumber
```

---

## 🔐 Gmail Setup (IMPORTANT)

This project uses Gmail SMTP for sending emails.

Steps:

1. Enable 2-Step Verification in your Google Account
2. Generate a Gmail App Password
3. Replace credentials inside `mailer.py`:

```
FROM_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
```

Do NOT use your normal Gmail password.

---

## 🧪 Running the Pipeline

Run the main script:

```
python main.py
```

The system will:

* Extract contacts from PDF
* Personalize email content
* Attach resume automatically
* Send emails via SMTP
* Save logs

---

## 📊 Logging

Email status is stored inside:

```
logs/send_log.csv
```

Includes:

* Email address
* Status (SUCCESS / ERROR)
* Timestamp

---

## ⚠️ Safety Notes

* Always test with a small batch before sending bulk emails
* Gmail has daily sending limits
* Add delays between emails to avoid spam blocking
* Verify resume file path before running

---

## 🎯 Future Improvements

* Async email sending
* AI-generated personalized outreach messages
* Spam-safe scheduling system
* Email open/click tracking
* Automated follow-up emails


Feel free to fork, improve, and experiment with automation workflows.

If you found this helpful, consider starring the repository.
