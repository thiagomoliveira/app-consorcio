from datetime import datetime

def converter_data(data_str):
    # Verifica se data_str é uma instância de datetime e a converte para string se necessário
    if isinstance(data_str, datetime):
        return data_str

    try:
        # Tenta converter usando o formato dia/mês/ano
        return datetime.strptime(data_str, '%d/%m/%Y')
    except ValueError:
        try:
            # Se falhar, tenta converter usando o formato mês/ano
            return datetime.strptime(data_str, '%m/%Y')
        except ValueError:
            raise ValueError(f"Data inválida: {data_str}")