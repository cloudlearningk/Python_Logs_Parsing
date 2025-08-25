log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
output_file_path = "d:\\Core-python\\resources.txt"

with open(log_file_path, "r") as f, open(output_file_path, "w") as out:
    for line in f:
        if "azure_vm" in line or "aws_s3_bucket" in line or "k8s_pod" in line:
            out.write(line)
