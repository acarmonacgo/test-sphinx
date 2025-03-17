"""
This module contains an example function for Sphinx.
"""

def hello_world(name: str) -> str:
    """
    Returns a personalized greeting.

    :param name: Name of the person to greet.
    :type name: str
    :return: Greeting message.
    :rtype: str

    **Example usage:**

    >>> hello_world("Augusto")
    'Hello, Augusto!'
    """
    return f"Hello, {name}!"
