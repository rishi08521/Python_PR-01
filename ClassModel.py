# class ClassName:
# # Constructor
#  def _init_(self, attribute1, attribute2):
#   self.attribute1 = attribute1
#   self.attribute2 = attribute2

# # Method
# def method_name(self):
#   print(f"Attribute 1: {self.attribute1}, Attribute 2: {self.attribute2}")

# # Create an object
# obj = ClassName("Value1", "Value2")
# obj.method_name()

class Cars:
    def __init__(self, carName, carModel, carYear, carCompany):
        self.carName = carName
        self.carModel = carModel
        self.carYear = carYear
        self.carCompany = carCompany

    def carVersion(self):
        print(f"This car {self.carName} model version {self.carModel} was built in the year {self.carYear} by {self.carCompany}.")

# Create an object of the Cars class
car = Cars("BMW", "M2 & M4", 2025, "Germany")
car.carVersion()
