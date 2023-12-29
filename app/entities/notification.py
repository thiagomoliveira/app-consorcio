from utils.notification_validations import *
from utils.type_conversion import convert_date

class Notification:
    def __init__(self, group, quota, send_date, return_date, notification_return_type, office, state, registry_office, name, contract, justification):
        # Initialize all attributes
        self._group = group
        self._quota = quota
        self._send_date = send_date
        self._return_date = return_date
        self._notification_return_type = notification_return_type
        self._office = office
        self._state = state
        self._registry_office = registry_office
        self._name = name
        self._contract = contract
        self._justification = justification
        
        # Perform validation
        self.is_valid, self.errors = validate_notification_data(
            group, quota, send_date, return_date, notification_return_type, office, state, registry_office, name, contract, justification)
        
        # Convert the dates if the notification is valid
        if self.is_valid:
            self._send_date = convert_date(send_date)
            self._return_date = convert_date(return_date)
        else:
            # Set attributes for invalid notifications
            self._send_date = send_date
            self._return_date = return_date

    # Getters and Setters with validation
    def get_group(self):
        return self._group

    def set_group(self, group):
        self._group = validate_numeric(group)

    def get_quota(self):
        return self._quota

    def set_quota(self, quota):
        self._quota = validate_numeric(quota)

    def get_send_date(self):
        return self._send_date

    def set_send_date(self, send_date):
        self._send_date = validate_date(send_date)

    def get_return_date(self):
        return self._return_date

    def set_return_date(self, return_date):
        self._return_date = validate_date(return_date)

    def get_notification_return_type(self):
        return self._notification_return_type

    def set_notification_return_type(self, notification_return_type):
        self._notification_return_type = validate_not_empty(notification_return_type, "Notification return type")

    def get_office(self):
        return self._office

    def set_office(self, office):
        self._office = validate_not_empty(office, "Office")

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = validate_state(state)

    def get_registry_office(self):
        return self._registry_office

    def set_registry_office(self, registry_office):
        self._registry_office = validate_not_empty(registry_office, "Registry office")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = validate_not_empty(name, "Name")

    def get_contract(self):
        return self._contract

    def set_contract(self, contract):
        self._contract = validate_numeric(contract)

    def get_justification(self):
        return self._justification

    def set_justification(self, justification):
        self._justification = validate_not_empty(justification, "Justification")

    def revalidate(self):
        # Reapply the validation logic
        self.is_valid, self.errors = validate_notification_data(
            self._group, self._quota, self._send_date, self._return_date, self._notification_return_type,
            self._office, self._state, self._registry_office, self._name, self._contract, self._justification
        )

        # Convert the dates if the notification is valid
        if self.is_valid:
            self._send_date = convert_date(self._send_date)
            self._return_date = convert_date(self._return_date)
            return {"status": "success", "message": "Notification successfully validated."}
        else:
            # Return information about the validation errors
            return {"status": "error", "message": "Validation errors found.", "errors": self.errors}

    # Magic methods
    def __eq__(self, other):
        if not isinstance(other, Notification):
            return False
        return (self._group, self._quota) == (other._group, other._quota)

    def __hash__(self):
        return hash((self._group, self._quota))

    def __str__(self):
        return (f"Notification(group={self._group}, quota={self._quota}, send_date={self._send_date}, "
                f"return_date={self._return_date}, notification_return_type={self._notification_return_type}, "
                f"office={self._office}, state={self._state}, registry_office={self._registry_office}, "
                f"name={self._name}, contract={self._contract}, justification={self._justification}, "
                f"is_valid={self.is_valid}, errors={self.errors})")
