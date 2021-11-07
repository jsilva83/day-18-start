import random as rnd


class Walker:

    DIRECTIONS = [90, 270, 0, 180]

    def __init__(self):
        return

    def chose_direction(self):
        return rnd.choice(self.DIRECTIONS)

    @staticmethod
    def chose_nr_steps():
        return rnd.randint(5, 10)
