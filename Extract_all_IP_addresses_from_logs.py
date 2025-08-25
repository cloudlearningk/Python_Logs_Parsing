
log_file_path = "d:\\Core-python\\devops_cloud_1000.log"

ips = []

with open (log_file_path, 'r') as f:
    for line in f:
        if "IP" in line:
            part = line.split("IP=")[1]
            ip = part.split()[0]
            ips.append(ip)


with open("all_ips.txt", "w") as f:
    for ip in ips:
        f.write(ip + "\n")

with open ("unique_ips.txt", "w") as f:
    for ip in sorted(set(ips)):
        f.write(ip + "\n")
