import pandas as pd
from entities.notificacao_invalida import NotificacaoInvalida
from factories.notificacao_factory import criar_notificacao

def importar_notificacao(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    notificacoes_validas = []
    notificacoes_invalidas = []
    for _, row in df.iterrows():
        notificacao = criar_notificacao(row)
        if isinstance(notificacao, NotificacaoInvalida):
            notificacoes_invalidas.append(notificacao)
        else:
            notificacoes_validas.append(notificacao)

    return notificacoes_validas, notificacoes_invalidas