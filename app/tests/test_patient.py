import pytest

from health_toolkit.patient import Patient, parse_fhir_patient


def test_parse_fhir_patient():
    resource = {
        "resourceType": "Patient",
        "identifier": [{"value": "12345"}],
        "name": [{"given": ["John", "Q"], "family": "Doe"}],
        "gender": "male",
        "birthDate": "1990-05-01",
    }
    p = parse_fhir_patient(resource)
    assert p.full_name == "John Q Doe"
    assert p.gender == "male"
    assert p.birth_date == "1990-05-01"
    assert p.identifiers == ["12345"]


def test_parse_fhir_patient_missing_fields():
    p = parse_fhir_patient({"resourceType": "Patient"})
    assert p.full_name == ""
    assert p.identifiers == []


def test_parse_fhir_wrong_type():
    with pytest.raises(ValueError):
        parse_fhir_patient({"resourceType": "Observation"})


def test_patient_to_dict():
    p = Patient(given_name="Jane", family_name="Roe", gender="female")
    d = p.to_dict()
    assert d["full_name"] == "Jane Roe"
    assert d["gender"] == "female"
