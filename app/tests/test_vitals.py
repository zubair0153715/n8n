import pytest

from health_toolkit import vitals


def test_bmi_basic():
    assert vitals.bmi(70, 1.75) == 22.9


def test_bmi_categories():
    assert vitals.bmi_category(17) == "underweight"
    assert vitals.bmi_category(22) == "normal"
    assert vitals.bmi_category(27) == "overweight"
    assert vitals.bmi_category(33) == "obese"


def test_bmi_invalid():
    with pytest.raises(ValueError):
        vitals.bmi(0, 1.7)
    with pytest.raises(ValueError):
        vitals.bmi(70, 0)


def test_blood_pressure_categories():
    assert vitals.blood_pressure_category(118, 76) == "normal"
    assert vitals.blood_pressure_category(125, 78) == "elevated"
    assert vitals.blood_pressure_category(132, 82) == "hypertension_stage_1"
    assert vitals.blood_pressure_category(145, 95) == "hypertension_stage_2"
    assert vitals.blood_pressure_category(190, 130) == "hypertensive_crisis"


def test_heart_rate_zone():
    assert vitals.heart_rate_zone(30, 60, 0.7) == 151


def test_heart_rate_invalid():
    with pytest.raises(ValueError):
        vitals.heart_rate_zone(30, 60, 1.5)
