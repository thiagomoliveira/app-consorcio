from data_import.notificacao_import import importar_notificacao
from data_operations.notificacao_data_operations import filtrar_notificacoes, agrupar_notificacoes_por_tipo_e_data
from datetime import datetime

class NotificacaoController:
    def __init__(self, data_path):
        self.data_path = data_path
        self.notificacoes_validas, self.notificacoes_invalidas = importar_notificacao(self.data_path)

    def get_initial_data(self):
        data_atual_str = datetime.now().strftime('%d/%m/%Y')
        notificacoes_filtradas = filtrar_notificacoes(
            self.notificacoes_validas, data_inicio='01/01/2010', data_fim=data_atual_str)
        return agrupar_notificacoes_por_tipo_e_data(notificacoes_filtradas)

    def get_filtered_data(self, start_date, end_date, states):
        notificacoes_filtradas = filtrar_notificacoes(
            self.notificacoes_validas, data_inicio=start_date, data_fim=end_date, estados=states)
        return agrupar_notificacoes_por_tipo_e_data(notificacoes_filtradas)