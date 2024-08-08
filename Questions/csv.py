# Path to your log file
log_file_path = '/http_requests.log'

# Open the file and filter lines containing "kafka"
with open(log_file_path, 'r') as file:
    kafka_lines = [line for line in file if 'kafka' in line]

# Output the filtered lines
for line in kafka_lines:
    print(line.split()[0])
