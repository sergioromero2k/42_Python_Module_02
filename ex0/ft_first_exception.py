def check_temperature(temp_str):
    try:
        temp = int(temp_str)
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
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def main():
    temp = input("Testing temperature: ")
    resultado = check_temperature(temp)
    if resultado is not None:
        print(f"Valid temperature returned: {resultado}")


if __name__ == "__main__":
    main()
