"""Command-line interface for the Health Toolkit.

Examples:
    python -m health_toolkit.cli bmi --weight 70 --height 1.75
    python -m health_toolkit.cli bp --systolic 135 --diastolic 85
"""

from __future__ import annotations

import argparse
import sys

from . import vitals


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="health-toolkit",
        description="A small runnable health-data toolkit (educational, not a medical device).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_bmi = sub.add_parser("bmi", help="Calculate BMI and category")
    p_bmi.add_argument("--weight", type=float, required=True, help="weight in kg")
    p_bmi.add_argument("--height", type=float, required=True, help="height in meters")

    p_bp = sub.add_parser("bp", help="Classify blood pressure")
    p_bp.add_argument("--systolic", type=int, required=True)
    p_bp.add_argument("--diastolic", type=int, required=True)

    p_hr = sub.add_parser("hr", help="Karvonen target heart rate")
    p_hr.add_argument("--age", type=int, required=True)
    p_hr.add_argument("--resting", type=int, required=True, help="resting heart rate")
    p_hr.add_argument("--intensity", type=float, required=True, help="0..1")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "bmi":
        value = vitals.bmi(args.weight, args.height)
        print(f"BMI: {value} ({vitals.bmi_category(value)})")
    elif args.command == "bp":
        category = vitals.blood_pressure_category(args.systolic, args.diastolic)
        print(f"Blood pressure: {args.systolic}/{args.diastolic} -> {category}")
    elif args.command == "hr":
        target = vitals.heart_rate_zone(args.age, args.resting, args.intensity)
        print(f"Target heart rate: {target} bpm")
    else:  # pragma: no cover
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
