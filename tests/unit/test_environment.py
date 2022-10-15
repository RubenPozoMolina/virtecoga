from virtecoga import Environment


class TestEnvironment:

    def test_environment(self):
        environment = Environment(
            size=(50, 50, 50),
            cycle_time=5
        )
        assert environment.cycle_time == 5
        assert environment.x == 50
        assert environment.y == 50
        assert environment.z == 50
