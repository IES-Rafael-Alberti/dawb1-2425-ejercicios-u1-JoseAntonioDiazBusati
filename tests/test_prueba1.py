import pytest
from src.prueba1 import comparar_num

@pytest.mark.parametrize(
    "n1, n2, expected",
    [
        (4, 9, 9),
        (1, 1, 0),
        (74, 97, 97),
        (12, 1, 12),
        (5, -5, 5)
    ]
)
def test_comparar_num(n1, n2, expected):
    assert comparar_num(n1, n2) == expected