"""
Simple garden management system demonstrating custom exceptions
and robus error handling with try/except/finally
"""


class ErrorAddPlant(Exception):
    # Raised when there is an issue adding a plant (empty name, duplicate)
    pass


class NotEnoughWater(Exception):
    # Raised when the water tank is empty during watering
    pass


class WaterLevelTooHigh(Exception):
    # Raised when a plant's water level is above the allowed maximum
    pass


class WaterLevelTooLow(Exception):
    # Raised when a plant's water level is below the allowed minimum
    pass


class SunLevelTooHigh(Exception):
    # Raised when a plant's sun level is above the allowed maximum
    pass


class SunLevelTooLow(Exception):
    # Raised when a plant's sun level is below the allowed minimum
    pass


class Garden:
    def __init__(self, name, level_water, level_sun):
        # Plant pbject with name, water level, and sun level
        self.name = name
        self.level_water = level_water
        self.level_sun = level_sun


class GardenManager:
    def __init__(self):
        # List to store plant objects
        self.plants = []
        # Water tank capacity
        self.tank = 10

    def add_plant(self, plant):
        # Check if plant name is valid
        if plant.name is None or plant.name == "":
            raise ErrorAddPlant("Plant name cannot be empty!")
        # Check for duplicate plant name
        for p in self.plants:
            if p.name == plant.name:
                raise ErrorAddPlant("Plant name is already in the garden.")
        # Add plant to garden list
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")

    def water_plant(self):
        try:
            print("Opening watering system")
            # Loop through each plant and water it
            for p in self.plants:
                # If tank is empty, raise an error
                if self.tank == 0:
                    raise NotEnoughWater("Not enough water in tank")

                # If plant already has too much water, raise an error
                if p.level_water >= 10:
                    raise WaterLevelTooHigh(
                        f"Water level {p.level_water} is too high (max 10)"
                    )

                # Otherwise, water the plant and decrease tank level
                self.tank -= 1
                p.level_water += 1
                print(f"Watering {p.name} - success")

        except NotEnoughWater as e:
            # Handle tank empty error
            print("Caught GardenError:", e)

        except WaterLevelTooHigh as e:
            # Handle plant water level too high
            print(f"Error watering plant: {e}")

        finally:
            # Always close watering system (cleanup)
            print("Closing watering system (cleanup)")

    def health_plant(self):
        try:
            print("")
            print("Checking plant health...")
            for p in self.plants:
                try:
                    # Check water level
                    if p.level_water < 0:
                        raise WaterLevelTooLow(
                            f"Water level {p.level_water} is too low (min 0)"
                        )
                    if p.level_water >= 10:
                        raise WaterLevelTooHigh(
                            f"Water level {p.level_water} is too high (max 10)"
                        )

                    # Check sun level
                    if p.level_sun < 0:
                        raise SunLevelTooLow(
                            f"Sun level {p.level_sun} is too low (min 0)"
                        )
                    if p.level_sun >= 10:
                        raise SunLevelTooHigh(
                            f"Sun level {p.level_sun} is too high (max 10)"
                        )

                    # If all values are correct, the plant is healthy
                    print(
                        f"{p.name}: healthy (water: {p.level_water}, "
                        f"sun: {p.level_sun})"
                    )
                except (
                    WaterLevelTooLow,
                    WaterLevelTooHigh,
                    SunLevelTooHigh,
                    SunLevelTooLow,
                ) as e:
                    # Handle any plant health errors
                    print(f"Error checking {p.name}: {e}")
        finally:
            # Final message after health check
            print("")
            print("Garden management system test complete!")


def main():
    manager = GardenManager()

    print("=== Garden Management System ===")
    print("")
    print("Adding plants to garden...")
    try:
        # Add plants to the garden
        manager.add_plant(Garden("tomato", 5, 8))
        manager.add_plant(Garden("lettuce", 9, 7))
        manager.add_plant(Garden("", 2, 3))
    except ErrorAddPlant as e:
        # Handle add plant errors
        print("Error adding plant:", e)
    print("")
    print("Watering plants...")
    manager.water_plant()
    print("")
    print("Checking plant health...")
    manager.health_plant()


if __name__ == "__main__":
    main()
