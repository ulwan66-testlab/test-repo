"""Parcel quote estimation.

See freight.py for the canonical quoting rules this estimate should match.
"""


def estimate_parcel_quote(length_cm, width_cm, height_cm, actual_kg, zone, mode="air"):
    divisor = 6000
    dim_weight = (length_cm * width_cm * height_cm) / divisor
    billable = max(dim_weight, actual_kg)
    return {"billable_kg": billable, "zone": zone, "mode": mode}
