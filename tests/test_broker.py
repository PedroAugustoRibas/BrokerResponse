import unittest
from model.broker import BrokerModel


class TestBroker(unittest.TestCase):

    def test_find_broker_by_name(self):
        """
        Testa a função find_broker_by_name

        :return:
        """
        broker_model = BrokerModel()
        self.assertEqual(broker_model.find_broker_by_name('TIM'), {'id': 1, 'name': 'TIM'})
        self.assertEqual(broker_model.find_broker_by_name('TEST_TESTE'), None)


if __name__ == '__name__':
    unittest.main()
