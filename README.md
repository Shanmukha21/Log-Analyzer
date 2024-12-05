# Log File Analyzer

This project provides a tool to analyze web server log files for useful insights, including request counts by IP, the most frequently accessed endpoint, and detection of suspicious activities such as potential brute force attacks based on failed login attempts. The analyzer parses log files, validates them, and produces CSV reports.

## Features

- **Log File Validation**: Ensures the log file contains necessary elements such as IP address, timestamp, request method, endpoint, status code, and response size.
- **IP Address Request Count**: Identifies how many requests were made by each IP address.
- **Most Frequently Accessed Endpoint**: Finds the most frequently accessed endpoint in the log file.
- **Suspicious Activity Detection**: Detects potential brute force attacks based on failed login attempts (HTTP 401 status codes).
- **CSV Output**: Saves the analysis results into a CSV file in a structured format.

## Requirements

- Python 3.x
- pandas (`pip install pandas`)
- Streamlit (`pip install straemlit`) (Optional)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Shanmukha21/log-analyzer.git
   cd log-analyzer

## Command to run Streamlit app `streanmlit run app.py`
