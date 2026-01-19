def garden_operations():
    """
    Defines several internal functions that trigger common Python errors.
    """
    def v_err():
        # ValueError: Occurs when the type is correct but the value
        # is inappropriate
        int("abc")

    def z_err():
        # ZeroDivisionError: Mathematical error when dividing by zero
        10 / 0

    def f_err():
        # FileNotFountError: Attempt to open a file that doesn't exist
        # on the system
        open("missing.txt")

    def k_err():
        # KeyError: Attempt to access a key that doesn't exist in a dictionary
        {"tomato": 5}["missing_plant"]

    return v_err, z_err, f_err, k_err


def test_error_types():
    """
    Tests and handles different exception types to ensure system stability.
    """
    v_err, z_err, f_err, k_err = garden_operations()

    # Individual try-except blocks for each error type
    try:
        v_err()
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()")
        print("")
    try:
        z_err()
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero")
        print("")

    try:
        f_err()
    except FileNotFoundError:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print("")

    try:
        k_err()
    except KeyError:
        print("Testing KeyError...")
        print("Caught KeyError: 'missing\\_plant'")
        print("")

    try:
        v_err()
        z_err()
        f_err()
        k_err()
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!")
        print("")

    print("All error types tested successfully!")


def main():
    """
    Main entry point for the error types demonstration.
    """
    print("=== Garden Error Types Demo ===")
    print("")
    garden_operations()
    test_error_types()


if __name__ == "__main__":
    main()
