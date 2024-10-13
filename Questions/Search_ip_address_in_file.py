# Path to your log file
log_file_path = 'your_log_file.log'

# Function to check if a string is a valid IP address
def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() and not (0 <= int(part) <= 255):
            return False
    return True

# Read the log file and extract IP addresses
ip_addresses = set()
with open(log_file_path, 'r') as file:
    for line in file:
        for word in line.split():
            if is_valid_ip(word):
                ip_addresses.add(word)

# Output the extracted IP addresses
for ip in ip_addresses:
    print(ip)
