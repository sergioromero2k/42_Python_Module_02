def water_plants(plant_list):
    """
    Simulate watering plants by ensuring that the system always closes.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                # We force an error if the plant is invalid.
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


plant_good = {"tomato", "lettuce", "carrots"}
plant_error = {"tomato", None, "carrot", "basil"}


def test_watering_system():
    """
    Run the requested tests to demonstrate the use of finally.
    """
    print("=== Garden Watering System ===")
    print(" ")
    # 1. Normal watering
    print("Testing normal watering...")
    water_plants(plant_good)
    print("Watering completed successfully!")
    print("")
    # 2. Irrigation with error
    print("Testing with error...")
    water_plants(plant_error)
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
