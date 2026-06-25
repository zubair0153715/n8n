"""A small Patient model plus a minimal FHIR Patient resource parser.

FHIR (Fast Healthcare Interoperability Resources) is the standard for exchanging
healthcare data. This parses the common fields from a FHIR R4 Patient resource.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class Patient:
    """A simple normalized patient record."""

    given_name: str = ""
    family_name: str = ""
    gender: str = ""
    birth_date: str = ""
    identifiers: list[str] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"{self.given_name} {self.family_name}".strip()

    def to_dict(self) -> dict[str, Any]:
        return {
            "given_name": self.given_name,
            "family_name": self.family_name,
            "full_name": self.full_name,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "identifiers": list(self.identifiers),
        }


def parse_fhir_patient(resource: dict[str, Any]) -> Patient:
    """Parse a FHIR R4 Patient resource (as a dict) into a Patient.

    Tolerant of missing fields — returns empty strings/lists when absent.
    """
    if not isinstance(resource, dict):
        raise TypeError("resource must be a dict")
    if resource.get("resourceType") not in (None, "Patient"):
        raise ValueError("resource is not a FHIR Patient")

    given_name = ""
    family_name = ""
    names = resource.get("name") or []
    if names:
        primary = names[0]
        given_list = primary.get("given") or []
        given_name = " ".join(given_list).strip()
        family_name = (primary.get("family") or "").strip()

    identifiers: list[str] = []
    for ident in resource.get("identifier") or []:
        value: Optional[str] = ident.get("value")
        if value:
            identifiers.append(value)

    return Patient(
        given_name=given_name,
        family_name=family_name,
        gender=resource.get("gender", "") or "",
        birth_date=resource.get("birthDate", "") or "",
        identifiers=identifiers,
    )
