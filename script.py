import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(subject, body, to_email, attachment_path=None):
    # SMTP server details
    smtp_server = "smtp.gmail.com"  # For Gmail, change accordingly for other services
    smtp_port = 587
    sender_email = "test_sender12@gmail.com" # Enter your email here
    sender_password = "your_app_password_here" # If two step verification is on then enter your app password(to know how to create an app password read the readme file)

    # Create the email object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach file if provided
    if attachment_path:
        filename = os.path.basename(attachment_path)
        attachment = open(attachment_path, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {filename}')

        msg.attach(part)

    try:
        # Connect to SMTP server and send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")


# Usage example
if __name__ == "__main__":
    subject = "Test Email"
    body = "This is a test email with an attachment."
    to_email = "test123@gmail.com"
    attachment_path = r"C:\Users\user_name\path\directory\demofile" # Set to None if you don't want to send an attachment
    
    send_email(subject, body, to_email, attachment_path)
