log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
output_file_path = "d:\\Core-python\\backup_summary.txt"

count = 0
total_size = 0

with open(log_file_path, "r") as f:
    for line in f:
        if "Backup completed" in line:
            count = count + 1
            parts = line.strip().split()
            for p in parts:
                if "Size=" in p:
                    size = int(p.replace("Size=", "").replace("MB", "").replace("GB", ""))
                    total_size = total_size + size

with open(output_file_path, "w") as out:
    out.write("Backup completed count: " + str(count) + "\n")
    out.write("Total backup size: " + str(total_size) + " MB\n")

print("Backup completed count:", count)
print("Total backup size:", total_size, "MB")
