from cars import *


def _main():
    for machine in get_car_list():
        if machine.car_type == 'car':
            print(machine.passenger_seats_count)
        elif machine.car_type == 'truck':
            print(machine.get_body_volume())
        elif machine.car_type == 'spec_machine':
            print(machine.extra)


if __name__ == '__main__':
    _main()