from Email_Service import EmailService
from Sms_Service import SmsService

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def notifyByEmail(self, message):
        self.email_service.send_email(message)

    def notifyBySms(self, message):
        self.sms_service.send_sms(message)

ns = NotificationService()
ns.notifyByEmail("Good morning")
ns.notifyBySms("hello")