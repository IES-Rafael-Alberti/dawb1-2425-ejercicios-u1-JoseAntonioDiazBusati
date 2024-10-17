import pytest
from src.ej11_def import suma_entero

@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1.0),
        (2, 3.0),
        (3, 6.0),
        (4, 10.0)
    ]
)
def test_suma_entero(n, expected):
    assert suma_entero(n)==expected