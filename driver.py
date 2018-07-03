class Driver:

    _all = []
    _count = 0

    def __init__(self, name, car_make, car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model
        Driver._all.append(self)
        Driver._count += 1

    @classmethod
    def fleet_size(cls):
        return Driver._count

    @classmethod
    def driver_names(cls):
        return [driver._name for driver in Driver._all]

    @classmethod
    def fleet_makes(cls):
        return [driver._car_make for driver in Driver._all]

    @classmethod
    def fleet_models(cls):
        return [driver._car_model for driver in Driver._all]

    @classmethod
    def fleet_makes_count(cls):
        dict = {}
        for driver in Driver._all:
            if driver._car_make in dict.keys():
                dict[driver._car_make] += 1
            else:
                dict.update({driver._car_make: 1})
        return dict

    @classmethod
    def fleet_models_count(cls):
        dict = {}
        for driver in Driver._all:
            if driver._car_model in dict.keys():
                dict[driver._car_model] += 1
            else:
                dict.update({driver._car_model: 1})
        return dict

    @classmethod
    def percent_of_fleet(cls, make):
        float = round(100 * Driver.fleet_makes_count()[make] / Driver._count, 2)
        return str(float) + '%'
