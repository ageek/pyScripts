import os

def rename_folders(directory, prefix):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            if dir_name.startswith(prefix):
                old_path = os.path.join(root, dir_name)
                new_path = os.path.join(root, dir_name[len(prefix):])
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    directory = input("Enter the root directory: ")  # Root directory path
    prefix_to_remove = input("Enter prefix to remove: ")  # Prefix to remove

    rename_folders(directory, prefix_to_remove)

