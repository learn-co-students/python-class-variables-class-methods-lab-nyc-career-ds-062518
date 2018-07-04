from collections import Counter
class Driver:
    _all = []
    _count= 0

    def __init__(self, name, car_make, car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model
        Driver._all.append(self)
        Driver._count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def car_make(self):
        return self._car_make

    @car_make.setter
    def car_make(self,car_make):
        self._car_make = car_make

    @property
    def car_model(self):
        return self._car_model

    @car_model.setter
    def car_model(self, car_model):
        self._car_model= car_model

    @classmethod
    def fleet_size(cls):
        return cls._count

    @classmethod
    def driver_names (cls):
        name_list= []
        for name in cls._all:
            name_list.append(name._name)
        return name_list

    @classmethod
    def fleet_makes (cls):
        fleet_list= []
        for fleet in cls._all:
            fleet_list.append(fleet.car_make)
        return fleet_list

    @classmethod
    def fleet_models (cls):
        fleet_models= []
        for driver in cls._all:
            fleet_models.append(driver.car_model)
        return fleet_models

    @classmethod
    def fleet_makes_count(cls):
        fleet_list_count= []
        for fleet in cls._all:
            fleet_list_count.append(fleet.car_make)
        fleet_count = dict(Counter(fleet_list_count))
        return fleet_count

    @classmethod
    def fleet_models_count(cls):
        fleet_models_count= []
        for fleet_models in cls._all:
            fleet_models_count.append(fleet_models.car_model)
        model_count = dict(Counter(fleet_models_count))
        return model_count

    @classmethod
    def percent_of_fleet (cls,car_make):
        num = str(100*(cls.fleet_makes_count()[car_make]/cls.fleet_size()))
        return num + "%"
