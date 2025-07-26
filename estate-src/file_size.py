import os


def count_python_files(root_dir='.'):
    py_file_count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.py'):
                py_file_count += 1
    return py_file_count

if __name__ == '__main__':
    root = '.'  # Change to your project root if needed
    total = count_python_files(root)
    print(f"Total Python (.py) files: {total}")
