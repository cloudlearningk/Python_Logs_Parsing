log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
output_file_path = "d:\\Core-python\\container_ids.txt"

with open(log_file_path, "r") as f, open(output_file_path, "w") as out:
    for line in f:
        parts = line.strip().split()
        for p in parts:
            if "containerID=" in p:
                container_id = p.replace("containerID=", "")
                out.write(container_id + "\n")
                print(container_id)
