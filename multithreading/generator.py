import time

file_path = "C:\\Users\\Home\\PycharmProjects\\WelcomeScreen\\multithreading\\server_logs.txt"

time_start = time.time()

lines = (line for line in open(file_path, encoding="utf-8"))
errors = (line.strip() for line in lines if "[ERROR]" in line)
for error_line in errors: print(error_line)

time_end = time.time()
time_elapsed = time_end - time_start
print(time_elapsed)