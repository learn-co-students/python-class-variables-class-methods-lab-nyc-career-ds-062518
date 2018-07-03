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
        car_makes_hist = {driver._car_make: 0 for driver in Driver._all}
        for driver in Driver._all:
            car_makes_hist[driver._car_make] +=1
        return car_makes_hist

    @classmethod
    def fleet_models_count(cls):
        car_models_hist = {driver._car_model: 0 for driver in Driver._all}
        for driver in Driver._all:
            car_models_hist[driver._car_model] +=1
        return car_models_hist
    @classmethod
    def percent_of_fleet(cls, car_make):
        for driver in Driver._all:
            percent = round(float((Driver.fleet_makes_count()[car_make]/ Driver.fleet_size())*100),3)
            return str(percent) + '%'
