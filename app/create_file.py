from datetime import datetime
import sys
import os


def create_file() -> None:
    command_parts = sys.argv[1:]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dir_list = []
    if "-d" in command_parts:
        dir_index = command_parts.index("-d")
    for arg in command_parts[dir_index + 1:]:
        if arg.startswith("-"):
            break
        dir_list.append(arg)

    for directory in dir_list:
        if not os.path.exists(directory):
            os.makedirs(directory)

    if "-f" in command_parts:
        file_index = command_parts.index("-f")
    for arg in command_parts[file_index + 1:]:
        if arg.startswith("-"):
            break
        if os.path.exists(arg):
            content = []
            line = 0
            while True:
                content_line = input("Enter content line: ")
                if content_line.lower() == "stop":
                    break
                line += 1
                content.append(f"Line{line} {content_line}")
            with open(arg, "a") as f:
                f.write(current_time)
                f.write("\n".join(content))

        with open(arg, "w") as f:
            content = []
            line = 0
            while True:
                content_line = input("Enter content line: ")
                if content_line.lower() == "stop":
                    break
                line += 1
                content.append(f"Line{line} {content_line}")
            f.write(current_time)
            f.write("\n".join(content))
