import os
import shutil

def list_files(directory):
    """List all files and directories in the given directory."""
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return f"Directory '{directory}' not found."

def create_directory(directory):
    """Create a new directory."""
    try:
        os.makedirs(directory, exist_ok=True)
        return f"Directory '{directory}' created successfully."
    except OSError as e:
        return f"Error creating directory '{directory}': {e}"

def delete_file(file_path):
    """Delete a file."""
    try:
        os.remove(file_path)
        return f"File '{file_path}' deleted successfully."
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except PermissionError:
        return f"No permission to delete '{file_path}'."

def move_file(src, dest):
    """Move a file from source to destination."""
    try:
        shutil.move(src, dest)
        return f"Moved file from '{src}' to '{dest}'."
    except FileNotFoundError:
        return f"Source file '{src}' not found."
    except shutil.Error as e:
        return f"Error moving file: {e}"

def read_file(file_path):
    """Read the contents of a file."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"File '{file_path}' not found."

def write_file(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, 'w') as f:
            f.write(content)
            return f"Content written to '{file_path}'."
    except OSError as e:
        return f"Error writing to file '{file_path}': {e}"
