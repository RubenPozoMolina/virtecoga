from virtecoga import actions
from virtecoga.living_being import LivingBeing


class Processor:

    environment = None

    def __init__(self, environment):
        self.environment = environment

    def process_environment(self):
        for living_being in self.environment.living_beings:
            self.process_living_being(living_being)

    def process_living_being(self, living_being: LivingBeing):
        for line in living_being.content:
            self.process_line(living_being, line)

    @staticmethod
    def get_action(line):
        return_value = None
        action = line[0:3]
        if action.isnumeric():
            return_value = int(action)
        return return_value

    @staticmethod
    def get_position(line):
        x = 0
        y = 0
        x_string = line[3:6]
        y_string = line[6:9]
        if x_string.isnumeric():
            x = int(x_string)
        if y_string.isnumeric():
            y = int(y_string)
        return_value = (x, y)
        return return_value

    def process_line(self, living_being, line):
        if line.startswith(actions.MOVE):
            self.environment.move(living_being, position=self.get_position(line))
        elif line.startswith(actions.EAT):
            self.environment.eat(living_being, quantity=10, filter=None)
        elif line.startswith(actions.REPRODUCE):
            self.environment.reproduce(actions.REPRODUCE, position=self.get_position(line))
        elif line.startswith(actions.EXCRETE):
            self.environment.excrete(living_being, quantity=10, filter=None)
        elif line.startswith(actions.DETECT):
            self.environment.detect(living_being, condition=True)
