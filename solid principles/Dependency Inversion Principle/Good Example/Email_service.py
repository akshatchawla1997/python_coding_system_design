from Notification_channel import NotificationChannel

class EmailService(NotificationChannel):
    def send(self, message):
        print(f"sending email {message}")