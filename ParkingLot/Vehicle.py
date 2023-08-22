from abc import ABC, abstractmethod
from datetime import datetime

class Vehicle(ABC):
    def __init__(self) -> None:
        self.licensePlate = ""
        self.entryTime = ""
        self.assignedLot = 0
    
    @abstractmethod
    def vehicleType():
        pass

    def assignTicket(self):
        self.entryTime = datetime.utcnow()
    
    @abstractmethod
    def parkingCharge(self):
        pass

    def getVehicleDetails(self):
        self.licensePlate = "XXO"
        self.assignTicket()
        return self.licensePlate

class SmallVehicle(Vehicle):
    def vehicleType(self):
        return "S"
    
    def parkingCharge(self):
        timeDiff = datetime.utcnow() - self.entryTime
        if timeDiff < 2:
            return 3
        else:
            return 10

class MediumVehicle(Vehicle):
    def vehicleType(self):
        return "M"
    
    def parkingCharge(self):
        timeDiff = datetime.utcnow() - self.entryTime
        if timeDiff < 2:
            return 5
        else:
            return 15

class LargeVehicle(Vehicle):
    def vehicleType(self):
        return "L"
    
    def parkingCharge(self):
        timeDiff = datetime.utcnow() - self.entryTime
        if timeDiff < 2:
            return 9
        else:
            return 23