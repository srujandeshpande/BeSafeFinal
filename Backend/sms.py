# Download the helper library from https://www.twilio.com/docs/python/installfrom twilio.rest import Client# Your Account Sid and Auth Token from twilio.com/console
account_sid = ‘AC74e46641376257d59ef0f0771666f64b’
auth_token = ‘7db4e3e9e1e1bad9c7ef957b6d6215fd’
client = Client(account_sid, auth_token)message = client.messages.create(
 body=’DANGER!’,
 from_=’[+][1][2563690733]',
 to=’[+][9][19740621505]'
 )
print(message.sid)
