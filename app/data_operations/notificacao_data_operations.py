import pandas as pd
from utils.conversoes_tipos import converter_data

def filtrar_notificacoes(notificacoes, data_inicio=None, data_fim=None, estados=None):
    notificacoes_filtradas = []
    for notificacao in notificacoes:
        if data_inicio:
            data_inicio = converter_data(data_inicio)
        if data_fim:
            data_fim = converter_data(data_fim)
        data_envio = notificacao.get_data_envio()
        estado = notificacao.get_uf()


        if (data_inicio and data_envio < data_inicio) or (data_fim and data_envio > data_fim):
            continue
        if estados and estado not in estados:
            continue

        notificacoes_filtradas.append(notificacao)

    return notificacoes_filtradas

def agrupar_notificacoes_por_tipo_e_data(notificacoes, granularidade='mensal'):
    # Tipos de retorno esperados
    tipos_retorno = ["positiva", "negativa", "notificando"]
    dados_agrupados = {}

    for notificacao in notificacoes:
        data_envio = notificacao.get_data_envio()

        # Ajustando a data para incluir apenas o ano e o mês
        if granularidade == 'mensal':
            data_envio = data_envio.strftime('%Y-%m')

        tipo_retorno = notificacao.get_tipo_retorno()
        chave = (data_envio, tipo_retorno)

        if chave not in dados_agrupados:
            dados_agrupados[chave] = 0
        dados_agrupados[chave] += 1

    # Convertendo o dicionário agrupado em um DataFrame para visualização
    df_agrupado = pd.DataFrame(list(dados_agrupados.items()), columns=['DataDeEnvio_Tipo', 'Contagem'])
    df_agrupado[['DataDeEnvio', 'TipoDeRetorno']] = pd.DataFrame(df_agrupado['DataDeEnvio_Tipo'].tolist(), index=df_agrupado.index)
    df_agrupado.drop(columns=['DataDeEnvio_Tipo'], inplace=True)

    # Reestruturando o DataFrame para melhor visualização
    df_agrupado = df_agrupado.pivot_table(index='DataDeEnvio', columns='TipoDeRetorno', values='Contagem', fill_value=0)

    # Garantindo que todos os tipos de retorno estejam presentes
    for tipo in tipos_retorno:
        if tipo not in df_agrupado.columns:
            df_agrupado[tipo] = 0

    return df_agrupado
