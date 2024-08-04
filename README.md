How it works:
Configuration: Set the network range, port range, timeout, and the number of threads.
scan_port(): Attempts to connect to a specific port on a given IP address. If successful, it prints that the port is open.
scan_ip(): Scans all ports in the specified range on a given IP address.
scan_network(): Scans all IP addresses in the specified network range. It uses threading to scan multiple IP addresses concurrently
To run the script use "python network_scanner.py".
