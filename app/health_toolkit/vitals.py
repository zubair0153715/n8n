"""Core vital-sign calculations: BMI, blood pressure, heart-rate zones.

All thresholds follow widely used clinical references (WHO BMI categories,
ACC/AHA blood-pressure categories). This is educational/demo software and is
NOT a medical device — do not use for diagnosis.
"""

from __future__ import annotations


def bmi(weight_kg: float, height_m: float) -> float:
    """Return Body Mass Index (kg/m^2), rounded to 1 decimal place."""
    if weight_kg <= 0:
        raise ValueError("weight_kg must be positive")
    if height_m <= 0:
        raise ValueError("height_m must be positive")
    return round(weight_kg / (height_m ** 2), 1)


def bmi_category(value: float) -> str:
    """Classify a BMI value using WHO categories."""
    if value < 18.5:
        return "underweight"
    if value < 25:
        return "normal"
    if value < 30:
        return "overweight"
    return "obese"


def blood_pressure_category(systolic: int, diastolic: int) -> str:
    """Classify blood pressure using ACC/AHA 2017 categories.

    Returns one of: 'normal', 'elevated', 'hypertension_stage_1',
    'hypertension_stage_2', 'hypertensive_crisis'.
    """
    if systolic <= 0 or diastolic <= 0:
        raise ValueError("blood pressure readings must be positive")

    if systolic > 180 or diastolic > 120:
        return "hypertensive_crisis"
    if systolic >= 140 or diastolic >= 90:
        return "hypertension_stage_2"
    if systolic >= 130 or diastolic >= 80:
        return "hypertension_stage_1"
    if 120 <= systolic < 130 and diastolic < 80:
        return "elevated"
    return "normal"


def heart_rate_zone(age: int, resting_hr: int, intensity: float) -> int:
    """Estimate target heart rate (bpm) using the Karvonen formula.

    intensity is a fraction between 0 and 1 (e.g. 0.7 for 70%).
    """
    if not (0 <= intensity <= 1):
        raise ValueError("intensity must be between 0 and 1")
    if age <= 0 or age > 130:
        raise ValueError("age out of range")
    if resting_hr <= 0:
        raise ValueError("resting_hr must be positive")

    max_hr = 220 - age
    reserve = max_hr - resting_hr
    return round(reserve * intensity + resting_hr)
