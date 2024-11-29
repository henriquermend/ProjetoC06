
from abc import ABC, abstractmethod

# Classe abstrata para definir métodos de criptografia e descriptografia
class EncryptionMethod(ABC):
    """
    Classe base abstrata para métodos de criptografia.

    Essa classe define a interface para os métodos de criptografia e descriptografia,
    obrigando as classes filhas a implementarem os métodos `encrypt` e `decrypt`.
    """

    @abstractmethod
    def encrypt(self, content: bytes, password: str) -> bytes:
        """
        Criptografa o conteúdo.

        Args:
            content (bytes): Conteúdo a ser criptografado.
            password (str): Senha usada para a criptografia.

        Returns:
            bytes: Conteúdo criptografado.
        """
        pass  # Método abstrato, deve ser implementado nas classes filhas

    @abstractmethod
    def decrypt(self, content: bytes, password: str) -> bytes:
        """
        Descriptografa o conteúdo.

        Args:
            content (bytes): Conteúdo criptografado.
            password (str): Senha usada para a descriptografia.

        Returns:
            bytes: Conteúdo descriptografado.
        """
        pass  # Método abstrato, deve ser implementado nas classes filhas


# Implementação de criptografia usando a operação XOR
class XOREncryption(EncryptionMethod):
    """
    Método de criptografia baseado em XOR.

    Esse método aplica a operação XOR entre os bytes do conteúdo e os bytes da senha.
    A operação XOR é simétrica, ou seja, o mesmo método é usado para criptografia
    e descriptografia.
    """

    def encrypt(self, content: bytes, password: str) -> bytes:
        """
        Criptografa o conteúdo usando XOR.

        Args:
            content (bytes): Conteúdo a ser criptografado.
            password (str): Senha usada para a criptografia.

        Returns:
            bytes: Conteúdo criptografado.
        """
        key = password.encode()  # Converte a senha para bytes
        key_length = len(key)  # Comprimento da senha
        # Aplica XOR em cada byte do conteúdo usando a senha como chave
        return bytes([content[i] ^ key[i % key_length] for i in range(len(content))])

    def decrypt(self, content: bytes, password: str) -> bytes:
        """
        Descriptografa o conteúdo usando XOR.

        Observação:
            Como o XOR é simétrico, a descriptografia é igual à criptografia.

        Args:
            content (bytes): Conteúdo criptografado.
            password (str): Senha usada para a descriptografia.

        Returns:
            bytes: Conteúdo descriptografado.
        """
        return self.encrypt(content, password)  # Reutiliza o método `encrypt`


# Implementação de um método de criptografia fictício
class DummyEncryption(EncryptionMethod):
    """
    Método de criptografia fictício que inverte o conteúdo.

    Esse método apenas reverte os bytes do conteúdo, sem usar uma chave de senha.
    Ele é útil para fins de demonstração e teste.
    """

    def encrypt(self, content: bytes, password: str) -> bytes:
        """
        Criptografa o conteúdo invertendo-o.

        Args:
            content (bytes): Conteúdo a ser criptografado.
            password (str): Senha (não utilizada nesse método).

        Returns:
            bytes: Conteúdo invertido.
        """
        return content[::-1]  # Inverte os bytes do conteúdo

    def decrypt(self, content: bytes, password: str) -> bytes:
        """
        Descriptografa o conteúdo invertendo-o novamente.

        Args:
            content (bytes): Conteúdo criptografado.
            password (str): Senha (não utilizada nesse método).

        Returns:
            bytes: Conteúdo original.
        """
        return content[::-1]  # Reverte novamente para restaurar o conteúdo original

