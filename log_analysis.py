"""
Web Server Log Analyzer
Analyzes web server logs to track traffic patterns and detect security threats.
Generates reports in CSV 
Author: Ghadiyaram Shanmukhasai Sreenivas
"""


import re
import csv
import pandas as pd
from collections import defaultdict

# Configure Threshold for flagging suspicious activity (eg. Brute force login attempts)
FAILED_LOGIN_THRESHOLD = 10


def validate_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if not re.search(r'\d+\.\d+\.\d+\.\d+', line):
                print(f"Invalid log format: Missing IP in line -> {line}")
                return False
            if not re.search(r'"(GET|POST|PUT|DLETE|OPTIONS|HEAD)', line):
                print(f"Invalid log format: Missing HTTP method in line -> {line}")
                return False
    print("Log file validation passed")
    return True


def parse_log_file(file_path):
    """
    Reads the log file and returns its lines.

    Args: 
        file_path (str): Path to the log file

    Returns: 
        pd.DataFrame: DataFrame containing parsed log details.
    """
    data = []
    log_pattern = (
        r'^(?P<ip>\d+\.\d+\.\d+\.\d+) '                         
        r'- - '
        r'\[(?P<timestamp>[^\]]+)\] '                           
        r'"(?P<method>[A-Z]+) (?P<endpoint>/[^ ]*) [^"]+" '     
        r'(?P<status>\d+) '                                     
        r'(?P<size>\d+)(?: "(?P<message>[^"]*)")?$'             
    )
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(log_pattern, line.strip())
            if match:
                data.append(match.groupdict())
    
    if not data:
        print("No valid log entries found")
        return pd.DataFrame()
    
    return pd.DataFrame(data)

def count_sort_req_ip(df):
    """
    Counts the number of requests made by each IP address.
    
    Args:
        df (pd.DataFrame): DataFrame containing log details.

    
    Returns:
        pd.DataFrame: DataFrame with IP addresses and request counts.
    """
    ip_counts = df['ip'].value_counts().reset_index()
    ip_counts.columns = ['IP Address', 'Request Count']
    return ip_counts
    


def most_frequent_endpoint(df):
    """
    Identifies the most frequently accessed endpoint.
    
    Args:
        df (pd.DataFrame): DataFrame containing log details.
    
    Returns:
        list: [Endpoint, access count] of the most accessed endpoint.
    """
    endpoint_counts = df['endpoint'].value_counts()
    return [endpoint_counts.idxmax(), endpoint_counts.max()]  # Return as a list
 

def detect_suspicious_activity(df):
    """
    Detects potential brute force attacks based on failed login attempts.
    
    Args:
        df (pd.DataFrame): DataFrame containing log details.

    Returns:
        pd.DataFrame: DataFrame with IP addresses and failed login counts exceeding the threshold.
    """
    
    failed_logins = df[df['status'] == '401']  # Filter failed login attempts
    flagged_ips = failed_logins['ip'].value_counts()
    flagged_ips = flagged_ips[flagged_ips > FAILED_LOGIN_THRESHOLD].reset_index()
    flagged_ips.columns = ['IP Address', 'Failed Login Count']
    return flagged_ips

def save_results_to_csv(ip_req, most_accessed, flagged_ips, output_file='log_analysis_results.csv'):
    """
    Saves analysis results to a CSV file.
    
    Args:
        ip_req (pd.DataFrame): DataFrame with IP request counts.
        most_accessed (list): List containing the most accessed endpoint and its count, e.g. ['/search', 1478].
        flagged_ips (pd.DataFrame): DataFrame with suspicious IPs and failed login counts.
        output_file (str): File name for the CSV output.
    """

    try:
        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            # Writing the IP Request section
            writer.writerow(["IP Requests:"])
            ip_req.to_csv(csvfile, index=False)

            # Write a newline to separate sections
            csvfile.write("\n")

            # Writing the Most Accessed Endpoint section
            writer.writerow(["Most Frequently Accessed Endpoint:"])
            most_accessed_text = f"{most_accessed[0]} (Accessed {most_accessed[1]} times)"
            writer.writerow([most_accessed_text])

            # Write a newline to separate sections
            csvfile.write("\n")

            # Writing the Suspicious Activity section
            writer.writerow(["Suspicious Activity:"])
            flagged_ips.to_csv(csvfile, index=False)

        print(f"Results saved to {output_file}")
    
    except Exception as e:
        print(f"Error while saving to CSV: {e}")



def main():
    """
    Main function to execute the log analysis script.
    """
    log_file = 'sample_small.log'
    # Parse log file into DF
    df = parse_log_file(log_file)
    if df.empty:
        print("No data available for analysis.")
        return
    
    # Validating the logfile
    val = validate_log_file(log_file)
    if not val:
        print(val)
        return
    print(val)
    

    # Perform Analysis
    ip_req = count_sort_req_ip(df)
    most_accessed = most_frequent_endpoint(df)
    flagged_ips = detect_suspicious_activity(df)

    # Display results
    print("Request per IP Address:")
    print(ip_req.to_string(index=False))

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

    print("\nSuspicious Activity Detected:")
    if not flagged_ips.empty:
        print(flagged_ips.to_string(index=False))
    else:
        print("No suspicious activity detected.")

    # Save results to a CSV file
    save_results_to_csv(ip_req, most_accessed, flagged_ips)


if __name__ == "__main__":
    main()
