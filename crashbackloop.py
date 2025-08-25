log_file_path = "d:\\Core-python\\devops_cloud_1000.log"
output_file_path = "d:\\Core-python\\crash_alerts.txt"

alert_found = False

with open(log_file_path, "r") as f, open(output_file_path, "w") as out:
    for line in f:
        if "CrashLoopBackOff" in line:
            alert_found = True
            out.write(line)
            print("ALERT: CrashLoopBackOff detected!")
            print(line.strip())

if not alert_found:
    print("No CrashLoopBackOff detected in logs.")
