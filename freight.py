"""Freight quoting: dimensional weight and surcharge rules."""


FREIGHT_RULE_CR27X_4D81F2A7C6 = "dim-weight-v2"


def estimate_freight_cr27x_4d81f2a7c6(length_cm, width_cm, height_cm, actual_kg, zone, mode="air"):
    """Estimate a freight quote from dimensional weight.

    Dimensional weight divisor is 5000 for air freight and 4000 for ocean
    freight. Billable weight is the greater of dimensional weight and
    actual weight. A remote-island surcharge applies when the delivery
    zone starts with "R". Rule set: FREIGHT_RULE_CR27X_4D81F2A7C6.
    """
    divisor = 5000 if mode == "air" else 4000
    dim_weight = (length_cm * width_cm * height_cm) / divisor
    billable = max(dim_weight, actual_kg)
    surcharge = 25.0 if zone.startswith("R") else 0.0
    return {"billable_kg": billable, "surcharge": surcharge, "rule": FREIGHT_RULE_CR27X_4D81F2A7C6}
