"""Input validation helpers."""


def validate_user_input(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a dict")
    name = data.get("name", "")
    if len(name) > 100:
        raise ValueError("name too long")
    return {"name": name.strip(), "age": data.get("age")}
