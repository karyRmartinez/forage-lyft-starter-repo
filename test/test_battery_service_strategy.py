import unittest
from battery_service_strategy import BatteryServiceStrategy

class TestBatteryServiceStrategy(unittest.TestCase):
    def test_needs_service_when_true(self):
        # Arrange
        battery_strategy = BatteryServiceStrategy()

        # Act
        result = battery_strategy.needs_service()

        # Assert
        self.assertTrue(result)

    def test_needs_service_when_false(self):
        # Arrange
        battery_strategy = BatteryServiceStrategy()

        # Act
        result = battery_strategy.needs_service()

        # Assert
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
