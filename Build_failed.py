log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
output_file_path = "d:\\Core-python\\failed_builds.txt"

with open(log_file_path, "r") as f, open(output_file_path, "w") as out:
    for line in f:
        if "Build Failed" in line:
            out.write(line)
