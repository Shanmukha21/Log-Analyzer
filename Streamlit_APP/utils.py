import re
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns



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

class Visualizations:
    
    @staticmethod
    def visualize_req_over_time(df):
        """Visualize requests over time."""
        try:
            df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S %z')
        except Exception as e:
            st.error(f"Error parsing timestamps: {e}")
            return

        requests_per_minute = df.set_index('timestamp').resample('T').size()

        plt.figure(figsize=(10, 6))
        requests_per_minute.plot()
        plt.title("Requests Over Time")
        plt.xlabel("Time")
        plt.ylabel("Number of Requests")
        plt.grid(True)
        st.pyplot(plt)


    @staticmethod
    def visualize_status_code_distribution(df):
        """Visualize HTTP status code distribution."""
        status_counts = df['status'].value_counts()

        plt.figure(figsize=(8, 5))
        status_counts.plot(kind='bar', color='skyblue')
        plt.title("HTTP Status Code Distribution")
        plt.xlabel("HTTP Status Code")
        plt.ylabel("Count")
        plt.grid(True)
        st.pyplot(plt)


    @staticmethod
    def visualize_failed_login_heatmap(df):
        """Visualize failed login attempts as a heatmap."""
        try:
            # Parse the timestamp column with a specific format
            df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S %z')
        except Exception as e:
            st.error(f"Error parsing timestamps: {e}")
            return

        # Filter for failed logins (HTTP status 401)
        failed_logins = df[df['status'] == '401']

        if failed_logins.empty:
            st.write("No failed login attempts detected.")
            return

        # Extract day and hour for heatmap
        failed_logins['hour'] = failed_logins['timestamp'].dt.hour
        failed_logins['day'] = failed_logins['timestamp'].dt.strftime('%A')

        # Create pivot table
        heatmap_data = failed_logins.pivot_table(index='day', columns='hour', aggfunc='size', fill_value=0)

        # Plot heatmap
        plt.figure(figsize=(12, 6))
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='coolwarm')
        plt.title("Failed Login Attempts by Hour and Day")
        plt.xlabel("Hour of Day")
        plt.ylabel("Day of Week")
        st.pyplot(plt)

    @staticmethod
    def visualize_endpoint_access(df):
        """Visualize endpoint access counts."""
        endpoint_counts = df['endpoint'].value_counts()

        plt.figure(figsize=(10, 6))
        endpoint_counts.plot(kind='bar', color='purple')
        plt.title("Endpoint Access Frequency")
        plt.xlabel("Endpoints")
        plt.ylabel("Access Count")
        plt.grid(True)
        st.pyplot(plt)
