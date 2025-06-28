class LivreIndisponibleError(Exception):
    def __init__(self, message="Livre Indisponible!"):
        super().__init__(message)

class QuotaEmpruntDepasseError(Exception):
    def __init__(self, message="Quota Emprunt Depasse!"):
        super().__init__(message)

class MembreInexistantError(Exception):
    def __init__(self, message="Membre Inexistant!"):
        super().__init__(message)

class LivreInexistantError(Exception):
    def __init__(self, message="Livre Inexistant!"):
        super().__init__(message)