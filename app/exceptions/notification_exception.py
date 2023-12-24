class NotificationException(Exception):
    def __init__(self, errors):
        super().__init__(" | ".join(errors))
        self.errors = errors