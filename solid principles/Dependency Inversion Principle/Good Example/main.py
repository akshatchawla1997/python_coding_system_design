from NotificationService import NotificationService
from Email_service import EmailService
from Sms_service import SmsService

sms = SmsService()
email = EmailService()
ns = NotificationService(sms)

ns.notify("Hey")

# ns = NotificationService(email)