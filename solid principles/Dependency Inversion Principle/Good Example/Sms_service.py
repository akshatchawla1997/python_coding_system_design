from Notification_channel import NotificationChannel

class SmsService(NotificationChannel):
    def send(self, message):
        print(f"sending SMS {message}")