from entities.valid_notification import ValidNotification
from entities.invalid_notification import InvalidNotification
from exceptions.notification_exception import NotificationException

def create_notification(data):
    try:
        notification = ValidNotification(
            group=data['Grupo'],
            quota=data['Cota'],
            send_date=data['DataDeEnvio'],
            return_date=data['DataDeRetorno'],
            notification_return_type=data['TipoDoRetorno'],
            office=data['Escritório'],
            state=data['UF'],
            registry_office=data.get('Cartório'),
            name=data.get('Nome'),
            contract=data.get('Contrato'),
            justification=data.get("Justificativa")
        )
        return notification
    except NotificationException as e:
        return InvalidNotification(data, str(e))
