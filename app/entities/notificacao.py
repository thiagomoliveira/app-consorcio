from utils.validacoes import valida_numero, valida_data, converte_data_para_python, valida_justificativa, valida_uf

class Notificacao:
    def __init__(self, grupo, cota, data_envio, data_retorno, justificativa, escritorio, uf):
        self.set_grupo(grupo)
        self.set_cota(cota)
        self.set_data_envio(data_envio)
        self.set_data_retorno(data_retorno)
        self.set_justificativa(justificativa)
        self.set_escritorio(escritorio) 
        self.set_uf(uf)

    # Getters e Setters com validação
    def get_grupo(self):
        return self._grupo

    def set_grupo(self, grupo):
        if not grupo:
            raise ValueError("Grupo não pode ser vazio")
        self._grupo = valida_numero(grupo, "Grupo")

    def get_cota(self):
        return self._cota

    def set_cota(self, cota):
        if not cota:
            raise ValueError("Cota não pode ser vazia")
        self._cota = valida_numero(cota, "Cota")

    def get_data_envio(self):
        return self._data_envio

    def set_data_envio(self, data_envio):
        if not data_envio:
            raise ValueError("Data de envio não pode ser vazia")
        valida_data(data_envio, "de envio")
        self._data_envio = converte_data_para_python(data_envio)

    def get_data_retorno(self):
        return self._data_retorno

    def set_data_retorno(self, data_retorno):
        if not data_retorno:
            raise ValueError("Data de retorno não pode ser vazia")
        valida_data(data_retorno, "de retorno")
        self._data_retorno = converte_data_para_python(data_retorno)

    def get_justificativa(self):
        return self._justificativa

    def set_justificativa(self, justificativa):
        if not justificativa:
            raise ValueError("Justificativa não pode ser vazia")
        self._justificativa = valida_justificativa(justificativa)

    def get_escritorio(self):
        return self._escritorio

    def set_escritorio(self, escritorio):
        if not escritorio:
            raise ValueError("Escritorio não pode ser vazio")
        self._escritorio = escritorio


    def get_uf(self):
        return self._uf

    def set_uf(self, uf):
        if not uf:
            raise ValueError("UF não pode ser vazia")
        self._uf = valida_uf(uf)

    # Métodos mágicos
    def __eq__(self, other):
        if not isinstance(other, Notificacao):
            return False
        return (self._grupo, self._cota) == (other._grupo, other._cota)
    
    def __hash__(self):
        return hash((self._grupo, self._cota))

    def __str__(self):
        return (f"Notificacao(grupo={self._grupo}, cota={self._cota}, data_envio={self._data_envio}, "
                f"data_retorno={self._data_retorno}, justificativa={self._justificativa}, "
                f"escritorio={self._escritorio}, uf={self._uf})")