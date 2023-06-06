from time import sleep

from virtecoga.processor import Processor


class Environment:
    x = 0
    y = 0
    living_beings = []
    cycles = []
    cycle_time = 0
    running = False
    processor = None

    def __init__(self, size=(100, 100), cycle_time=1):
        self.x = size[0]
        self.y = size[1]
        self.cycle_time = cycle_time
        self.processor = Processor(self)

    def begin(self):
        self.running = False
        while self.running:
            sleep(self.cycle_time)

    def move(self, living_being, position):
        pass

    def eat(self, living_being, quantity, eat_filter):
        pass

    def reproduce(self, living_being, position, mutation_factor=0.001):
        pass

    def excrete(self, living_being, quantity, excrete_filter):
        pass

    def detect(self, living_being, condition):
        pass
