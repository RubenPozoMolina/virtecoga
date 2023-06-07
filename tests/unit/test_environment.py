from virtecoga import Environment


class TestEnvironment:

    def test_environment(self):
        environment = Environment(
            size=(50, 50),
            cycle_time=5
        )
        assert environment.cycle_time == 5
        assert environment.x == 50
        assert environment.y == 50

    def test_environment_get(self):
        environment = Environment(
            size=(50, 50),
            cycle_time=5
        )
        living_being_code = environment.add((1, 1), '')
        living_being = environment.get(living_being_code)
        assert living_being.code == living_being_code
        assert living_being.position == (1, 1)
        assert living_being.content == ''
