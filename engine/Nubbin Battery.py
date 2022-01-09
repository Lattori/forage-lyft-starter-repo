class NubbinBattery:
    def __init__(self,battery,last_service_date):
        self.battery = battery
        super.__init__(last_service_date)

    def Battery_should_be_served(self,fouryear):
        if self.last_service_date > fouryear:
            self.needs_service()
