from datetime import datetime

def converter_data(data_str):
    # Verificar se 'data_str' já é uma instância de datetime
    if isinstance(data_str, datetime):
        return data_str
    try:
        return datetime.strptime(data_str, '%d/%m/%Y')
    except ValueError:
        raise f"Data inválida: {data_str}"