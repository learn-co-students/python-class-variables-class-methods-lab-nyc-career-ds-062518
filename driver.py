class Driver:
    _all = []
    _count = 0

#Class Methods
    @classmethod
    def all(cls):
        return cls._all
    @classmethod
    def count(cls):
        return cls._count
    @classmethod
    def count_plus(cls):
        cls._count += 1
    @classmethod
    def fleet_size(cls):
        return len(cls.all())
    @classmethod
    def driver_names(cls):
        return [driver.name for driver in cls.all()]
    @classmethod
    def fleet_makes(cls):
        return [driver.car_make for driver in cls.all()]
    @classmethod
    def fleet_models(cls):
        return [driver.car_model for driver in cls.all()]
#see https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension for method on constructing these
#in dictionary comprehensions.
    @classmethod
    def fleet_makes_count(cls):
        temp_fleet_makes_count = {}
        for make in cls.fleet_makes():
            if make in temp_fleet_makes_count:
                temp_fleet_makes_count[make] += 1
            else:
                temp_fleet_makes_count[make] = 1
        return temp_fleet_makes_count
    @classmethod
    def fleet_models_count(cls):
        temp_fleet_models_count = {}
        for model in cls.fleet_models():
            if model in temp_fleet_models_count:
                temp_fleet_models_count[model] += 1
            else:
                temp_fleet_models_count[model] = 1
        return temp_fleet_models_count
    @classmethod
    def percent_of_fleet(cls, make):
        total_make = sum(Driver.fleet_makes_count().values())
        make_count = Driver.fleet_makes_count()[make]
        return str(round((make_count / total_make)*100, 2)) + '%'

    def __init__(self, name, car_make, car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model
        Driver.all().append(self)
        Driver.count_plus()

#Instance Methods
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self.name = name
    @property
    def car_make(self):
        return self._car_make
    @car_make.setter
    def car_make(self, car_make):
        self.car_make = car_make
    @property
    def car_model(self):
        return self._car_model
    @car_model.setter
    def car_model(self, car_model):
        self.car_model = car_model
