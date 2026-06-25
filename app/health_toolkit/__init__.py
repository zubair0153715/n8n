"""Health Toolkit — a small, runnable Python library for common health-data tasks.

Inspired by the best open-source health/medical projects, this is original,
working code you can clone and run.
"""

from .vitals import bmi, bmi_category, blood_pressure_category, heart_rate_zone
from .patient import Patient, parse_fhir_patient
from .units import lb_to_kg, kg_to_lb, in_to_m, cm_to_m

__version__ = "0.1.0"

__all__ = [
    "bmi",
    "bmi_category",
    "blood_pressure_category",
    "heart_rate_zone",
    "Patient",
    "parse_fhir_patient",
    "lb_to_kg",
    "kg_to_lb",
    "in_to_m",
    "cm_to_m",
    "__version__",
]
