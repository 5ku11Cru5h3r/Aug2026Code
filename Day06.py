# Assignment 1
class SmartThermostat:
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0

    def __init__(self, appliance_name: float, initial_temp: float):
        self.__appliance_name = appliance_name
        self.__target_temp = initial_temp
        pass

    @property
    def target_temp(self):
        return self.__target_temp

    @target_temp.setter
    def target_temp(self, temperature):
        if (isinstance(temperature, (float, int)) == False):
            raise TypeError("Give a float or int in temperature")
        if (SmartThermostat.MAX_TEMP < temperature or SmartThermostat.MIN_TEMP > temperature):
            self.__target_temp = 22.0
            raise ValueError(
                f"`initial_temp` is out of the `[{SmartThermostat.MIN_TEMP, SmartThermostat.MAX_TEMP}]` bounds, it defaults to `22.0`")
        self.__target_temp = temperature

    @property
    def appliance_name(self):
        return self.__appliance_name

    # @appliance_name.setter
    # def appliance_name(self, *args):
    #     self.__appliance_name = args[0]


# Assignment 2
class Vehicle:
    def __init__(self, make: str, model: str, fuel_capacity: float):
        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity
        pass

    def calculate_range(self, fuel_efficiency):
        return self.fuel_capacity * fuel_efficiency

    def get_description(self):
        return f"Vehicle: {self.make} {self.model}"


class DeliveryTruck(Vehicle):
    def __init__(self, make, model, fuel_capacity, cargo_load):
        super().__init__(make, model, fuel_capacity)
        self.cargo_load = cargo_load

    def calculate_range(self, fuel_efficiency):
        return super().calculate_range(fuel_efficiency)*(1 - (self.cargo_load * 0.1))

    def get_description(self):
        return f"Truck: <{self.make}> <{self.model}> carrying {self.cargo_load} tons"


# Assignment 3
class PriceAmount:
    def __init__(self, value, currency: str):
        self.value = value
        self.currency = currency.upper()
        pass

    def __str__(self):
        return f'<{self.currency}> <{self.value:.2f}>'

    def __repr__(self):
        return f"PriceAmount(value=<{self.value}>, currency='<{self.currency}>')"

    def __add__(self, other):
        if (isinstance(other, PriceAmount) == False):
            raise TypeError(
                "Cannot add PriceAmount Object with (any) other object")
        if (isinstance(other, PriceAmount) == True and self.currency != other.currency):
            raise ValueError(
                f"Cannot add price amounts with different currencies: '<{self.currency}>' and '<{other.currency}>")
        return PriceAmount(self.value+other.value, self.currency)

    def __eq__(self, other):
        if (self.value == other.value and self.currency == other.currency):
            return True
        return False

# Assignment 4


def main():
    # Assignment 1
    thermostat = SmartThermostat("Living Room AC", 24.0)
    print(thermostat.appliance_name)  # Output: Living Room AC
    print(thermostat.target_temp)     # Output: 24.0

    thermostat.target_temp = 28.0     # Updates successfully
    print(thermostat.target_temp)     # Output: 28.0

    try:
        thermostat.target_temp = 5.0  # Out of range!
    except ValueError as e:
        print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.

    # Assignment 2
    truck = DeliveryTruck("Volvo", "FH16", 300.0, cargo_load=2.0)

    # Base range calculations without load adjustment would be 300 * 5 = 1500 km.
    # 2.0 tons load reduces range by 20% (10% * 2) -> 1500 * 0.8 = 1200 km.
    print(truck.calculate_range(5.0))  # Output: 1200.0
    print(truck.get_description())

    # Assignment 3
    p1 = PriceAmount(19.99, "usd")

    p2 = PriceAmount(10.01, "USD")
    p3 = PriceAmount(15.00, "EUR")

    print(str(p1))      # Output: USD 19.99
    print(repr(p1))     # Output: PriceAmount(value=19.99, currency='USD')

    total = p1 + p2
    print(str(total))   # Output: USD 30.00

    print(p1 == PriceAmount(19.99, "USD"))  # Output: True

    try:
        bad_addition = p1 + p3
    except ValueError as e:
        print(e)


main()
