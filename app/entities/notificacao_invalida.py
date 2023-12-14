class NotificacaoInvalida:
    def __init__(self, dados, erros):
        self._dados = dados  
        self._erros = erros 

    @property
    def dados(self):
        return self._dados

    @property
    def erros(self):
        return self._erros
    
    def __eq__(self, other):
        if not isinstance(other, NotificacaoInvalida):
            return False
        return (self.dados.get('grupo'), self.dados.get('cota')) == (other.dados.get('grupo'), other.dados.get('cota'))

    def __hash__(self):
        return hash((self.dados.get('grupo'), self.dados.get('cota')))

    def __str__(self):
        return (f"NotificacaoInvalida(dados={self._dados}, erros={self._erros})")
