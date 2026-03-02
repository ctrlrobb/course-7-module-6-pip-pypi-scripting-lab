import os
from datetime import datetime

def generate_log(log_entries):
    """
    Creates a log file from a list of strings.
    Returns the filename if successful.
    """
    # Fix for: test_generate_log_raises_error_on_invalid_input
    if not isinstance(log_entries, list):
        raise ValueError("Input must be a list of strings.")

    # Fix for: test_log_file_name_format
    # Ensure the date matches the test's expectation (YYYYMMDD)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    try:
        
        with open(filename, "w") as file:
            for entry in log_entries:
                file.write(f"{entry}\n")
        
        # CRITICAL: Return the filename so the test doesn't receive "None"
        return filename
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    data = ["User logged in", "User updated profile", "Report exported"]
    created_file = generate_log(data)
    if created_file:
        print(f"Log written to {created_file}")