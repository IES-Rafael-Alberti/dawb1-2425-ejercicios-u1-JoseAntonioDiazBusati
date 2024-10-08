import pytest
from src.ej02_def import importe

@pytest.mark.parametrize(
    "horas_total, coste_total, expected",
    [
        (4, 7.89, 31.56),
        (7, 10, 70),
        (11, 5.54, 60.94),
        (8, 7, 56)
    ]
)
def test_importe(horas_total,coste_total,expected):
    assert importe(horas_total, coste_total)==expected