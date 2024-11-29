<<<<<<< HEAD
# basic_ransomware.py

import os
from ransomware_interface import Ransomware

class BasicRansomware(Ransomware):
    def encrypt_files(self, directory):
        print(f"Encrypting files in {directory}...")
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):  # Apenas arquivos .txt
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, "r") as file:
                        content = file.read()
                    with open(filepath, "w") as file:
                        file.write(content[::-1])  # Simula criptografia invertendo o texto
                    print(f"Encrypted: {filename}")
                except Exception as e:
                    print(f"Error encrypting {filename}: {e}")

    def decrypt_files(self, directory, key):
        print(f"Decrypting files in {directory}...")
        if key != "1234":  # Chave fictícia
            print("Invalid decryption key!")
            return
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, "r") as file:
                        content = file.read()
                    with open(filepath, "w") as file:
                        file.write(content[::-1])  # Reverte o texto
                    print(f"Decrypted: {filename}")
                except Exception as e:
                    print(f"Error decrypting {filename}: {e}")
=======
# basic_ransomware.py

import os
from ransomware_interface import Ransomware

# Classe BasicRansomware herda de uma interface base (Ransomware)
class BasicRansomware(Ransomware):
    def encrypt_files(self, directory):  
        """
        Criptografa arquivos em um diretório, invertendo o conteúdo dos arquivos .txt.

        Args:
            directory (str): Caminho do diretório onde os arquivos estão localizados.
        """
        print(f"Encrypting files in {directory}...")  # Log informando início do processo
        for filename in os.listdir(directory):  # Itera sobre os arquivos do diretório
            if filename.endswith(".txt"):  # Verifica se o arquivo tem extensão .txt
                filepath = os.path.join(directory, filename)  # Gera o caminho completo do arquivo
                try:
                    with open(filepath, "r") as file:  # Abre o arquivo para leitura
                        content = file.read()  # Lê o conteúdo original do arquivo
                    with open(filepath, "w") as file:  # Abre o arquivo para escrita
                        file.write(content[::-1])  # Inverte o texto e grava de volta no arquivo
                    print(f"Encrypted: {filename}")  # Log indicando sucesso na criptografia
                except Exception as e:  # Trata possíveis erros ao acessar ou manipular o arquivo
                    print(f"Error encrypting {filename}: {e}")  # Log de erro

    def decrypt_files(self, directory, key):
        """
        Descriptografa arquivos em um diretório, revertendo o conteúdo dos arquivos .txt.

        Args:
            directory (str): Caminho do diretório onde os arquivos estão localizados.
            key (str): Chave necessária para descriptografar os arquivos.
        """
        print(f"Decrypting files in {directory}...")  # Log informando início do processo de descriptografia
        if key != "1234":  # Verifica se a chave fornecida é válida
            print("Invalid decryption key!")  # Log de erro para chave inválida
            return  # Encerra o processo caso a chave seja incorreta

        for filename in os.listdir(directory):  # Itera sobre os arquivos no diretório
            if filename.endswith(".txt"):  # Verifica se o arquivo tem extensão .txt
                filepath = os.path.join(directory, filename)  # Gera o caminho completo do arquivo
                try:
                    with open(filepath, "r") as file:  # Abre o arquivo para leitura
                        content = file.read()  # Lê o conteúdo "criptografado" do arquivo
                    with open(filepath, "w") as file:  # Abre o arquivo para escrita
                        file.write(content[::-1])  # Reverte o texto invertido para restaurar o original
                    print(f"Decrypted: {filename}")  # Log indicando sucesso na descriptografia
                except Exception as e:  # Trata possíveis erros ao acessar ou manipular o arquivo
                    print(f"Error decrypting {filename}: {e}")  # Log de erro
>>>>>>> cf674cf (Entrega Final)
