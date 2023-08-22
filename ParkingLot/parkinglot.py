'''
- vehicle types
    - small, medium, large
- parking lot
    - lot types (s, m, l, hc)
    - add new car
    - remove car
    - payment
    - ticket
- payment
    - charge
    
    

'''
from Vehicle import SmallVehicle, MediumVehicle, LargeVehicle
import collections


class ParkingLot:
    def __init__(self) -> None:
        self.parkingLotDict = collections.defaultdict(int)
        self.licensePlates = {}

    def addCar(self, vehicleType):
        if vehicleType.vehicleType() in self.parkingLotDict and self.parkingLotDict[vehicleType.vehicleType()] >= 1:
            self.licensePlates[vehicleType.getVehicleDetails()] = vehicleType
        else:
            return "Parking lot full"

    def removeCar(self, licensePlate):
        if licensePlate in self.licensePlates:
            amount = self.licensePlates[licensePlate].parkingCharge()
            print("Your amount is: ", amount)

            vt = self.licensePlates[licensePlate]
            self.parkingLotDict[vt.vehicleType()]+=1
            del self.licensePlates[licensePlate]

            return "Please procced ahead."

        self.parkingLotDict[type]+=1

    def addCarTypeToParkingLot(self, type, count):
        if type not in self.parkingLotDict:
            self.parkingLotDict[type] = 0
        self.parkingLotDict[type] = count

pl = ParkingLot()
sv = SmallVehicle()
mv = MediumVehicle()
lv = LargeVehicle()

pl.addCarTypeToParkingLot("S", 20)
pl.addCarTypeToParkingLot("M", 30)
pl.addCarTypeToParkingLot("L", 50)

carType = "S"

if carType == "S":
    pl.addCar(SmallVehicle())
elif carType == "M":
    pl.addCar(MediumVehicle())
elif carType == "L":
    pl.addCar(LargeVehicle())
print(pl.licensePlates)