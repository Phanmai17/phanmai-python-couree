#แนวทางการแก้ปัญหาเกี่ยวกับรถยนต์
class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    vehicle_type = "Car"
    
    #ข้อมูลที่จะต้องใช้ในโปรแกรมนี้
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
    
    #โปรแกรมนี้จะทำอะไรได้บ้าง
    def drive(self, distance):
        """Method to update mileage"""
        self.mileage += distance
        return f"Drove {distance} km. Total mileage: {self.mileage} km"
    
    def get_info(self):
        """Method to get car information"""
        return f"{self.year} {self.brand} {self.model} - Mileage: {self.mileage} km"
    
    @classmethod
    def get_vehicle_type(cls):
        """Class method to access class attributes"""
        return cls.vehicle_type

# Creating instances การสร้างวัตถุ(การปั้ม)
car1 = Car("Toyota", "Camry", 2022) # car1 จะมี brand,model,year,mileage,drive(),get_info()
car2 = Car("Honda", "Civic", 2021)

# Accessing class attributes
print(f"All cars have {Car.wheels} wheels")
print(f"Vehicle type: {Car.get_vehicle_type()}")

# Accessing instance attributes
print(car1.get_info()) # 2022 Toyota Camry - mileage : 100 km
print(car2.get_info())

# Using methods
print(car1.drive(100)) #mileage += 100 => 100
print(car2.drive(250))

print(car1.drive(200)) #mileage ของ car1 ตอนนี้เท่าไหร่