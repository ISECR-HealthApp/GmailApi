from fastapi import FastAPI, status
import smtplib
import ssl
from email.message import EmailMessage

app = FastAPI(
    title="GmailApi",
    description="Api to send mmail by Gmail",
    version="1.0")


def email():
    # Define email sender and receiver
    email_sender = 'bproyecto23@gmail.com'
    email_password = 'ryzgkselrrwiyghc'
    email_receiver = 'bproyecto23@gmail.com'

    # Set the subject and body of the email
    subject = 'Evidencia API Gmail!'
    body = """
    Este es un correo de evidencia del API Gmail
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello():
    return {"message": f"GmailApi"}


@app.post("/submit", status_code=status.HTTP_200_OK)
async def sent_email():
    email()
    return {"message": "Success"}



