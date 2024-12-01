class FuelStation:
    def __init__(self, diesel: int = 2, petrol: int = 2, electric: int = 1):
        """
        Initializes the FuelStation with the maximum number of slots for each fuel type.
        Args:
        - diesel (int): Number of diesel fuel slots (default 2).
        - petrol (int): Number of petrol fuel slots (default 2).
        - electric (int): Number of electric vehicle slots (default 1).
        """
        self.max_slot = {"diesel": diesel, "petrol": petrol, "electric": electric}
        self.curr_slot = {"diesel": 0, "petrol": 0, "electric": 0}

    def fuel_vehicle(self, fuel_type: str) -> bool:
        """
        Fuels a vehicle if there is an available slot for the given fuel type.
        Args:
        - fuel_type (str): The type of fuel ("diesel", "petrol", or "electric").
        Returns:
        - bool: True if the vehicle is fueled; False otherwise.
        """
        if fuel_type not in self.max_slot:
            return False  # Invalid fuel type

        if self.curr_slot[fuel_type] < self.max_slot[fuel_type]:
            self.curr_slot[fuel_type] += 1
            return True
        return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        """
        Opens a fuel slot for the given fuel type.
        Args:
        - fuel_type (str): The type of fuel ("diesel", "petrol", or "electric").
        Returns:
        - bool: True if a slot is successfully opened; False otherwise.
        """
        if fuel_type not in self.curr_slot:
            return False  # Invalid fuel type

        if self.curr_slot[fuel_type] > 0:
            self.curr_slot[fuel_type] -= 1
            return True
        return False


# Testing the FuelStation
output = []
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

# Test cases
output.append(fuel_station.fuel_vehicle("diesel"))  # True
output.append(fuel_station.fuel_vehicle("petrol"))  # True
output.append(fuel_station.fuel_vehicle("diesel"))  # True
output.append(fuel_station.fuel_vehicle("electric"))  # True
output.append(fuel_station.fuel_vehicle("diesel"))  # False
output.append(fuel_station.open_fuel_slot("diesel"))  # True
output.append(fuel_station.fuel_vehicle("diesel"))  # True
output.append(fuel_station.open_fuel_slot("electric"))  # True
output.append(fuel_station.open_fuel_slot("electric"))  # False

print(output)  # Expected: [True, True, True, True, False, True, True, True, False]
