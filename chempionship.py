from driver import *

class Championship():
    def __init__(self) -> None:
        self.driveres = {}
    
    def createDriver(self, driver_name:Driver):
        driver = Driver(driver_name)
        self.driveres.update({driver : None})
        return self.driveres

    def getDrivers(self):
        return self.driveres
    
    def getDriver(self):
        for driver in self.driveres:
            if driver