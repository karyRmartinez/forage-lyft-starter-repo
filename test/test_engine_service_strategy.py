import unittest
from engine_service_strategy import EngineServiceStrategy

class TestEngineServiceStrategy(unittest.TestCase):
    def test_needs_service_when_true(self):
        # Arrange
        engine_strategy = EngineServiceStrategy()

        # Act
        result = engine_strategy.needs_service()

        # Assert
        self.assertTrue(result)

    def test_needs_service_when_false(self):
        # Arrange
        # Adjust the implementation if needed, for example, by providing specific conditions when service is not needed
        engine_strategy = EngineServiceStrategy()

        # Act
        result = engine_strategy.needs_service()

        # Assert
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
