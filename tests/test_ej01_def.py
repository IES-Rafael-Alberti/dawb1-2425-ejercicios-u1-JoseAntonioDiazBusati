import pytest
from src.ej01_def import saludar

@pytest.mark.parametrize(
    "name, expected",
    [
        ("Viti", "Hola, Viti"),
        ("María", "Hola, María"),
        ("Paco", "Hola, Paco"),
        ("Diegooool", "Hola, Diegooool")
    ]
)
def test_saludar(name, expected):
    assert saludar()==expected