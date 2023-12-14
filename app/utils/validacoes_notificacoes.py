from datetime import datetime
import pandas as pd

def valida_numero(valor): 
    if not valor or pd.isna(valor):
        raise ValueError("Valor não pode ser vazio ou nulo")
    elif not str(valor).isdigit():
        raise ValueError("Valor inválido")
    return valor

def valida_nome(nome):
    if not nome or pd.isna(nome):
        raise ValueError("Nome não pode ser vazio ou nulo")
    return nome

def valida_tipo_retorno(tipo_retorno):
    if not tipo_retorno or pd.isna(tipo_retorno):
        raise ValueError("Tipo de retorno não pode ser vazio ou nulo")
    # Aqui você pode adicionar qualquer outra lógica de validação necessária
    return tipo_retorno

def valida_uf(uf):
    estados_brasileiros = [
        "AC", "AL", "AP", "AM", "BA",
        "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB",
        "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP",
        "SE", "TO"
    ]
    if not uf or pd.isna(uf):
        raise ValueError("UF não pode ser vazia ou nula")
    elif uf.upper() not in estados_brasileiros:
        raise ValueError("UF inválida")
    return uf.upper()

def valida_data(data):
    if not data or pd.isna(data):
        raise ValueError("Data não pode ser vazia ou nula")
    try:
        return datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Data inválida")
    
def valida_escritorio(escritorio):
    if not escritorio or pd.isna(escritorio):
        raise ValueError("Escritorio não pode ser vazio ou nulo")
    return escritorio

def valida_cartorio(cartorio):
    if not cartorio or pd.isna(cartorio):
        raise ValueError("Cartório não pode ser vazio ou nulo")
    return cartorio

def valida_contrato(contrato):
    if not contrato or pd.isna(contrato):
        raise ValueError("Contrato não pode ser vazio ou nulo")
    elif not str(contrato).isdigit():
        raise ValueError("Contrato inválido")
    return contrato

def validar_dados_notificacao(grupo, cota, data_envio, data_retorno, tipo_retorno, escritorio, uf, cartorio, nome, contrato):
    erros = []

    try:
        valida_numero(grupo)
    except ValueError as e:
        erros.append("Grupo")

    try:
        valida_numero(cota)
    except ValueError as e:
        erros.append("Cota")

    try:
        valida_contrato(contrato)
    except ValueError as e:
        erros.append("Contrato")

    try:
        valida_data(data_envio)
    except ValueError as e:
        erros.append("DataDeEnvio")

    try:
        valida_data(data_retorno)
    except ValueError as e:
        erros.append("DataDeRetorno")

    try:
        valida_tipo_retorno(tipo_retorno)
    except ValueError as e:
        erros.append("Tipo de retorno")

    try:
        valida_escritorio(escritorio)
    except ValueError as e:
        erros.append("Escritório")

    try:
        valida_uf(uf)
    except ValueError as e:
        erros.append("UF")

    try:
        valida_cartorio(cartorio)
    except ValueError as e:
        erros.append("Cartório")

    try:
        valida_nome(nome)
    except ValueError as e:
        erros.append("Nome")

    return len(erros) == 0, erros