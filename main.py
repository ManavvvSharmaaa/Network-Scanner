import socket
from threading import Thread, Lock

network = '192.168.1.'
port_range = (20, 1024)
timeout = 1
threads = 100

lock = Lock()


def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            with lock:
                print(f"IP: {ip}, Port: {port} is open")
    except:
        pass


def scan_ip(ip):
    for port in range(port_range[0], port_range[1] + 1):
        scan_port(ip, port)


def scan_network():
    threads_list = []
    for i in range(1, 255):
        ip = network + str(i)
        t = Thread(target=scan_ip, args=(ip,))
        t.start()
        threads_list.append(t)

        while len(threads_list) >= threads:
            for thread in threads_list:
                if not thread.is_alive():
                    threads_list.remove(thread)

    for thread in threads_list:
        thread.join()


if __name__ == "__main__":
    scan_network()
