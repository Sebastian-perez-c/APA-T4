"""
Nombre y apellidos: Sebastian Pérez

Este módulo implementa la generación de números pseudoaleatorios mediante el algoritmo
lineal congruente (LGC), utilizando una clase iterable `Aleat` y una función generadora
`aleat`. Ambas implementaciones permiten configurar los parámetros del generador (m, a, c, x0)
y reiniciar la secuencia con una nueva semilla.

Ejecutar los tests unitarios:
    python3 -m doctest -v aleatorios.py
"""

class Aleat:
    """
    Generador de números pseudoaleatorios usando el método LGC como clase iterable.

    Atributos:
    - m (int): módulo
    - a (int): multiplicador
    - c (int): incremento
    - x (int): valor actual de la secuencia

    Métodos:
    - __next__(): devuelve el siguiente número pseudoaleatorio
    - __call__(x0): reinicia la secuencia con una nueva semilla

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0):
        self.x = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Generador de números pseudoaleatorios usando el método LGC como generador.

    Argumentos:
    - m (int): módulo
    - a (int): multiplicador
    - c (int): incremento
    - x0 (int): semilla inicial

    Devuelve:
    - números pseudoaleatorios en el rango [0, m)

    Se puede reiniciar la secuencia enviando una nueva semilla con send().

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        new_seed = yield (x := (a * x + c) % m)
        if new_seed is not None:
            x = new_seed


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
