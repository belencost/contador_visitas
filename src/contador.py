class ContadorClics:
    # El contador de clics comienza en cero
    def __init__(self):
        self.clics = 0

    # Se suma 1 al contador cada vez que alguien clickea el botón
    def incrementar(self):
        self.clics += 1
        return self.clics

    # Devuelve cantidad de clics
    def obtener_clics(self):
        return self.clics

    # Inicializa el contador a cero 
    def reiniciar(self):
        self.clics = 0