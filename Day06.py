# Assignment 1
import re


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


class Patient:
    _patient_counter = 0

    @classmethod
    def get_total_patients(cls):
        return cls._patient_counter

    @staticmethod
    def validate_dob_format(dob_str):
        pattern = re.match(
            pattern=r"(?P<Year>\d{4})-(?P<Month>\d{2})-(?P<Day>\d{2})", string=dob_str
        )
        if pattern is None:
            return False
        return True

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        Patient._patient_counter += 1
        self.patient_id = f"PAT-{1000 + Patient._patient_counter}"

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, value):
        if Patient.validate_dob_format(value):
            self._dob = value
        else:
            raise ValueError(
                f"Invalid date of birth format: '{value}'. Expected YYYY-MM-DD.")

    pass

# Assignment 5


class Notifier:
    def __init__(self, **kwargs):
        self.sender_id = kwargs.get("sender_id")

    def send(self, message: str):
        return [f"[Notifier {self.sender_id}] general broadcast: {message}"]


class EmailNotifier(Notifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.email_server = kwargs.get("email_server")

    def send(self, message):
        email_log = [f"[Email via {self.email_server}] sending: {message}"]
        return email_log + super().send(message)


class SMSNotifier(Notifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sms_gateway = kwargs.get("sms_gateway")

    def send(self, message):
        sms_log = [f"[SMS via {self.sms_gateway}] sending: {message}"]
        return sms_log + super().send(message)


class HybridAlertChannel(EmailNotifier, SMSNotifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send(self, message):
        return [f"[HYBRID ALERT] Initiating dual channels..."] + super().send(message)

# Assignment 6


class DatabaseRecord:
    def __init__(self, **kwargs):
        self.record_id = kwargs.get("record_id")
        self.data = kwargs.get("data")

    def __repr__(self):
        return f"Record(id=<{self.record_id}>, data=<{self.data}>)"

    def __str__(self):
        return f"Record(id=<{self.record_id}>, data=<{self.data}>)"


class ResultSetIterator:
    _index_counter = 0

    def __init__(self, **kwargs):
        records_list = kwargs.get("records_list")
        if (isinstance(list, records_list) and all(isinstance(r, DatabaseRecord) for r in records_list)):
            self.records_list = records_list
        else:
            raise TypeError(
                "`records_list` shall be list of `DatabaseRecord` instances")
        # ResultSetIterator._index_counter += 1

    def __iter__(self):
        # records_list = self.kwargs.get("records_list")
        # for i in self.records_list:
        #     yield i
        return self

    def __next__(self):
        if ResultSetIterator._index_counter >= len(self.records_list):
            raise StopIteration
        record = self.records_list[ResultSetIterator._index_counter]
        ResultSetIterator._index_counter += 1
        return record


class DatabaseResultSet:
    def __init__(self):
        pass


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
    # Assignment 4
        # 1. Valid Registration
    p1 = Patient("Arham Khan", "1999-05-15")
    print(p1.patient_id)  # Output: PAT-1001

    # 2. Invalid DOB registration (throws ValueError)
    try:
        p2 = Patient("Lisa", "12/08/1998")
    except ValueError as e:
        # Output: Invalid date of birth format: '12/08/1998'. Expected YYYY-MM-DD.
        print(e)

    print(Patient.get_total_patients())  # Output: 1

    print("+"*80)

    # Assignment 5
    alert = HybridAlertChannel(
        sender_id="SYS-ADMIN", email_server="smtp.cdac.in", sms_gateway="gw.acts.com")

    logs = alert.send("Disk space 95%")

    for log in logs:
        print(log)


main()
