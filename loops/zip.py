# task 11
hosts = ["host1", "host2", "host3"]
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
for host, ip in zip(hosts, ips):
    print(host, ip) 