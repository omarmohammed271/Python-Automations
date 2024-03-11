# Importing the Required Library
from twilio.rest import Client

# Configuring Twilio Credentials and Logging in
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# Sending an SMS
message = client.messages.create(
    body='Hello from Python!',
    from_='+1234567890',  # Your Twilio phone number
    to='+9876543210'  # Recipient's phone number
)

# Verifying if the message is sent or not
print(f"SMS sent successfully. Message ID: {message.sid}")