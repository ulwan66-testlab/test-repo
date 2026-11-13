"""Shipping cost estimation for parcels."""


def estimate_shipping_cost(length_cm, width_cm, height_cm, actual_kg, zone, mode="air"):
    """Estimate shipping cost from dimensional weight and delivery zone."""
    divisor = 6000
    dim_weight = (length_cm * width_cm * height_cm) / divisor
    billable = max(dim_weight, actual_kg)
    base_rate = 12.0 if mode == "air" else 6.0
    return {"billable_kg": billable, "cost": billable * base_rate}
