class Vehicle:
    def start(self):
        print("Vehicle started.")

    def stop(self):
        print("Vehicle stopped.")


class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")


class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started.")

    def stop(self):
        print("Motorcycle stopped.")


vehicle = Vehicle()
vehicle.start()  # Output: Vehicle started
vehicle.stop()   # Output: Vehicle stopped

car = Car()
car.start()      # Output: Car started
car.stop()       # Output: Car stopped

motorcycle = Motorcycle()
motorcycle.start()  # Output: Motorcycle started
motorcycle.stop()   # Output: Motorcycle stopped
