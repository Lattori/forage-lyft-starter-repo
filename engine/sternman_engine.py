from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on,Battery):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on
        self.Battery = Battery

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return self.needs_service()
        else:
            return False

    def Battery_should_be_served(self,twoyear):
        if self.last_service_date > twoyear:
            self.needs_service()

