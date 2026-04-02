
from Citizen import Citizen
from Driving_License import Driving_License


class Driving_Citizen(Driving_License, Citizen):
    def __init__(self, id, last_name, middle_name, first_name, hometown, living_area,
                 driving_license_id, driving_license_type):
        Citizen.__init__(self, id, last_name, middle_name, first_name, hometown, living_area)
        self.driving_license_id = driving_license_id
        self.driving_license_type = driving_license_type

    def vehicle_type(self):
        vehicle = []

        if 'A' in self.driving_license_type:
            vehicle.append("Motorbike")

        if 'B' in self.driving_license_type:
            vehicle.append("Car")

        if 'C' in self.driving_license_type:
            vehicle.append("Car")
            vehicle.append("Bus")

        if 'D' in self.driving_license_type:
            vehicle.append("Car")
            vehicle.append("Bus")
            vehicle.append("Truck")

        return vehicle
