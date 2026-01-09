def garden_operations():
    def v_err():
        int("abc")

    def z_err():
        10 / 0

    def f_err():
        open("missing.txt")

    def k_err():
        {"tomato": 5}["missing_plant"]

    return v_err, z_err, f_err, k_err


def test_error_types():
    v_err, z_err, f_err, k_err = garden_operations()
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
    print("=== Garden Error Types Demo ===")
    print("")
    garden_operations()
    test_error_types()


if __name__ == "__main__":
    main()
