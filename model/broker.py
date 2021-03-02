
class BrokerModel:
    def __init__(self):
        self.dir_files = 'files/'
        self.list_broker = [{"id": 1, "name": "TIM"},
                            {"id": 1, "name": "VIVO"},
                            {"id": 2, "name": "CLARO"},
                            {"id": 2, "name": "OI"},
                            {"id": 3, "name": "NEXTEL"}]

    @staticmethod
    def list_ddd():
        return {11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46 , 47, 48, 49, 51, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99}

    def find_broker_by_name(self, broker_name):
        """
        Pesquisa o broker pelo nome
        Arg: broker_name(String):
        :return: broker
        """
        for broker in self.list_broker:
            if broker_name.lower() == broker['name'].lower():
                return broker

        return None



