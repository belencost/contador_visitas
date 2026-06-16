class ContadorVisitas:
    # Las visitas comienzan en cero
    def __init__(self):
        self.visitas = 0

    # Se suma 1 al contador cada vez que alguien entra
    def incrementar(self):
        self.visitas += 1
        return self.visitas

    # Devuelve cantidad de visitas 
    def obtener_visitas(self):
        return self.visitas

    # Inicializa el contador a cero 
    def reiniciar(self):
        self.visitas = 0