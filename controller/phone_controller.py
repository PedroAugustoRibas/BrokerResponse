from datetime import datetime
from model.broker import BrokerModel
from model.blacklist import BlackList


class PhoneController:
    def __init__(self):
        self.list_ddd = BrokerModel.list_ddd()
        self.mailing_list = {}

    def validate_phone(self, ddd, phone, scheduling_time):
        """
        Função para validar o telefone, ddd e horario de atendimento
        Arg: ddd (Integer)
        Arg: phone (String)
        Arg: scheduling_time (String)
        :return:
        """
        phone_size = len(phone)
        scheduling_time = self.convert_string_to_date(scheduling_time)
        if int(ddd) not in self.list_ddd:
            raise Exception("[Telefone] DDD inválido no Brasil: %s" % ddd)

        if len(ddd) > 2:
            raise Exception("[Telefone] Tamanho de DDD inválido: %s" % ddd)

        if not int(phone[0]) == 9:
            raise Exception("[Telefone] Inicio do telefone inválido: %s " % phone)

        if int(phone[1]) > 6:
            raise Exception("[Telefone] Segundo dígito menor que 6: %s " % phone)

        if not phone_size == 9:
            raise Exception("[Telefone] Tamanho inválido: %s " % phone)

        if int(ddd) == 11:
            raise Exception("[Telefone] DDD bloqueado: [%s] São Paulo" % ddd)

        if phone in self.mailing_list.keys() and scheduling_time > self.mailing_list[phone]:
            raise Exception("[Telefone] Já foi enviada uma mensagem para esse número : %s" % phone)

        self.mailing_list[phone] = scheduling_time.strftime("%H:%M:%S")

    def validate_message(self, message):
        """
        Função para validação específica da Mensagem
        :return:
        """
        if len(message) > 140:
            raise Exception("Mensagem inválida: excede 140 caracteres")

    def validate_hour(self, scheduling_time):
        """
        Função para validação específica do Horário
        :return:
        """
        scheduling_time = self.convert_string_to_date(scheduling_time)
        if scheduling_time.hour > 19:
            raise Exception("Horário agendamento inválido: horário [%s] acima das 19:59:59" % scheduling_time)

    @staticmethod
    def convert_string_to_date(date):
        """
        Converte a data String para Datetime
        Arg: date(string)
        :return: Data no formato Datetime
        """
        try:
            return datetime.strptime(date, '%H:%M:%S')
        except Exception as err:
            raise Exception("Horário agendamento inválido [%s]: %s" % (date, err))

    @staticmethod
    def check_phone_blacklist(phone):
        """
        Verifica se o telefone está na blacklist
        Arg: phone(string)
        :return: boolean
        """
        if BlackList.find_phone(phone):
            return True
        return False



