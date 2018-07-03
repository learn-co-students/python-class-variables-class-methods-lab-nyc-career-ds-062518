class Driver:

    _all = []

    _count = 0

    def __init__(self, name, car_make, car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model
        Driver._all.append(self)
        Driver._count = Driver._count + 1

    #classmethods
    @classmethod
    def fleet_size(cls):
        return cls._count

    @classmethod
    def driver_names(cls):
        list_drivers = [driver._name for driver in cls._all]
        return list_drivers

    @classmethod
    def fleet_makes(cls):
        car_makes = [driver._car_make for driver in cls._all]
        return car_makes

    @classmethod
    def fleet_models(cls):
        car_models = [driver._car_model for driver in cls._all]
        return car_models

    @classmethod
    def fleet_makes_count(cls):
        fleet_makes_histo = {}
        local_fleet_makes = cls.fleet_makes()#[x._car_make for x in cls._all]
        for y in local_fleet_makes:
            fleet_makes_histo[y] = fleet_makes_histo.get(y, 0) + 1
        return fleet_makes_histo

    @classmethod
    def fleet_models_count(cls):
        fleet_models_histo = {}
        local_fleet_models = cls.fleet_models()#[x._car_make for x in cls._all]
        for y in local_fleet_models:
            fleet_models_histo[y] = fleet_models_histo.get(y, 0) + 1
        return fleet_models_histo

    @classmethod
    def percent_of_fleet(cls, car_make):
        total_cars = cls._count
        local_fleet = cls.fleet_makes_count()
        car_by_cars = round(float((local_fleet[car_make]/total_cars)*100), 3)
        return str(car_by_cars) + "%"

    #then we need to divide the number we want from the total number
    #then we need to multiple by 100
    #then we also need to use float() to get the number as a float
    #it's possible we can use round in the same step
    #then we need to use str() to convet it back to a string
    #and then return it after concatenating the string with %







    #decorarors for _name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    #decorarors for _car_make
    @property
    def car_make(self):
        return self._car_make

    @car_make.setter
    def car_make(self, car_make):
        self._car_make = car_make


    #decorarors for _car_model
    @property
    def car_model(self):
        return self._car_model

    @car_model.setter
    def car_model(self, car_model):
        self._car_model = car_model



    #return all driver objects
    @classmethod
    def all(cls):
        return cls._all

    #return count of number of driver objects
    @classmethod
    def count(cls):
        return cls._count
