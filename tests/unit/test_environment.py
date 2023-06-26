import json
import pytest
from virtecoga import Environment
from virtecoga.position import Position

MAX_X = 50
MAX_Y = 50
CYCLE_TIME = 5

position_values = [
    {"x": 0, "y": 0, "result": True},
    {"x": MAX_X - 1, "y": MAX_Y - 1, "result": True},
    {"x": -1, "y": 0, "result": False},
    {"x": 0, "y": -1, "result": False},
    {"x": MAX_X, "y": 0, "result": False},
    {"x": 0, "y": MAX_Y, "result": False},
    {"x": "a", "y": 0, "result": False},
    {"x": 0, "y": "a", "result": False}
]

with open('tests/data/beings.json', 'r') as f:
    beings_values = json.load(f)


@pytest.fixture(scope="module")
def environment():
    local_environment = Environment(
        size=(MAX_X, MAX_Y),
        cycle_time=CYCLE_TIME
    )
    yield local_environment


class TestEnvironment:

    def test_environment(self, environment):
        assert environment.cycle_time == CYCLE_TIME
        assert environment.x == MAX_X
        assert environment.y == MAX_Y

    @pytest.mark.parametrize('value', position_values)
    def test_verify_position_ok(self, environment, value):
        position = Position(value['x'], value['y'])
        return_value = environment.verify_position(position)
        assert return_value == value['result']

    @pytest.mark.parametrize('value', beings_values)
    def test_environment_add(self, environment, value):
        position = Position(value['position']['x'], value['position']['y'])
        content = value['content']
        living_being_code = environment.add(position, content)
        assert living_being_code == value['result']['code']
