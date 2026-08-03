from datetime import datetime
import sys
import os


def create_file() -> None:

    command = sys.argv[1:]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dir_path = None
    dir_args = []
    if "-d" in command:
        d_index = command.index("-d")
        for arg in command[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_args.append(arg)
        if dir_args:
            dir_path = os.path.join(*dir_args)
            os.makedirs(dir_path, exist_ok=True)

    if not "-f" in command:
            return
    
    file_name = None
    f_index = command.index("-f")
    for name in command[f_index + 1:]:
        if name.startswith("-"):
            break
        file_name = name

    if not file_name:
        return
    
    file_path = os.path.join(dir_path, file_name) if dir_path else file_name
    with open(file_path, "a") as f:
        file_content = []
        line = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            file_content.append(f"Line{line} {line_content}")
            line += 1
        f.write(current_time + "\n")
        f.write("\n".join(file_content) + "\n")
