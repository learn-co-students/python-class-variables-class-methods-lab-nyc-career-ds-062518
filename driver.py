class Driver:
    _all=[]
    _allnames = []
    _count = 0
    _list_of_fleet_makes = []
    _list_of_fleet_models = []

    def __init__(self, name, car_make, car_model):
        self._name= name
        self._car_make= car_make
        self._car_model= car_model
        Driver._all.append(self)
        Driver._allnames.append(self._name)
        Driver._count += 1
        Driver._list_of_fleet_makes.append(self._car_make)
        Driver._list_of_fleet_models.append(self._car_model)

    @classmethod
    def fleet_size(cls):
        return Driver._count

    @classmethod
    def driver_names(cls):
        return Driver._allnames

    @classmethod
    def fleet_makes(cls):
        return Driver._list_of_fleet_makes

    @classmethod
    def fleet_models(cls):
        return Driver._list_of_fleet_models

    @classmethod
    def fleet_makes_count(cls):
        fleetmakelist= cls.fleet_makes()
        import collections
        fleethist = collections.Counter(fleetmakelist)
        fleethistogram = dict.fromkeys(fleetmakelist, 0)
        count = 0
        for fleetmake in fleetmakelist:
            fleethistogram[fleetmake] += 1
        return fleethistogram

    @classmethod
    def fleet_models_count(cls):
        fleetmodelslist= cls.fleet_models()
        import collections
        modelhist = collections.Counter(fleetmodelslist)
        modelhistogram = dict.fromkeys(fleetmodelslist, 0)
        count = 0
        for fleetmodel in fleetmodelslist:
            modelhistogram[fleetmodel] += 1
        return modelhistogram

    @classmethod
    def percent_of_fleet(cls, make):
        totalcars= sum(Driver.fleet_makes_count().values())
        tper = Driver.fleet_makes_count()[make]/  totalcars
        percent = str(float((tper)*100)) +'%'
        return percent
