# Health Toolkit

A small, runnable Python toolkit for common health-data tasks (BMI, blood pressure,
heart-rate zones, FHIR patient parsing). Original, working code you can clone and run.

Not a medical device — educational/demo only.

Quick start:

    cd app
    pip install -r requirements.txt
    pytest -q
    python -m health_toolkit.cli bmi --weight 70 --height 1.75

License: MIT
