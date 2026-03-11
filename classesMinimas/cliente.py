class Cliente:
    def __init__(self, idCliente, nomeCliente):
        self.idCliente = idCliente
        self.nomeCliente = nomeCliente
        
    def __str__(self):
        return f"ID: {self.idCliente}, Nome: {self.nomeCliente}"