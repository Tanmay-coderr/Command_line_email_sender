import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def send_email(subject, body, to_email, sender_email, sender_password, attachment_path=None):
    # SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach file if attachment_path is provided
    if attachment_path:
        try:
            filename = os.path.basename(attachment_path)
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(part)
        except Exception as e:
            print(f"Error attaching file: {str(e)}")
            return

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


# Example Usage
if __name__ == "__main__":
    # Get sender email and password from the user
    sender_email = input("Enter your Gmail address: ")
    sender_password = input("Enter your Gmail app password: ")  # Securely input password

    # Get recipient email, subject, and body
    to_email = input("Enter recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")

    # Optionally, ask for an attachment path
    attachment_path = input("Enter the path of the attachment (or press Enter to skip): ")
    if not attachment_path:
        attachment_path = None  # No attachment

    # Send the email
    send_email(subject, body, to_email, sender_email, sender_password, attachment_path)

