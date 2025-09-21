# Extract_Syslogs_Data
A lightweight Python utility that parses raw syslog files and extracts the most relevant network‑traffic fields:

1. Source IP
2. Destination IP
3. Destination Port
4. Protocol (TCP, UDP, ICMP, …)
   
The script also deduplicates identical entries, ensuring a clean output.

1. Input: Plain‑text (.txt) file with one syslog line per row.
2. Output: Comma‑Separated Values (.csv) file ready for Excel, Google Sheets, or any downstream analysis tool.

✨ Key Features
1. Simple usage – just point it at a .txt log file.
2. Robust parsing – uses regular expressions to locate IPv4 addresses, ports, and protocol identifiers regardless of minor variations in log formatting.
3. Automatic deduplication – stores extracted records in a set, guaranteeing each unique combination appears only once.

