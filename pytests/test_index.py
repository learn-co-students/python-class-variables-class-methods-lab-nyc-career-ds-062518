import pytest
from driver import Driver

def test_driver_class_vars():
    assert '_all' in Driver.__dict__.keys(), "The Driver class needs a class variable _all"
    assert '_count' in Driver.__dict__.keys(), "The Driver class needs a class variable _count"

def test_driver_class_init():
    driver_1 = Driver("Terrance", "Toyota", "Camry")
    driver_2 = Driver("Rachel", "Subaru", "Forrester")
    driver_3 = Driver("Jeff", "Toyota", "Camry")
    driver_4 = Driver("Lore", "Honda", "Pilot")
    assert Driver._all == [driver_1, driver_2, driver_3, driver_4], "Remember to keep track of all drivers that have been instantiated"
    assert Driver._count == 4

def test_fleet_size_class_method():
    assert "fleet_size" in Driver.__dict__.keys(), "Missing class method 'fleet_size' in the Driver class"
    assert Driver.fleet_size() == 4, "The fleet size should represent the total number of drivers in the Driver class"

def test_driver_names_class_method():
    assert "driver_names" in Driver.__dict__.keys(), "Missing class method 'driver_names' in the Driver class"
    assert Driver.driver_names() == ["Terrance", "Rachel", "Jeff", "Lore"]

def test_fleet_makes_class_method():
    assert "fleet_makes" in Driver.__dict__.keys(), "Missing class method 'fleet_makes' in the Driver class"
    assert Driver.fleet_makes() == ["Toyota", "Toyota", "Subaru", "Honda"]

def test_fleet_models_class_method():
    assert "fleet_models" in Driver.__dict__.keys(), "Missing class method 'fleet_models' in the Driver class"
    assert Driver.fleet_models() == ["Camry", "Camry", "Forrester", "Pilot"]

def test_fleet_makes_count_class_method():
    assert "fleet_makes_count" in Driver.__dict__.keys(), "Missing class method 'fleet_makes_count' in the Driver class"
    assert Driver.fleet_makes_count() == {'Honda': 1, 'Toyota': 2, 'Subaru': 1}

def test_fleet_models_count_class_method():
    assert "fleet_models_count" in Driver.__dict__.keys(), "Missing class method 'fleet_models_count' in the Driver class"
    assert Driver.fleet_models_count() == {'Pilot': 1, 'Camry': 2, 'Forrester': 1}

def test_percent_of_fleet_class_method():
    assert "percent_of_fleet" in Driver.__dict__.keys(), "Missing class method 'percent_of_fleet' in the Driver class"
    assert Driver.percent_of_fleet("Toyota") == "50.0%"
