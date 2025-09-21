import re
import pandas as pd
import os


def extract_unique_log_info(log_text):
    """
    Extracts SrcIP, DstIP, Protocol, and DstPort from log data
    and returns a set of unique entries.
    """
    pattern = re.compile(
        r"SrcIP: (?P<src_ip>[\d.]+), DstIP: (?P<dst_ip>[\d.]+), .*?DstPort: (?P<dst_port>\d+), Protocol: (?P<protocol>\w+)",
        re.MULTILINE | re.DOTALL
    )

    unique_entries = set()

    for match in pattern.finditer(log_text):
        entry_tuple = (
            match.group('src_ip'),
            match.group('dst_ip'),
            match.group('protocol'),
            match.group('dst_port')
        )
        unique_entries.add(entry_tuple)

    return unique_entries


def main():
    """Main function to read log data, extract unique info, and export to Excel."""
    file_path = "12-9-25.txt"
    excel_file_path = "unique_log_report-12-9-25.txt.xlsx"

    try:
        # Step 1: Read data from the log file
        with open(file_path, 'r') as file:
            log_data = file.read()

        # Step 2: Extract unique information using the dedicated function
        extracted_data_set = extract_unique_log_info(log_data)

        # Check if any data was extracted
        if extracted_data_set:
            # Step 3: Convert the set of tuples to a pandas DataFrame
            # Define column names for the DataFrame
            columns = ['Source IP', 'Destination IP', 'Protocol', 'Destination Port']
            df = pd.DataFrame(list(extracted_data_set), columns=columns)

            # Write the DataFrame to an Excel file
            df.to_excel(excel_file_path, index=False)

            print(f"Successfully exported {len(df)} unique records to '{excel_file_path}'.")
        else:
            print("No log data found to export.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}. Please ensure you have pandas and openpyxl installed.")


# Execute the main function
if __name__ == "__main__":
    main()
