class ErroNotificacao(Exception):
    def __init__(self, erros):
        super().__init__(" | ".join(erros))
        self.erros = erros