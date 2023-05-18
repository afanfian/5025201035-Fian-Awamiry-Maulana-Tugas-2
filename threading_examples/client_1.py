import socket
import logging



def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")
    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        msg = 'TIME\r\n'
        logging.warning(f"sending {msg}")
        sock.sendall(msg.encode('utf-8'))
        data = sock.recv(32)
        result = data.decode('utf-8')
        logging.warning(f"{result}")
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    for i in range(1,10):
        kirim_data()
