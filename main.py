from controller.file_controller import FileController
from controller.broker_controller import BrokerController
from controller.phone_controller import PhoneController

erros = []
success = []

try:
    phone_controller = PhoneController()
    file_controller = FileController()
    broker_controller = BrokerController()
    data_files = file_controller.get_data()

    for file in data_files:
        for line, item in enumerate(data_files[file]):
            try:
                data = item.split(";")

                id_message = data[0]
                ddd = data[1]
                phone = data[2]
                id_broker = broker_controller.get_id_broker(data[3])
                scheduling_time = data[4]
                message = data[5]

                phone_controller.validate_phone(ddd, phone, scheduling_time)
                phone_controller.validate_hour(scheduling_time)
                phone_controller.validate_message(message)

                if PhoneController.check_phone_blacklist(phone):
                    raise Exception("[%s] -> Telefone na Blacklist: %s" % (file, phone))

                success.append("[%s] -> %s;%s" % (file, id_message, id_broker))

            except Exception as err:
                erros.append("[%s] -> Linha[%s] -> %s" % (file, line + 1, err))
                continue

    print("Sucesso:")
    for line in success:
        print(line)

    print("\nErros:")
    for line in erros:
        print(line)

except Exception as err:
    print(err)

