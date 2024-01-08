import pandas as pd
from entities.notification import Notification
from factories.notification_factory import create_notification
from utils.notification_validations import validate_notification_data
from utils.type_conversion import convert_date
from sqlalchemy import and_
from sqlalchemy import func, select, case
import calendar

def add_notifications_to_database(session, notifications):
    try:
        # Add each valid notification to the session
        for notification in notifications:
            session.add(notification)
    except Exception as e:
        # In case of an error, error handling and rollback should be done externally
        print(f"Error preparing notifications for addition: {e}")
        raise

def import_notifications_from_excel(file_path):
    df = pd.read_excel(file_path)
    valid_notifications = []
    invalid_notifications = []
    for _, row in df.iterrows():
        notification = create_notification(row)
        if notification.is_valid:
            valid_notifications.append(notification)
        else:
            invalid_notifications.append(notification)

    return valid_notifications, invalid_notifications

def revalidate_notification(self):
        self.is_valid, self.errors = validate_notification_data(
            self.group, self.quota, self.send_date, self.return_date, self.return_type,
            self.office, self.state, self.registry_office, self.name, self.contract, self.justification
        )

        if self.is_valid:
            self.send_date = convert_date(self.send_date)
            self.return_date = convert_date(self.return_date)
            return {"status": "success", "message": "Notification successfully validated."}
        else:
            return {"status": "error", "message": "Validation errors found.", "errors": self.errors}
        
def filter_notifications_by_date(query, start_date=None, end_date=None, granularity='daily'):
    if start_date:
        start_date = convert_date(start_date)

    if end_date:
        end_date = convert_date(end_date)
        if granularity == 'monthly':
            last_day = calendar.monthrange(end_date.year, end_date.month)[1]
            end_date = end_date.replace(day=last_day)

    date_filters = []
    if start_date:
        date_filters.append(Notification._send_date >= start_date)
    if end_date:
        date_filters.append(Notification._send_date <= end_date)

    return query.filter(and_(*date_filters))

def filter_notifications_by_state(query, states=None):
    if states:
        return query.filter(Notification._state.in_(states))
    return query

def group_notifications_by_return_type_and_state(query):
    # Usando a query como um filtro, sem incluir todas as suas colunas na subconsulta
    filtered_query = query.with_entities(
        Notification._state,
        Notification._return_type,
        func.count().label('count')
    ).group_by(
        Notification._state,
        Notification._return_type
    ).subquery('filtered_counts')

    # Construindo a consulta agrupada final com base na subconsulta filtrada
    grouped_query = select(
        filtered_query.c._state.label('state'),
        func.sum(case((filtered_query.c._return_type == 'positiva', filtered_query.c.count), else_=0)).label('positiva'),
        func.sum(case((filtered_query.c._return_type == 'negativa', filtered_query.c.count), else_=0)).label('negativa'),
        func.sum(case((filtered_query.c._return_type == 'notificando', filtered_query.c.count), else_=0)).label('notificando'),
        func.sum(filtered_query.c.count).label('todas')
    ).group_by(
        filtered_query.c._state
    )
    return grouped_query

def group_notifications_by_return_type_and_date(query, granularity='daily'):
    # Ajustando a extração da data com base na granularidade
    if granularity == 'monthly':
        date_part = func.strftime('%Y-%m', Notification._send_date)
    elif granularity == 'daily':
        date_part = func.strftime('%Y-%m-%d', Notification._send_date)
    else:
        raise ValueError("Granularity must be 'daily' or 'monthly'")

    # Usando a query como um filtro, selecionando apenas as colunas necessárias para a subconsulta
    filtered_query = query.with_entities(
        date_part.label('send_date'),
        Notification._return_type,
        func.count().label('count')
    ).group_by(
        date_part,
        Notification._return_type
    ).subquery('filtered_counts')

    # Construir a query agrupada final com base na subconsulta filtrada
    grouped_query = select(
        filtered_query.c.send_date,
        func.sum(case((filtered_query.c._return_type == 'positiva', filtered_query.c.count), else_=0)).label('positiva'),
        func.sum(case((filtered_query.c._return_type == 'negativa', filtered_query.c.count), else_=0)).label('negativa'),
        func.sum(case((filtered_query.c._return_type == 'notificando', filtered_query.c.count), else_=0)).label('notificando'),
        func.sum(filtered_query.c.count).label('todas')
    ).group_by(
        filtered_query.c.send_date
    )

    return grouped_query
