import os
import traceback
from model.file import FileModel


class FileController:
    def __init__(self):
        self.file_model = FileModel()

    def get_data(self):
        """
        Função que realiza a chamada da função get_files_data()
        :return: Retorna os dados do arquivo
        """
        data = self.file_model.get_files_data()
        if data:
            return data
        raise Exception("Nenhum arquivo foi encontrado")


