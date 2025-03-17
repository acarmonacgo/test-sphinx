"""
Este módulo contiene una función de ejemplo para Sphinx.
"""

def hello_world(name: str) -> str:
    """
    Devuelve un saludo personalizado.

    :param name: Nombre de la persona a saludar.
    :type name: str
    :return: Mensaje de saludo.
    :rtype: str

    **Ejemplo de uso:**

    >>> hello_world("Augusto")
    'Hola, Augusto!'
    """
    return f"Hola, {name}!"
