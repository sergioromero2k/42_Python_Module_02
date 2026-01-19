class GardenError(Exception):
    """
    Base excpetion class for all garden-related errors.
    """
    pass


class PlantError(GardenError):
    """
    Exception raised for issues specifically related to plants.
    """
    pass


class WaterError(GardenError):
    """
    Exception raised fot issues related to the irrigation system.
    """
    pass


# Vali datasets for verification
plants = {
    "Roses",
    "Tulips",
    "Sunflowers"
}

waters = {
    "Drip Irrigation",
    "Sprinkler Irrigation",
    "Surface Irrigation",
    "Subsurface Irrigation",
    "Flood Irrigation"
}


def verify_plant(plant: str) -> bool:
    """
    Checks if the selected irrigation method is available
    """
    if plant not in plants:
        raise PlantError(f"The {plant} plant is wilting!")
    return True


def verify_water(water: str) -> bool:
    """
    Checks if the selected irrigation method is available
    """
    if water not in waters:
        raise WaterError("Not enough water in the tank!")
    return True


def main():
    """
    Main demonstration of custom error handling and inheritance
    """
    plant = "tomato"
    water = "Manual Bucket"

    print("=== Custom Garden Errors Demo ===")
    print("")
    # Specific catch for PlantError
    print("Testing PlantError...")
    try:
        verify_plant(plant)
    except PlantError as e:
        print("Caught PlantError:", e)
    print("")
    # Specific catch for WaterError
    print("Testing WaterError...")
    try:
        verify_water(water)
    except WaterError as e:
        print("Caught WaterError:", e)
    print("")
    # Catching multiple types using the base class (Polymorphism)
    print("Testing catching all garden errors…")
    try:
        verify_plant(plant)
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        verify_water(water)
    except GardenError as e:
        print("Caught a garden error:", e)

    print("")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
