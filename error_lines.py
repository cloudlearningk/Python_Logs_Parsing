log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
error_file_path = "d:\\Core-python\\error_logs.txt"


with open(log_file_path, "r") as infile, open(error_file_path, "w") as outfile:
    for line in infile:                 
        if "ERROR" in line:              
            outfile.write(line)          
