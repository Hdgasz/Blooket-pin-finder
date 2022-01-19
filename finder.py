import socket
import ssl
import random
import time
import threading
import logging
import json
import datetime
from pystyle import Colors, Colorate
from pystyle import Write, Colors
x = datetime.datetime.now()
print("1-100 [you can put more threads but it might brake. If you have a good GPU or CPU you can run 20k threads or more this will crash the blooketgames]")
thread_amount = int(input("Number of Threads: "))
f = open('Pins.txt', 'a' )


def main(name):
    for _ in range(10000):
        random_numbers = str(random.randint(100000, 999999))

        ssl_context = ssl.create_default_context()

        sock = socket.socket()
        sock.settimeout(5)
        sock.connect(("api.blooket.com", 443))

        sock = ssl_context.wrap_socket(sock, False, False, False, "api.blooket.com")

        sock.sendall(f"GET /api/firebase/id?id={random_numbers} HTTP/1.1\r\nHost: api.blooket.com\r\n\r\n".encode())
        data = sock.recv(1024).split(b"vegur\r\n\r\n")[1].split(b"\n")[0]

        _data = json.loads(data.decode())

        if _data["success"] != False:
            print(Colors.green + "Valid game pin: " +  random_numbers)
            f.write('valid game pin: ')
            f.write(random_numbers)
            f.write("\n")
            f.flush()
        else:
            print(Colors.red + 'Invalid game pin: ' + random_numbers)
        time.sleep(0)

        try: sock.shutdown(2)
        except OSError: pass
        sock.close()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    threads = list()
    for index in range(thread_amount):
        logging.info("Main: created and started thread %d.", index)
        x = threading.Thread(target=main, args=(index,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        logging.info("Main: before joining thread %d.", index)
        thread.join()
        logging.info("Main: thread %d done", index)
