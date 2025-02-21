from .DatabaseContext.DatabaseContext import DatabaseContext
from .DatabaseContext.IDatabaseContext import IDatabaseContext

def register_services(container):
    container[IDatabaseContext] = DatabaseContext
