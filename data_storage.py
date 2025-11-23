# data_storage.py
# Handles reading and writing library data to a simple text file (data persistence).

import json
import os

# Non-functional Requirement: Maintainability - Use a constant for the file path
DATA_FILE = 'library_data.json'


def load_data():
    """
    Functional Module 3a: Reads library data from a JSON file.

    Returns:
        list: The list of book dictionaries, or an empty list if the file is new.
    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: If the file content is corrupted/invalid JSON.
    """
    # Check if file exists before trying to open it
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Data file '{DATA_FILE}' does not exist.")

    try:
        with open(DATA_FILE, 'r') as f:
            # Load JSON content
            data = json.load(f)
            # Basic validation: ensure data loaded is a list
            if isinstance(data, list):
                return data
            else:
                # Corrupted data case
                print(f"[WARNING] Data file content is invalid format (not a list). Starting fresh.")
                return []
    except json.JSONDecodeError:
        # Corrupted JSON case
        print(f"[WARNING] Data file '{DATA_FILE}' is corrupted (Invalid JSON). Starting fresh.")
        return []
    except Exception as e:
        # Catch any other file/OS exceptions
        raise e


def save_data(library_data):
    """
    Functional Module 3b: Writes the current library data list to a JSON file.
    """
    try:
        with open(DATA_FILE, 'w') as f:
            # Write data as pretty-printed JSON for human readability (Usability)
            json.dump(library_data, f, indent=4)
        # print(f"[INFO] Data successfully saved to {DATA_FILE}")
    except Exception as e:
        # Non-functional Requirement: Error Handling Strategy
        print(f"[CRITICAL ERROR] Failed to save data to file: {e}")