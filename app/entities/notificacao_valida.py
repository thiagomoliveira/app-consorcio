from utils.validacoes_notificacoes import *
from exceptions.notificacao_exception import ErroNotificacao

class NotificacaoValida:
    def __init__(self, grupo, cota, data_envio, data_retorno, tipo_retorno, escritorio, uf, cartorio, nome, contrato, justificativa):
        valido, erros = validar_dados_notificacao(grupo, cota, data_envio, data_retorno, tipo_retorno, escritorio, uf, cartorio, nome, contrato, justificativa)
        if not valido:
            raise ErroNotificacao(erros)
        
        self._grupo = grupo
        self._cota = cota
        self._data_envio = data_envio
        self._data_retorno = data_retorno
        self._tipo_retorno = tipo_retorno
        self._escritorio = escritorio
        self._uf = uf
        self._cartorio = cartorio
        self._nome = nome
        self._contrato = contrato
        self._justificativa = justificativa

    # Getters e Setters com validação
    def get_grupo(self):
        return self._grupo

    def set_grupo(self, grupo):
        self._grupo = valida_numero(grupo)

    def get_cota(self):
        return self._cota

    def set_cota(self, cota):
        self._cota = valida_numero(cota)

    def get_data_envio(self):
        return self._data_envio

    def set_data_envio(self, data_envio):
        self._data_envio = valida_data(data_envio)

    def get_data_retorno(self):
        return self._data_retorno

    def set_data_retorno(self, data_retorno):
        self._data_retorno = valida_data(data_retorno)

    def get_tipo_retorno(self):
        return self._tipo_retorno

    def set_tipo_retorno(self, tipo_retorno):
        self._tipo_retorno = valida_tipo_retorno(tipo_retorno) 

    def get_escritorio(self):
        return self._escritorio

    def set_escritorio(self, escritorio):
        self._escritorio = valida_escritorio(escritorio)

    def get_uf(self):
        return self._uf

    def set_uf(self, uf):
        self._uf = valida_uf(uf)

    def get_cartorio(self):
        return self._cartorio

    def set_cartorio(self, cartorio):
        self._cartorio = valida_cartorio(cartorio)

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = valida_nome(nome)

    def get_contrato(self):
        return self._contrato

    def set_contrato(self, contrato):
        self._contrato = valida_contrato(contrato)

    def get_justificativa(self):
        return self._justificativa
    
    def set_justificativa(self, justificativa):
        self._justificativa = valida_justificativa(justificativa)
        
    # Métodos mágicos
    def __eq__(self, other):
        if not isinstance(other, NotificacaoValida):
            return False
        return (self._grupo, self._cota) == (other._grupo, other._cota)

    def __hash__(self):
        return hash((self._grupo, self._cota))

    def __str__(self):
        return (f"Notificacao(grupo={self._grupo}, cota={self._cota}, data_envio={self._data_envio}, "
                f"data_retorno={self._data_retorno}, tipo_retorno={self._tipo_retorno}, "
                f"escritorio={self._escritorio}, uf={self._uf}, cartorio={self._cartorio}, "
                f"nome={self._nome}, contrato={self._contrato}, justificativa={self._justificativa})")