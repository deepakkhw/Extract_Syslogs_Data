# Extract_Syslogs_Data
A lightweight Python utility that parses raw syslog files and extracts the most relevant network‑traffic fields:

1. Source IP
2. Destination IP
3. Destination Port
4. Protocol (TCP, UDP, ICMP, …)
   
The script also deduplicates identical entries, ensuring a clean output.

1. Input: Plain‑text (.txt) file with one syslog line per row.
2. Output: in excel file ready for Excel, Google Sheets, or any downstream analysis tool.

✨ Key Features
1. Simple usage – just point it at a .txt log file.
2. Robust parsing – uses regular expressions to locate IPv4 addresses, ports, and protocol identifiers regardless of minor variations in log formatting.
3. Automatic deduplication – stores extracted records in a set, guaranteeing each unique combination appears only once.

Note:
  """Main function to read log data, extract unique info, and export to Excel."""
  
    file_path = "12-9-25.txt"
    excel_file_path = "unique_log_report-12-9-25.txt.xlsx"

    You must add your file in the above variable. Also, you can choose the output excel file format.
