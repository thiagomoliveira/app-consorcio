def valida_numero(valor, nome="Valor"):
    if valor.isdigit():
        return valor
    else:
        raise ValueError(f"{nome} deve conter apenas números")

def valida_justificativa(justificativa):
    opcoes_validas = ["positiva", "negativa", "notificando"]
    if justificativa.lower() in opcoes_validas:
        return justificativa
    else:
        raise ValueError("Justificativa inválida")

def valida_uf(uf):
    estados_brasileiros = [
    "AC", "AL", "AP", "AM", "BA",
    "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB",
    "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP",
    "SE", "TO"
]
    if uf.upper() in estados_brasileiros:
        return uf.upper()
    else:
        raise ValueError("UF inválida")
    
from datetime import datetime

def valida_data(data, contexto_data=None):
    try:
        datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        detalhe_msg = f" {contexto_data}" if contexto_data else ""
        raise ValueError(f"Data{detalhe_msg} inválida, o formato deve ser dd/mm/aaaa")

    
def converte_data_para_python(data):
    return datetime.strptime(data, '%d/%m/%Y')


