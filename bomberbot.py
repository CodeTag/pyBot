import socket
from bot import Bot

class BomberBot():
    def __init__(self):
        try:
            self.conectar("rbBot", "984198716")
            self.controlConexion()
        except Exception as e:
            print(e)

    def conectar(self, user, token):
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.socket_cliente.connect(("bomberbot.py", 5000))
        bienvenida = self.socket_cliente.recv(1279)
        print(bienvenida)
        self.socket_cliente.send("%s,%s" % (user, token))
        self.conectado = True

    def controlConexion(self):
        response = None
        while self.conectado:
            print("turno")

            server_message = self.socket_cliente.recv(511)
            message = server_message.split(";")
            print(message[0])

            if message[0] == "EMPEZO":
                bot = Bot(message[2][0])
                bot.update_map(message[1])
            elif message[0] == "TURNO":
                print("turno: %s" % message[1])
                bot.update_map(message[2])
                msg = bot.move()
                self.socket_cliente.send(msg)
            elif message[0] == "PERDIO":
                print("perdi :(")

if __name__ == "__main__":
	BomberBot()
