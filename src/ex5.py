from pprint import pprint

class Car:
    def __init__(self, car_id, miles, model) -> None:
        self.car_id = car_id
        self.miles = miles
        self.model = model
    
    def to_dict(self):
        return {"id": self.car_id, "miles": self.miles, "model": self.model}


def build_car_list():
    car_list = []
    with open("../files/input.txt", "r") as file, open("../files/car-ids.txt", "r") as file2:
        next(file)

        for row1, row2 in zip(file, file2):
            lst1 = row1.split(", ")
            lst2 = row2.split(", ")
            try:
                car_list.append(Car(int(lst1[0]), int(lst1[1]), lst2[1].strip()).to_dict())
            except:
                pass
    return car_list
    pass # TODO


def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
