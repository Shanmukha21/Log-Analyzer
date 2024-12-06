import re
import pandas as pd

class LogAnalyzer:
    """
    A class for log file validation, parsing, and analysis.
    """
    FAILED_LOGIN_THRESHOLD = 10  # Configure threshold for failed login attempts

    @staticmethod
    def validate_log_file(file_path):
        """
        Validates the log file for basic elements (IP address, method, status, etc.).

        Args:
            file_path (str): Path to the log file.

        Returns:
            bool: True if the file is valid, False otherwise.
        """
        log_pattern = (
            r'^(?P<ip>\d+\.\d+\.\d+\.\d+) '                         # IP address
            r'- - '
            r'\[(?P<timestamp>.*?)\] '                              # Timestamp
            r'"(?P<method>[A-Z]+) (?P<endpoint>/[^ ]*) [^"]+" '     # Method and endpoint
            r'(?P<status>\d+) '                                     # HTTP status code
            r'(?P<size>\d+)(?: "(?P<message>.*?)")?$'               # Response size and optional message
        )
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if not re.match(log_pattern, line.strip()):
                        return False
            return True
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return False

    @staticmethod
    def parse_log_file_to_dataframe(file_path):
        """
        Parses the validated log file into a pandas DataFrame.

        Args:
            file_path (str): Path to the log file.

        Returns:
            pandas.DataFrame: DataFrame containing parsed log details.
        """
        log_lines = []
        log_pattern = (
            r'^(?P<ip>\d+\.\d+\.\d+\.\d+) '  # IP address
            r'- - '
            r'\[(?P<timestamp>.*?)\] '       # Timestamp
            r'"(?P<method>[A-Z]+) (?P<endpoint>/[^ ]*) [^"]+" '  # Method and endpoint
            r'(?P<status>\d+) '              # HTTP status code
            r'(?P<size>\d+)(?: "(?P<message>.*?)")?$'  # Response size and optional message
        )

        with open(file_path, 'r') as file:
            for line in file:
                match = re.match(log_pattern, line.strip())
                if match:
                    log_lines.append(match.groupdict())

        return pd.DataFrame(log_lines)

    @staticmethod
    def count_sort_req_ip(df):
        """
        Counts and sorts the number of requests made by each IP address.

        Args:
            df (pandas.DataFrame): DataFrame containing log details.

        Returns:
            pandas.DataFrame: DataFrame with IP addresses and request counts.
        """
        ip_counts = df['ip'].value_counts().reset_index()
        ip_counts.columns = ['IP Address', 'Request Count']
        return ip_counts

    @staticmethod
    def most_frequent_endpoint(df):
        """
        Identifies the most frequently accessed endpoint.

        Args:
            df (pandas.DataFrame): DataFrame containing log details.

        Returns:
            tuple: (Endpoint, access count) of the most accessed endpoint.
        """
        endpoint_counts = df['endpoint'].value_counts()
        return endpoint_counts.idxmax(), endpoint_counts.max()

    @staticmethod
    def detect_suspicious_activity(df):
        """
        Detects potential brute force attacks based on failed login attempts.

        Args:
            df (pandas.DataFrame): DataFrame containing log details.

        Returns:
            pandas.DataFrame: DataFrame with IP addresses and failed login counts exceeding the threshold.
        """
        failed_logins = df[df['status'] == '401']
        suspicious_ips = failed_logins['ip'].value_counts()
        suspicious_ips = suspicious_ips[suspicious_ips > LogAnalyzer.FAILED_LOGIN_THRESHOLD].reset_index()
        suspicious_ips.columns = ['IP Address', 'Failed Login Count']
        return suspicious_ips
