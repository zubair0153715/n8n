"""Unit conversion helpers used across the toolkit."""

from __future__ import annotations


def lb_to_kg(pounds: float) -> float:
    """Convert pounds to kilograms."""
    if pounds < 0:
        raise ValueError("weight cannot be negative")
    return pounds * 0.45359237


def kg_to_lb(kg: float) -> float:
    """Convert kilograms to pounds."""
    if kg < 0:
        raise ValueError("weight cannot be negative")
    return kg / 0.45359237


def in_to_m(inches: float) -> float:
    """Convert inches to meters."""
    if inches < 0:
        raise ValueError("height cannot be negative")
    return inches * 0.0254


def cm_to_m(cm: float) -> float:
    """Convert centimeters to meters."""
    if cm < 0:
        raise ValueError("height cannot be negative")
    return cm / 100.0
