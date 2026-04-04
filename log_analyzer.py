#Parse Single Log Line
def parse_log_line(line):
    try:
        line = line.strip()
        if line == "":
            return None
        parts = line.split(",")
        if len(parts) != 4:
            return None
        timestamp, ip, status, response = parts
        return {
            "timestamp": timestamp.strip(),
            "ip": ip.strip(),
            "status": int(status.strip()),
            "response": int(response.strip())
        }
    except:
        return None

#Read log file
def read_logs(filename):
    entries = []
    try:
        with open(filename, "r") as f:
            for line in f:
                entry = parse_log_line(line)
                if entry:  # only append valid entries
                    entries.append(entry)
    except FileNotFoundError:
        print(f"File {filename} not found")
    return entries

#Calcilate Stats
def analyze_logs(entries):
    total_requests = len(entries)
    unique_ips = set()
    status_distribution = {}
    response_time_per_ip = {}
    error_count_per_ip = {}

    for entry in entries:
        ip = entry["ip"]
        status = entry["status"]
        response = entry["response"]

        unique_ips.add(ip)

        # Status distribution
        status_distribution[status] = status_distribution.get(status, 0) + 1

        # Response times per IP
        if ip not in response_time_per_ip:
            response_time_per_ip[ip] = []
        response_time_per_ip[ip].append(response)

        # Error counts per IP
        if ip not in error_count_per_ip:
            error_count_per_ip[ip] = {"errors": 0, "total": 0}
        error_count_per_ip[ip]["total"] += 1
        if status >= 400:
            error_count_per_ip[ip]["errors"] += 1

    # Average response time per IP
    avg_response_time_per_ip = {}
    for ip in response_time_per_ip:
        avg_response_time_per_ip[ip] = sum(response_time_per_ip[ip]) / len(response_time_per_ip[ip])

    # Problematic IPs
    problematic_ips = {}
    for ip in error_count_per_ip:
        errors = error_count_per_ip[ip]["errors"]
        total = error_count_per_ip[ip]["total"]
        if errors > 0:
            problematic_ips[ip] = (errors / total) * 100

    return total_requests, unique_ips, status_distribution, avg_response_time_per_ip, problematic_ips

#Write reports
def write_report(filename, total_requests, unique_ips, status_distribution, avg_response_per_ip, problematic_ips):
    with open(filename, "w") as f:
        f.write(f"Total Requests: {total_requests}\n")
        f.write(f"Unique IPs: {len(unique_ips)}\n")
        f.write(f"Status Distribution: {status_distribution}\n")
        f.write(f"Average Responses Time:\n")
        for ip in avg_response_per_ip:
            f.write(f"{ip}: {avg_response_per_ip[ip]:.0f}ms\n")

        if problematic_ips:
            f.write(f"Problematic IPs:\n")
            for ip in problematic_ips:
                f.write(f"{ip}: {problematic_ips[ip]:.2f} % errors\n")
        else:
            f.write(f"No problematic IPs\n")
    print(f"Written report to {filename}")


def main():
    log_file = input("Enter log file name: ")
    entries = read_logs(log_file)

    if not entries:
        print("No valid log entries found!")
        return

    total_requests, unique_ips, status_distribution, avg_response_per_ip, problematic_ips = analyze_logs(entries)

    write_report("log_report.txt", total_requests, unique_ips, status_distribution, avg_response_per_ip, problematic_ips)

main()
