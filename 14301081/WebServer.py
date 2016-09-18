import socket
import traceback
import thread


def main():
    HOST = '127.0.0.1'
    PORT = 3333

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    clientSocket.bind((HOST, PORT))
    clientSocket.listen(1)
    while 1:
        try:
            clientsock, clientaddr = clientSocket.accept()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue
        thread.start_new_thread(ClientServer, (clientsock, clientaddr))


def ReverseStr(RS):
    answ = ''
    l = len(RS)
    while l > 0:
        l -= 1
        answ += RS[l]
    return answ


def ClientServer(clientSocket, clientAddress):
    try:
        print(clientSocket.getpeername())
        while 1:
            data = clientSocket.recv(1024)
            if not len(data):
                break
            print(clientSocket.getpeername()),
            print(': ' + str(data))
            back = ReverseStr(str(data))
            clientSocket.sendall(back + "\n")

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
    try:
        clientSocket.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()


if __name__ == "__main__":
    main()
