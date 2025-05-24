import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from car import Car

def test_car_start():
    car = Car("Toyota", "Corolla", 2020)
    assert car.start() == "The 2020 Toyota Corolla is starting."