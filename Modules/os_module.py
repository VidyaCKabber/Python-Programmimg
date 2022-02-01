import os

# Current working directory
print(os.getcwd())

# Change current working directory
os.chdir("/home/vidya")

# list directories / files in another directory
files = os.listdir(os.getcwd())
#print(files)

files1 = os.listdir(r'/home/vidya')
# print(files1)

# Create new directory
os.mkdir("Test")

# Create recursive directories
os.makedirs('Test/dev_tests', exist_ok=True)

# Remove directory
os.rmdir("/home/vidya/Test/dev_tests/")

# Concatinate files and directories
cur_directory = os.getcwd()
file1 = 'text1.txt'

combined = os.path.join(cur_directory, 'Folder1','OneMarker', file1)
print(combined)

# Check file or folder is existed
print(os.path.exists(combined))

# Check given path is file or directory
print(os.path.isfile(combined))
print(os.path.isdir(combined))

# Get file stats
file_path = os.path.join(os.getcwd(), 'learn-python', 'newfile.txt')
print(os.stat(file_path))
print(os.stat(file_path).st_size)

# Access environment variables
env_path = os.environ.get('PATH')
print(env_path)

# Get login username
print(os.getlogin())
