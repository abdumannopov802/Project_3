class Driver():
    def __init__(self, name) -> None:
        self.driver_name = name
    
    @property
    def driverName(self):
        return self.driver_name

    def __str__(self) -> str:
        return self.driver_name
        
    def getName(self):
        return self.driver_name
    
