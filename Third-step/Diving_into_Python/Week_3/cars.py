import csv
import os.path

EXTENSIONS = ['.jpeg', '.jpg', '.png', '.gif']


class UndefinedExtension(Exception):
    """Exception about an undefined extension"""


class CarBase:
    @staticmethod
    def get_photo_file_ext(photo_file_name):
        return os.path.splitext(photo_file_name)[1]

    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        try:
            if self.get_photo_file_ext(photo_file_name) != '':
                self.photo_file_name = self.get_photo_file_ext(photo_file_name)
            else:
                raise UndefinedExtension
        except UndefinedExtension:
            print("There's not such extension like:", self.get_photo_file_ext(photo_file_name) or None)
        self.brand = brand
        self.carrying = carrying


class Car(CarBase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name, carrying):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, body_whl, carrying):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = [float(i) for i in body_whl.split('x')]
        if self.body_length == '' or self.body_width == '' or self.body_height == '':
            self.body_length, self.body_width, self.body_height = 0, 0, 0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list():
    lst = []
    with open('_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if row:
                if row[0] == 'car' and row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[5] != '':
                    lst.append(Car(row[0], row[1], row[2], row[3], row[5]))
                elif row[0] == 'truck' and row[0] != '' and row[1] != '' and row[3] != '' and row[4] != '' and row[5] != '':
                    lst.append(Truck(row[0], row[1], row[3], row[4], row[5]))
                elif row[0] == 'spec_machine' and row[0] != '' and row[1] != '' and row[3] != '' and row[5] != '' and \
                        row[6] != '':
                    lst.append(SpecMachine(row[0], row[1], row[3], row[5], row[6]))
    return lst