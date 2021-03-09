import unittest
from model.blacklist import BlackList


class TestBlackList(unittest.TestCase):

    def test_find_phone(self):
        """
          Testa a função find_phone

        :return:
        """
        self.assertEqual(BlackList.find_phone('21914683666'), True)
        self.assertEqual(BlackList.find_phone('41998405459'), False)


if __name__ == '__name__':
    unittest.main()
