import pytest
from src.ej05_def import precio

@pytest.mark.parametrize(
    "articulo, iva, expected",
    [
        (49.1, 9.44, 53.73),
        (32.0, 0.0, 32.0),
        (86.0, 30.0, 111.8),
        (75.4, 24, 93.496)
    ]
)
def test_precio(articulo, iva, expected):
    assert precio()==expected