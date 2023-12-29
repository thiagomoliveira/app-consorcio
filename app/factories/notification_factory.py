from entities.notification import Notification

def create_notification(data):
    notification = Notification(
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
