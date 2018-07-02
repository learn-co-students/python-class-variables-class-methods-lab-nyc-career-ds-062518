class Driver:
    _all = []
    _count =0

    def __init__(self, name, car_make, model):
        self._name = name
        self._car_make = car_make
        self._model = model
        Driver._all.append(self)
        Driver._count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def car_make(self):
        return self._car_make

    @car_make.setter
    def car_make(self, car_make):
        self._car_make = car_make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @classmethod
    def fleet_size(cls):
        return cls._count

    @classmethod
    def driver_names(cls):
        return [driver.name for driver in cls._all]

    @classmethod
    def fleet_makes(cls):
        return [driver.car_make for driver in cls._all]

    @classmethod
    def fleet_models(cls):
        return [driver.model for driver in cls._all]

    @classmethod
    def fleet_makes_count(cls):
        make_list = cls.fleet_makes()
        return {make: make_list.count(make) for make in set(make_list)}

    @classmethod
    def fleet_models_count(cls):
        model_list = cls.fleet_models()
        return {model: model_list.count(model) for model in set(model_list)}

    @classmethod
    def percent_of_fleet(cls, make):
        fleet_make_freq = cls.fleet_makes_count()
        fleet_count = fleet_make_freq[make]
        percent = str(round(((fleet_count/cls._count)*100),3))
        return percent+'%'
