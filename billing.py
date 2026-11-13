"""Billing code that must match the canonical invoice contract."""


def calculate_invoice_total(line_items, tax_rate=0.10):
    subtotal = sum(item["price"] * item["qty"] for item in line_items)
    tax = subtotal * tax_rate
    return {"subtotal": subtotal, "tax": tax, "total": subtotal + tax}


def invoice_for_order(order):
    return calculate_invoice_total(order["items"])
