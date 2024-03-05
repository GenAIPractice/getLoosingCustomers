# Import necessary libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send a custom email based on context
def send_custom_email():
    # Example of sending a custom email
    subject = "Custom Email Subject"
    message = "This is a custom email message based on the context."
    recipient_email = "sangram97@gmail.com"

    # Call the function to send the custom email


    # Set up the SMTP server details for a free SMTP server like Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'genaipractice2024@gmail.com'  # Your Gmail address
    smtp_password = 'fpzkzjipgaiufkiq'  # Your Gmail password

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = "sangram97@gmail.com"
    msg['Subject'] = 'Welcome to GenAI Bank'

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(smtp_username, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
