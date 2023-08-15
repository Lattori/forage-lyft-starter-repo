from Tire import tire_wear_array


class SpinderBattery:

    def __init__(self,battery,last_service_date):
        self.battery = battery
        super.__init__(last_service_date)

    def Battery_should_be_served(self,threeyear):
        if self.last_service_date > threeyear:
            self.needs_service()
