import pandas as pd
from datetime import timedelta
from utils.conversoes_tipos import converter_data
import calendar

def filtrar_notificacoes(notificacoes, data_inicio=None, data_fim=None, estados=None):
    notificacoes_filtradas = []
    if data_inicio:
            data_inicio = converter_data(data_inicio)
    if data_fim:
        data_fim = converter_data(data_fim)
        ultimo_dia = calendar.monthrange(data_fim.year, data_fim.month)[1]
        data_fim = data_fim.replace(day=ultimo_dia)
    for notificacao in notificacoes:
        data_envio = notificacao.get_data_envio()
        estado = notificacao.get_uf()
        if (data_inicio and data_envio <= data_inicio) or (data_fim and data_envio >= data_fim):
            continue
        if estados and estado not in estados:
            continue
        notificacoes_filtradas.append(notificacao)
    return notificacoes_filtradas

def agrupar_notificacoes_por_tipo_e_data(notificacoes, granularidade='mensal'):
    # Tipos de retorno esperados
    tipos_retorno = ["positiva", "negativa", "notificando"]
    dados_agrupados = {}
    totais_por_data = {}

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

        # Acumulando totais por data
        if data_envio not in totais_por_data:
            totais_por_data[data_envio] = 0
        totais_por_data[data_envio] += 1

    # Convertendo o dicionário agrupado em um DataFrame
    df_agrupado = pd.DataFrame(list(dados_agrupados.items()), columns=['DataDeEnvio_Tipo', 'Contagem'])
    df_agrupado[['DataDeEnvio', 'TipoDeRetorno']] = pd.DataFrame(df_agrupado['DataDeEnvio_Tipo'].tolist(), index=df_agrupado.index)
    df_agrupado.drop(columns=['DataDeEnvio_Tipo'], inplace=True)

    # Reestruturando o DataFrame
    df_agrupado = df_agrupado.pivot_table(index='DataDeEnvio', columns='TipoDeRetorno', values='Contagem', fill_value=0)

    # Garantindo que todos os tipos de retorno e totais estejam presentes
    for tipo in tipos_retorno:
        if tipo not in df_agrupado.columns:
            df_agrupado[tipo] = 0
    df_agrupado['total'] = df_agrupado.sum(axis=1)

    # Incluindo totais por data de envio
    for data, total in totais_por_data.items():
        df_agrupado.at[data, 'total'] = total

    return df_agrupado

def agrupar_notificacoes_por_estado(notificacoes):
    agrupamento_por_estado = {}
    for notificacao in notificacoes:
        estado = notificacao.get_uf()
        tipo_retorno = notificacao.get_tipo_retorno()
        
        if estado not in agrupamento_por_estado:
            agrupamento_por_estado[estado] = {'total': 0, 'positiva': 0, 'negativa': 0, 'notificando': 0}
        
        agrupamento_por_estado[estado]['total'] += 1
        if tipo_retorno == 'positiva':
            agrupamento_por_estado[estado]['positiva'] += 1
        elif tipo_retorno == 'negativa':
            agrupamento_por_estado[estado]['negativa'] += 1
        elif tipo_retorno == 'notificando':
            agrupamento_por_estado[estado]['notificando'] += 1
    
    return agrupamento_por_estado