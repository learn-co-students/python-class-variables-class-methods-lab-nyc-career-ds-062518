class Driver:

    _all = []
    _count = 0

    def __init__(self, name, carMake, carModel):
        self._name = name
        self._car_make = carMake
        self._car_model = carModel
        Driver._all.append(self)
        Driver._count += 1

    @classmethod
    def all(cls):
        return cls._all


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def make(self):
        return self._car_make

    @make.setter
    def make(self, make):
        self._car_make= make

    @property
    def model(self):
        return self._car_model

    @model.setter
    def model(self, model):
        self._car_model = model

    @classmethod
    def fleet_size(cls):
        return cls._count

    @classmethod
    def driver_names(cls):
        return [driver.name for driver in cls.all()]
        # driver_list = []
        # for driver in cls._all:
        #     driver_list.append(driver['name'])
        # return driver_list

    @classmethod
    def fleet_makes(cls):
        return [driver.make for driver in cls.all()]


    @classmethod
    def fleet_models(cls):
        return [driver.model for driver in cls.all()]

    @classmethod
    def fleet_makes_count(cls):
        all_makes = set(cls.fleet_makes())
        histogram = dict.fromkeys(all_makes, 0)
        for driver in cls.fleet_makes():
            histogram[driver] += 1
        return histogram


    @classmethod
    def fleet_models_count(cls):
        all_models = set(cls.fleet_models())
        histogram = dict.fromkeys(all_models, 0)
        for driver in cls.fleet_models():
            histogram[driver] += 1
        return histogram

    @classmethod
    def percent_of_fleet(cls, car):
        num = float((cls.fleet_makes_count()[car])/ len(cls.all()))
        num_perc = round(num * 100, 3)
        return str(num_perc) + "%"


# import collections
# hist = collections.Counter(artists)
# histogram = dict.fromkeys(artists,0)
# set(histogram)
# for artist in artists:
#     histogram[artist] += 1
