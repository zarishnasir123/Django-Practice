from django.dispatch import Signal, receiver

notification = Signal()


@receiver(notification)
def show_notification(sender, **kwargs):
    print("------------------------")
    print("Notification: ")
    print(sender)
    print(f"{kwargs}") 