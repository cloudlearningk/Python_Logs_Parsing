log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
output_file_path = "d:\\Core-python\\user_hits.txt"

users = {}

with open(log_file_path, "r") as f:
    for line in f:
        parts = line.split()
        for p in parts:
            if "User=" in p:
                user = p.replace("User=", "")
                if user in users:
                    users[user] = users[user] + 1
                else:
                    users[user] = 1

with open(output_file_path, "w") as out:
    for user in users:
        out.write(user + " " + str(users[user]) + "\n")
