from datetime import datetime

def convert_date(date_str):
    # Check if date_str is a datetime instance and convert it to string if needed
    if isinstance(date_str, datetime):
        return date_str

    try:
        # Try to convert using the day/month/year format
        return datetime.strptime(date_str, '%d/%m/%Y')
    except ValueError:
        try:
            # If it fails, try to convert using the month/year format
            return datetime.strptime(date_str, '%m/%Y')
        except ValueError:
            raise ValueError(f"Invalid date: {date_str}")
