import requests


class BlackList:

    @staticmethod
    def find_phone(phone):
        """
        Verifica se o telefone está na blacklist
        Args:
          phone (String) : Telefone para consulta na blacklist
        Returns:
            (bool)  (True -> Telefone na Blacklist / False -> Telefone OK)
        """
        result = requests.get(url="https://front-test-pg.herokuapp.com/blacklist/")

        for item in result.json():
            if item["phone"] == phone:
                return True
        return False
