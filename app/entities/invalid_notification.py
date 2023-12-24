class InvalidNotification:
    def __init__(self, data, errors):
        self._data = data
        self._errors = errors

    @property
    def data(self):
        return self._data

    @property
    def errors(self):
        return self._errors
    
    def __eq__(self, other):
        if not isinstance(other, InvalidNotification):
            return False
        return (self.data.get('Grupo'), self.data.get('Cota')) == (other.data.get('Grupo'), other.data.get('Cota'))

    def __hash__(self):
        return hash((self.data.get('Grupo'), self.data.get('Cota')))

    def __str__(self):
        return (f"InvalidNotification(data={self._data}, errors={self._errors})")
