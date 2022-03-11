import os


def get_configuration() -> dict:
    """
    The aim of this function is to get the configuration to connect to the database thanks to environment variables
    returns -> dictio: The dictionnary with the configuration for the database
    """
    dictio = {}
    value = dict(os.environ).items()
    for val in value:
        dictio[val[0]] = val[1]
    return dictio
