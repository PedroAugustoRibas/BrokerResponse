import os


class FileModel:
    def __init__(self):
        self.dir_files = 'files/'

    def get_files_data(self):
        """
        Função que realiza uma busca nos dados do arquivo que é depositado no diretório /files
        :return: Retorna os dados do arquivo
        """
        data = {}
        files = os.listdir(self.dir_files)
        for file in files:
            with open(os.path.join(self.dir_files, file)) as file_data:
                data[file] = file_data.readlines()
        return data



