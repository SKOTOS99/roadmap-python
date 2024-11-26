

class TaskModel:

    def __init__(self, ids, tittle, description, active):
        self.ids = ids
        self.tittle = tittle
        self.description = description
        self.active = active

    def to_dict(self):
        """Convierte el objeto Task a un diccionario serializable en JSON."""
        return {
            "ids": self.ids,
            "title": self.tittle,
            "description": self.description,
            "active": self.active,
        }
