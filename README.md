# Command-Line Email Sender

This is a Python script that allows you to send emails using Gmail's SMTP server. You can customize the subject, body, and recipient email address. The script also supports attachments, though it's currently set up to send emails without attachments.

## Prerequisites

- Python 3.x
- Required libraries: `smtplib`, `email`
- A Gmail account with **2-Step Verification** enabled.

## How to Generate an App Password for Gmail

To send emails using your Gmail account from this script, you need to create an app-specific password. Follow these steps:


1.Open the link : https://myaccount.google.com/apppasswords<br>
2.Sign in to your google account.<br>
3.Enter a name for your app password.<br>
4.Copy the generated password and save it for later use.<br>

## How to run the Email sender

To run the email sender, follow these steps:


1.Open the `script.py` file and modify the following:<br>
  ->`test_sender12@gmail.com` to your email id.<br>
  ->`your_app_password_here` to your app password.<br>
  ->`test123@gmail.com` to  recipient's email address.<br>
  ->`C:\Users\user_name\path\directory\demofile` to your file path.<br>
2.Change the email subject and body acoording to your preference.<br>
3.Run the script in the terminal.
