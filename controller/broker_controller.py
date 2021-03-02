from model.broker import BrokerModel


class BrokerController:
    def __init__(self):
        self.model_broker = BrokerModel()

    def get_id_broker(self, broker_name):

        broker = self.model_broker.find_broker_by_name(broker_name)
        if broker:
            return broker['id']
        raise Exception("Não foi encontrado nenhum broker com este nome")

