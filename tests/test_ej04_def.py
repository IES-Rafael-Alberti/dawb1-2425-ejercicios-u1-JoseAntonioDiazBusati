import pytest
from src.ej04_def import pedir_grados

@pytest.mark.parametrize(
    "fahrenheit, celsius, expected",
    [
        (49, 9.44, "9.44ºC (49.0)ºF)"),
        (32, 0.0, "0.0ºC (32.0)ºF)"),
        (86, 30.0, "30.0ºC (86.0)ºF)"),
        (75.92, 24.4, "24.4ºC (75.92)ºF)")
    ]
)
def test_pedir_grados(fahrenheit, celsius, expected):
    assert pedir_grados()==expected