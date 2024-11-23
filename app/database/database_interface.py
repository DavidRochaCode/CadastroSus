# database/database_interface.py
from abc import ABC, abstractmethod

#definir os métodos que todas as classes de banco de dados devem implementar.
class DatabaseInterface(ABC):
    @abstractmethod
    def execute(self, query, params=None):
        pass

    @abstractmethod
    def fetch_all(self, query, params=None):
        pass

    @abstractmethod
    def close(self):
        pass
