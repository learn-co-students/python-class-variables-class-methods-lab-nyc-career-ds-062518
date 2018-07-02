class Driver:
    _all = []
    _count = 0

    def __init__ (self, _name, _make, _model):
        self._name = _name
        self._make = _make
        self._model = _model
        Driver._all.append(self)
        Driver._count += 1

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def make(self):
        return self._make
    @make.setter
    def make(self, _make):
        self._make = _make

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, _model):
        self._model = _model

    @classmethod
    def fleet_size(cls):
        return cls._count

    @classmethod
    def driver_names(cls):
        return [driver._name for driver in cls._all]

    @classmethod
    def fleet_makes(cls):
        return [driver._make for driver in cls._all]

    @classmethod
    def fleet_models(cls):
        return [driver._model for driver in cls._all]

    @classmethod
    def fleet_makes_count(cls):
        make_list = cls.fleet_makes()
        return {make:make_list.count(make) for make in set(make_list)}

    @classmethod
    def fleet_models_count(cls):
        model_list = cls.fleet_models()
        return {model:model_list.count(model) for model in set(model_list)}

    @classmethod
    def percent_of_fleet(cls, _make):
        fleet_make_freq = cls.fleet_makes_count()
        fleet_count = fleet_make_freq[_make]
        percent = fleet_count / cls._count * 100
        return str(round(percent, 3)) + '%'
