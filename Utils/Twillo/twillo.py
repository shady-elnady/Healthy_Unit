# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACb5dc0835e0f1c6028d0954c496ebaa38"
auth_token = "bd6b5b719b8479361c9469c4a48cf015"
verify_sid = "VAe6fbe41fa66523bda1c4cb03f63f93cf"
verified_number = "+201061656112"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)