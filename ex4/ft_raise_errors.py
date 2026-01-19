def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validates plant health parameters and raises errors if values are invalid.
    Returns a success message if all checks pass.
    """

    # 1) Validate that the plant name is not empty or None
    if plant_name is None or plant_name == "":
        # If the name is invalid, raise a ValueError
        raise ValueError("Plant name cannot be empty!")

    # 2) Validate water level: must be between 1 and 10
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    # 3) Validate sunlight hours: must be between 2 and 12
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} \
                        is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    # If everything is correct, return a success message
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    # Program header
    print("=== Garden Plant Health Checker ===")

    # 1) Valid case: should not raise any errors
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 2, 5))
    except ValueError as e:
        # If an error occurs, print it
        print("Error:", e)

    # 2) Empty plant name case: should raise ValueError
    print("Testing empty plant name...")
    try:
        check_plant_health(None, 5, 5)
    except ValueError as e:
        print("Error:", e)

    # 3) Invalid water level case: should raise ValueError
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print("Error:", e)

    # 4) Invalid sunlight hours case: should raise ValueError
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print("Error:", e)

    # Final message indicating all tests finished
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
