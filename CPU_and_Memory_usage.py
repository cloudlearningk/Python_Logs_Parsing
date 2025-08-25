log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
output_file_path = "d:\\Core-python\\vm_usage.txt"

with open(log_file_path, "r") as f, open(output_file_path, "w") as out:
    for line in f:
        if "CPU=" in line and "Memory=" in line:
            parts = line.strip().split()

            cpu_value = ""
            mem_value = ""

            for p in parts:
                if "CPU=" in p:
                    cpu_value = p.split("=")[1].replace("%", "")
                    cpu_value = int(cpu_value)  
                if "Memory=" in p:
                    mem_value = p.split("=")[1].upper().replace("%" ,"")
                    if "GB" in mem_value:
                        mem_value = int(mem_value.replace("GB", "")) * 1024
                    elif "MB" in mem_value:
                        mem_value = int(mem_value.replace("MB", ""))
                    else:
                        mem_value = int(mem_value)

            out.write("CPU=" + str(cpu_value) + "%, Memory=" + str(mem_value) + "MB\n")
            print("CPU=", cpu_value, "%", "Memory=", mem_value, "MB")
