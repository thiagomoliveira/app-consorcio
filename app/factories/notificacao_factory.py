from entities.notificacao_valida import NotificacaoValida
from entities.notificacao_invalida import NotificacaoInvalida
from exceptions.notificacao_exception import ErroNotificacao

def criar_notificacao(dados):
    try:
        notificacao = NotificacaoValida(
            grupo=dados['Grupo'],
            cota=dados['Cota'],
            data_envio=dados['DataDeEnvio'],
            data_retorno=dados['DataDeRetorno'],
            tipo_retorno=dados['TipoDeRetorno'],
            escritorio=dados['Escritório'],
            uf=dados['UF'],
            cartorio=dados.get('Cartório'),
            nome=dados.get('Nome'),
            contrato=dados.get('Contrato'),
            justificativa=dados.get("Justificativa")

        )
        return notificacao
    except ErroNotificacao as e:
        return NotificacaoInvalida(dados, str(e))
