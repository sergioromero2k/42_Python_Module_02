def check_temperature(temp_str):
    """
    Validates the temperature input for the agricultural pipeline.
    """
    try:
        # Attemps to convert input to a float number
        temp = int(temp_str)
        # Checks if temperature is within reasonable range (0 to 40)
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
    except ValueError:
        # Handles cases where input is not a number
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def main():
    """
    Demonstrates the robust handling of different sensor inputs.
    """
    temp = input("Testing temperature: ")
    result = check_temperature(temp)
    print("=== Garden Temperature Checker ===")
    print("")
    if result is not None:
        print(f"Valid temperature returned: {result}")


if __name__ == "__main__":
    main()
