import tkinter as tk
from tkinter import scrolledtext, simpledialog
import os
from file_manager import FileManager
from ransomware_interface import XOREncryption, DummyEncryption  # Certifique-se que esse arquivo existe

# Arte ASCII Inicial
ASCII_IMAGE_NORMAL = """
            .,,uod8B8bou,,.                             
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.                    
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||                   
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||                   
         !.......:!?|||||!!^^""'            ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         .........||||                    ,||||                   
          .;.......||||               _.-!!|||||                   
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'                    
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....               
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   .             
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     .           
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^";:::       .         
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.   
..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo. 
  ..........:::::::::::::::::::::::;iof688888888888b.     YBBBP^'
    ........::::::::::::::::;iof688888888888888888888b.          
      ......:::::::::;iof688888888888888888888888888888b.         
        ....:::;iof688888888888888888888888888888888899fT!        
          ..::!8888888888888888888888888888888899fT|!^"'          
            ' !!988888888888888888888888899fT|!^"'                
                !!8888888888888888899fT|!^"'                      
                  !988888888899fT|!^"'                            
                    !9899fT|!^"'                                          
"""

# Arte ASCII Após Criptografia
ASCII_IMAGE_ENCRYPTED = """
⢀⣴⣶⣿⣿⣷⡶⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢶⣿⣿⣿⣿⣶⣄⠀⠀
⠀⢠⡿⠿⠿⠿⢿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⡿⠿⠿⠿⠿⣦⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⡿⠆⠀⠀⠀⠀⠰⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⡤⠄⢤⣀⡈⢿⡄⠀⠀⠀⠀⢠⡟⢁⣠⡤⠠⠤⢤⣀⠀⠀⠀⠀
⠐⢄⣀⣼⢿⣾⣿⣿⣿⣷⣿⣆⠁⡆⠀⠀⢰⠈⢸⣿⣾⣿⣿⣿⣷⡮⣧⣀⡠⠀
⠰⠛⠉⠙⠛⠶⠶⠏⠷⠛⠋⠁⢠⡇⠀⠀⢸⡄⠈⠛⠛⠿⠹⠿⠶⠚⠋⠉⠛⠆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡇⠀⠀⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢻⠇⠀⠀⠘⡟⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠰⣄⡀⠀⠀⣀⣠⡤⠞⠠⠁⠀⢸⠀⠀⠀⠀⡇⠀⠘⠄⠳⢤⣀⣀⠀⠀⣀⣠⠀
⠀⢻⣏⢻⣯⡉⠀⠀⠀⠀⠀⠒⢎⣓⠶⠶⣞⡱⠒⠀⠀⠀⠀⠀⢉⣽⡟⣹⡟⠀
⠀⠀⢻⣆⠹⣿⣆⣀⣀⣀⣀⣴⣿⣿⠟⠻⣿⣿⣦⣀⣀⣀⣀⣰⣿⠟⣰⡟⠀⠀
⠀⠀⠀⠻⣧⡘⠻⠿⠿⠿⠿⣿⣿⣃⣀⣀⣙⣿⣿⠿⠿⠿⠿⠟⢃⣴⠟⠀⠀⠀
⠀⠀⠀⠀⠙⣮⠐⠤⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠤⠊⡵⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠲⣶⣶⠖⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⢀⣿⣿⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿
"""

# Arte ASCII para Sucesso na Descriptografia
ASCII_IMAGE_SUCCESS = """
░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗░██████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░╚█████╗░
██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░██████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
"""

# Arte ASCII para Erro de Senha
ASCII_IMAGE_ERROR = """
 ___ _ __ _ __ ___  _ __ 
 / _ \ '__| '__/ _ \| '__|
|  __/ |  | | | (_) | |   
 \___|_|  |_|  \___/|_|   
"""

# Arte ASCII para Exclusão de Arquivos
ASCII_IMAGE_DELETED = """
                          88            88                               
         88            88              ,d               
         88            88              88               
 ,adPPYb,88  ,adPPYba, 88  ,adPPYba, MM88MMM ,adPPYba,  
a8"    Y88 a8P_____88 88 a8P_____88   88   a8P_____88  
8b       88 8PP""""""" 88 8PP"""""""   88   8PP"""""""  
"8a,   ,d88 "8b,   ,aa 88 "8b,   ,aa   88,  "8b,   ,aa  
 "8bbdP"Y8  "Ybbd8"' 88  "Ybbd8"'   "Y888 "Ybbd8"'                
"""

class RansomwareSimulatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simulador de Ransomware")
        self.window.geometry("900x600")
        self.window.configure(bg="black")

        self.logs = []

        # Métodos de criptografia disponíveis
        self.encryption_methods = {
            "XOR": XOREncryption(),
            "Dummy": DummyEncryption(),
        }
        self.selected_method = tk.StringVar(value="XOR")  # Valor padrão

        # Inicialização do FileManager com o método padrão e senha fixa
        self.file_manager = FileManager(self.encryption_methods[self.selected_method.get()], "1234")

        self.attempts_left = 3  # Número máximo de tentativas permitidas

        # Configuração da interface gráfica
        self.setup_ui()

    def setup_ui(self):
        """
        Configura a interface gráfica com imagens ASCII, botões e área de logs.
        """
        # Imagem ASCII Inicial
        self.ascii_label = tk.Label(
            self.window,
            text=ASCII_IMAGE_NORMAL,
            font=("Courier", 8, "bold"),
            bg="black",
            fg="lime"
        )
        self.ascii_label.pack(pady=10)

        # Título
        self.title_label = tk.Label(
            self.window,
            text="Simulador de Ransomware",
            font=("Courier", 24, "bold"),
            bg="black",
            fg="lime"
        )
        self.title_label.pack(pady=20)

        # Menu para selecionar método de criptografia
        self.method_menu_label = tk.Label(
            self.window,
            text="Escolha o método de criptografia:",
            font=("Courier", 14),
            bg="black",
            fg="lime"
        )
        self.method_menu_label.pack(pady=5)

        self.method_menu = tk.OptionMenu(
            self.window,
            self.selected_method,
            *self.encryption_methods.keys(),
            command=self.update_encryption_method  # Chamada ao alterar o método
        )
        self.method_menu.config(
            font=("Courier", 12),
            bg="black",
            fg="lime",
            width=20
        )
        self.method_menu.pack(pady=5)

        # Frame para os botões
        self.button_frame = tk.Frame(self.window, bg="black")
        self.button_frame.pack(pady=10)

        # Botão Criptografar
        self.encrypt_button = tk.Button(
            self.button_frame,
            text="Criptografar",
            command=self.encrypt_files,
            font=("Courier", 14),
            bg="black",
            fg="lime",
            width=20
        )
        self.encrypt_button.grid(row=0, column=0, padx=5)

        # Botão Descriptografar
        self.decrypt_button = tk.Button(
            self.button_frame,
            text="Descriptografar",
            command=self.decrypt_files,
            font=("Courier", 14),
            bg="black",
            fg="lime",
            width=20
        )
        self.decrypt_button.grid(row=0, column=1, padx=5)

        # Área de Logs
        self.log_area = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            font=("Courier", 12),
            bg="black",
            fg="lime",
            width=80,
            height=10
        )
        self.log_area.pack(pady=20)

    def add_log(self, message):
        """
        Adiciona uma mensagem à área de logs.
        """
        self.logs.append(message)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def update_encryption_method(self, method):
        """
        Atualiza o método de criptografia com base na escolha do usuário.
        """
        self.add_log(f"Método de criptografia atualizado para: {method}")
        self.file_manager = FileManager(self.encryption_methods[method], self.file_manager.password)

    def encrypt_files(self):
        """
        Executa o processo de criptografia dos arquivos na pasta simulada.
        Atualiza a imagem ASCII após a criptografia.
        """
        self.add_log("Iniciando criptografia...")
        logs = self.file_manager.encrypt_files("simulated_folder")
        for log in logs:
            self.add_log(log)
        self.ascii_label.config(text=ASCII_IMAGE_ENCRYPTED)
        self.add_log("Arquivos criptografados com sucesso!")

    def decrypt_files(self):
        """
        Solicita a senha do usuário e executa o processo de descriptografia.
        Verifica a senha e atualiza as tentativas restantes.
        """
        if self.attempts_left <= 0:
            self.add_log("Todos os arquivos já foram deletados. Operação inválida.")
            return

        # Solicita a senha ao usuário
        password = simpledialog.askstring("Senha", "Digite a senha para descriptografar:")
        if password:
            if password == self.file_manager.password:
                # Senha correta
                self.add_log("Senha correta! Descriptografando arquivos...")
                logs = self.file_manager.decrypt_files("simulated_folder", password)
                for log in logs:
                    self.add_log(log)
                self.ascii_label.config(text=ASCII_IMAGE_SUCCESS)
                self.attempts_left = 3  # Reseta as tentativas
            else:
                # Senha incorreta
                self.attempts_left -= 1
                self.add_log(f"Senha incorreta! Tentativas restantes: {self.attempts_left}")
                self.ascii_label.config(text=ASCII_IMAGE_ERROR)

                # Deleta os arquivos se as tentativas acabarem
                if self.attempts_left == 0:
                    self.delete_all_files()

    def delete_all_files(self):
        """
        Deleta todos os arquivos da pasta simulada após exceder as tentativas.
        Atualiza a imagem ASCII para indicar exclusão.
        """
        folder = "simulated_folder"
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
        self.add_log("Todos os arquivos foram deletados!")
        self.ascii_label.config(text=ASCII_IMAGE_DELETED)

    def run(self):
        """
        Inicia o loop principal da aplicação.
        """
        self.window.mainloop()


if __name__ == "__main__":
    gui = RansomwareSimulatorGUI()
    gui.run()

