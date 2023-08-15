from abc import ABC

from car import Car


def create_palindrome(current_date, last_service_date, warning_light_on, current_mileage):
    Palindrome = CarFactory(current_date, last_service_date, warning_light_on, current_mileage)


def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    Rorschach = CarFactory(current_date, last_service_date, current_mileage, last_service_mileage)


def create_thovex(current_date, last_service_date, current_mileage, service_mileage):
    thovex = CarFactory(current_date, last_service_date, current_mileage, service_mileage)


def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    glissade = CarFactory(current_date, last_service_date, current_mileage, last_service_mileage)


def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    calliope = CarFactory(current_date, last_service_date, current_mileage, last_service_mileage)


class CarFactory:
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_on):
        self._current_date = current_date
        self._last_service_date = last_service_date
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on
        super.__init__(self._last_service_mileage, self._current_mileage, self._current_date, self._last_service_date)

    def set_current_date(self, current_date):
        self._current_date = current_date

    def set_last_service_date(self, last_service_date):
        self._last_service_date = last_service_date

    def set_current_mileage(self, current_milage):
        self._current_mileage = current_milage

    def set_warning_light_boolean(self, light=bool):
        self.warning_light_on = light

    def last_service_mileage(self, last_service_mileage):
        self._last_service_mileage = last_service_mileage

    def get_current_date(self):
        return self._current_date

    def get_last_service_date(self):
        return self.last_service_date

    def get_current_mileage(self):
        return self._current_mileage

    def get_last_service_mileage(self):
        return self._last_service_mileage

    def get_warning_light(self):
        return self.warning_light_on
