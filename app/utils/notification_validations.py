from datetime import datetime
import pandas as pd

def validate_numeric(value, field_name):
    """
    Validates if the given numeric value is not empty, null, or non-digit.
    """
    if not value or pd.isna(value):
        raise ValueError(f"{field_name} cannot be empty or null")
    elif not str(value).isdigit():
        raise ValueError(f"Invalid {field_name}")
    return value


def validate_state(state):
    """
    Validates if the given state is not empty, null, and is a valid Brazilian state.
    """
    brazilian_states = [
        "AC", "AL", "AP", "AM", "BA",
        "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB",
        "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP",
        "SE", "TO"
    ]
    if not state or pd.isna(state):
        raise ValueError("State cannot be empty or null")
    elif state.upper() not in brazilian_states:
        raise ValueError("Invalid state")
    return state.upper()


def validate_date(date):
    """
    Validates if the given date is not empty or null and is in the correct format (dd/mm/yyyy).
    """
    if not date or pd.isna(date):
        raise ValueError("Date cannot be empty or null")
    try:
        return datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Invalid date")

def validate_not_empty(value, field_name):
    """
    Validates if the given value is not empty or null.
    """
    if not value or pd.isna(value):
        raise ValueError(f"{field_name} is empty or null")
    return value

def validate_notification_data(group, quota, send_date, return_date, notification_return_type, office, state, registry_office, name, contract, justification):
    """
    Validates the data for a notification. Returns a boolean indicating if the data is valid and a list of error fields if any.
    """
    errors = []

    try:
        validate_numeric(group, "Group")
    except ValueError:
        errors.append("Group")

    try:
        validate_numeric(quota, "Quota")

    except ValueError:
        errors.append("Quota")

    try:
        validate_numeric(contract, "Contract")
    except ValueError:
        errors.append("Contract")

    try:
        validate_date(send_date)
    except ValueError:
        errors.append("Send date")

    try:
        validate_date(return_date)
    except ValueError:
        errors.append("Return date")

    try:
        validate_not_empty(notification_return_type, "Notification return type")
    except ValueError:
        errors.append("Notification return type")

    try:
        validate_not_empty(office, "Office")
    except ValueError:
        errors.append("Office")

    try:
        validate_state(state)
    except ValueError:
        errors.append("State")

    try:
        validate_not_empty(registry_office, "Registry office")
    except ValueError:
        errors.append("Registry office")

    try:
        validate_not_empty(name, "Name")
    except ValueError:
        errors.append("Name")

    try:
        validate_not_empty(justification, "Justification")
    except ValueError:
        errors.append("Justification")

    return len(errors) == 0, errors
