import Car
car = Car.Car(2025, "Lexus", 156)
for i in range (1,5):
    car.accelerate()
    speed = car.get_speed()
    print(speed)
for f in range (1,5):
    car.brake()
    speed = car.get_speed()
    print(speed)