import threading
from time import sleep

from virtecoga import LivingBeing
from virtecoga.position import Position
from virtecoga.processor import Processor

DEFAULT_MAX_X = 100
DEFAULT_MAX_Y = 100


class Environment:
    x = 0
    y = 0
    living_being_index = 0
    living_beings = []
    cycles = []
    cycle_time = 0
    running = False
    processor = None
    running_thread = None

    def __init__(self, size=(DEFAULT_MAX_X, DEFAULT_MAX_Y), cycle_time=1):
        self.x = size[0]
        self.y = size[1]
        self.cycle_time = cycle_time
        self.processor = Processor(self)

    def run(self):
        self.running = True
        while self.running:
            sleep(self.cycle_time)

    def begin(self):
        self.running_thread = threading.Thread(target=self.run)
        self.running_thread.start()

    def end(self):
        self.running = False
        self.running_thread.join()

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

    def get_index(self):
        self.living_being_index += 1
        return self.living_being_index

    def verify_position(self, position: Position):
        return_value = False
        if isinstance(position.x, int) and isinstance(position.y, int):
            if 0 <= position.x < self.x:
                if 0 <= position.y < self.y:
                    return_value = True
        return return_value

    def add(self, position: Position, content):
        code = None
        if self.verify_position(position):
            code = self.get_index()
            living_being = LivingBeing(
                code=code,
                position=position,
                content=content
            )
            self.living_beings.append(living_being)
        return code

    def get(self, code) -> LivingBeing:
        return_value = None
        for living_being in self.living_beings:
            if living_being.code == code:
                return_value = living_being
                break
        return return_value
