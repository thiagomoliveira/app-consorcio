from data_import.import_notification import import_notifications_from_excel
from data_operations.notification_data_operations import *
from datetime import datetime

class NotificationController:
    def __init__(self, data_path):
        self.data_path = data_path
        self.valid_notifications, self.invalid_notifications = import_notifications_from_excel(self.data_path)

    def get_initial_data(self):
        current_date_str = datetime.now().strftime('%d/%m/%Y')
        filtered_notifications = filter_notifications(
            self.valid_notifications, start_date='01/01/2010', end_date=current_date_str)
        return group_notifications_by_type_and_date(filtered_notifications)

    def get_aggregated_data_by_type_and_date(self, start_date, end_date, states):
        filtered_notifications = filter_notifications(
            self.valid_notifications, start_date=start_date, end_date=end_date, states=states)
        return group_notifications_by_type_and_date(filtered_notifications)
    
    def get_aggregated_data_by_state(self, start_date=None, end_date=None):
        filtered_notifications = filter_notifications(
            self.valid_notifications, start_date=start_date, end_date=end_date)
        return group_notifications_by_state(filtered_notifications)
