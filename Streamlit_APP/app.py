"""
Web Server Log Analyzer
Analyzes web server logs to track traffic patterns and detect security threats.
Generates reports in CSV 
Author: Ghadiyaram Shanmukhasai Sreenivas
"""

import os
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils import LogAnalyzer, Visualizations

def main():
    st.title("Log File Analysis Tool")
    st.write("Upload a log file to perform analysis.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a log file", type=["log"])

    if uploaded_file is not None:
        # Ensure 'temp' directory exists
        os.makedirs("temp", exist_ok=True)

        # Save uploaded file temporarily
        file_path = f"temp/{uploaded_file.name}"
        with open(file_path, "wb") as file:
            file.write(uploaded_file.read())

        # Validate log file
        if not LogAnalyzer.validate_log_file(file_path):
            st.error("The log file is invalid. Please upload a valid log file.")
            return

        # Parse log file
        df = LogAnalyzer.parse_log_file_to_dataframe(file_path)

        # Visualization Buttons
        st.subheader("Visualization")
        col1, col2, col3, col4 = st.columns(4)  # Arrange buttons in a row
        with col1:
            if st.button("Requests Over Time"):
                Visualizations.visualize_req_over_time(df)
        with col2:
            if st.button("Status Code Distribution"):
                Visualizations.visualize_status_code_distribution(df)
        with col3:
            if st.button("Failed Login Attempts"):
                Visualizations.visualize_failed_login_heatmap(df)
        with col4:
            if st.button("Endpoint Access"):
                Visualizations.visualize_endpoint_access(df)

        # Display raw data
        st.subheader("Log File Data")
        st.dataframe(df)

        # Analysis: Requests per IP Address
        st.subheader("Requests per IP Address")
        ip_counts = LogAnalyzer.count_sort_req_ip(df)
        st.table(ip_counts)

        # Analysis: Most Frequently Accessed Endpoint
        st.subheader("Most Frequently Accessed Endpoint")
        most_accessed = LogAnalyzer.most_frequent_endpoint(df)
        st.write(f"**Endpoint:** {most_accessed[0]} (Accessed {most_accessed[1]} times)")

        # Analysis: Suspicious Activity Detection
        st.subheader("Suspicious Activity Detected")
        suspicious_ips = LogAnalyzer.detect_suspicious_activity(df)
        if not suspicious_ips.empty:
            st.table(suspicious_ips)
        else:
            st.write("No suspicious activity detected.")


if __name__ == "__main__":
    main()
