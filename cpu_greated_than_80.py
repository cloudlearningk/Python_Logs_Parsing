log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
output_file_path = "d:\\Core-python\\high_cpu_logs.txt"

with open(log_file_path, "r") as f, open(output_file_path, "w") as out:
    for line in f:
        
        if "CPU=" in line and "Memory=" in line:
            parts = line.strip().split()

            cpu_value = 0

            
            for p in parts:
                if "CPU=" in p:
                    cpu_value = int(p.split("=")[1].replace("%", ""))

            
            if cpu_value > 80:
                out.write(line)  
                print("CPU =", cpu_value, "%")
