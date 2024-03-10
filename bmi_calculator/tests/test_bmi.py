# tests/test_bmi_calculator.py
from src.bmi_calculator import calculate_bmi
import pytest

def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.86

def test_calculate_bmi_zero_height():
    with pytest.raises(ValueError, match="Height must be greater than 0."):
        calculate_bmi(70, 0)