import smtplib
import pandas as pd
from email.mime.text import MIMEText

# Load messages CSV
messages_df = pd.read_csv('messages.csv')

# Gmail credentials
gmail_user = 'naidugodasi751@gmail.com'              # Replace with your Gmail address
gmail_password = 'zgkgpvdkobnvdeqa'        # Replace with your 16-character App Password

# Connect to Gmail SMTP server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(gmail_user, gmail_password)

# Send emails one by one
for idx, row in messages_df.iterrows():
    to_email = row['email']
    message_text = row['message']

    msg = MIMEText(message_text)
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = "Thank you from Our Event Team"

    try:
        server.sendmail(gmail_user, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

server.quit()
