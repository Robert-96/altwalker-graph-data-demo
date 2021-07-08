import random


class ExampleModel:

    def v_start(self, data):
        data['number'] = random.random()

    def v_A(self, data):
        number = float(data['number'])

        print("Reached vertex `v_A` because {} is bigger than 0.5".format(number))

    def v_B(self, data):
        number = float(data['number'])

        print("Reached vertex `v_B` because {} is less than 0.5".format(number))

    def e_chose_A(self):
        pass

    def e_chose_B(self):
        pass

    def e_restart(self):
        pass
