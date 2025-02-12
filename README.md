# Log Analyzer

This repository contains a comprehensive log analysis solution, which includes a Jupyter Notebook for step-by-step log file analysis, a standalone Python script for automated analysis, and a Streamlit-based web application for interactive log data visualization.

## Project Structure

### 1. Root Directory
- **`log_analysis.py`**: A standalone Python script that automates log file analysis. This script processes log data and generates insights in a CSV format for large-scale or batch analysis.
- **`log_analysis_results.csv`**: The log analysis output is saved as a CSV file. It includes processed insights, such as request counts, most accessed endpoints, and suspicious activity detected.
- **`sample.log`**: This is a sample log file containing 10,000 entries. It is used for testing and demonstration purposes to show the capabilities of the analysis solution.

### 2. Streamlit_APP Directory
- **`app.py`**: The main script for the Streamlit web application. Run this script to launch the log analysis tool in a web browser, allowing users to upload log files and view interactive visualizations.
- **`utils.py`**: This file contains helper functions used by the Streamlit app to process log data, generate insights, and display results in visual formats like charts and graphs.
- **`temp/`**: A temporary directory where uploaded log files are stored for processing within the Streamlit app. It also includes a placeholder `sample.log` for testing.

---

## Usage Instructions

### 1. Running the Python Script
1. To run the automated log analysis script, execute the `log_analysis.py` script using the following command:
   ```bash
   python log_analysis.py
   ```
2. The script will process the log file and generate insights, which will be saved in a CSV file named `log_analysis_results.csv`.
3. You can analyze the results in the CSV file to extract actionable insights, such as IP address request counts and detected suspicious activity.

### 2. Launching the Streamlit Application
1. Navigate to the `Streamlit_APP` directory.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the Streamlit application by running:
   ```bash
   streamlit run app.py
   ```
4. In your web browser, you can upload log files to analyze and explore the results interactively.
5. The app allows you to generate and view visualizations such as request counts per IP address, most frequently accessed endpoints, and failed login attempt heatmaps.

---

## Key Features

### 1. Log Analysis in Jupyter Notebook
The `log_analysis.ipynb` notebook provides an interactive approach to log file analysis. You can perform the following tasks:
- **Requests per IP Address**: View the number of requests made by each IP address.
- **Most Frequently Accessed Endpoint**: Identify which endpoint was accessed the most in the log file.
- **Suspicious Activity Detection**: Detect suspicious activity, such as repeated failed login attempts from the same IP address.

### 2. Visualizations in Streamlit
The Streamlit app (`app.py`) allows you to visualize the log data interactively. The following graphs and charts are available:
- **Requests per IP Address**: A bar chart displaying the number of requests per IP address.
- **Most Frequently Accessed Endpoint**: A simple text display showing the most accessed endpoint and its count.
- **Failed Login Attempts Heatmap**: A heatmap showing the failed login attempts over time to detect patterns.
- **Request Counts Over Time**: A line chart that shows how the number of requests fluctuates over time.

These visualizations help you quickly identify patterns, trends, and potential security threats in the log data.

---

## Prerequisites
- Python 3.8 or later
- Required libraries:
  - **Pandas**: For data analysis and manipulation.
  - **Streamlit**: For building the interactive web application.
  - **Matplotlib**: For generating plots and graphs.
  - **Seaborn**: For creating heatmaps.

To install the dependencies, you can use the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## Sample Input

Here is an example of the log file format that the tools in this repository expect:

```bash
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:37 +0000] "GET /contact HTTP/1.1" 200 312
198.51.100.23 - - [03/Dec/2024:10:12:38 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:39 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:40 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:41 +0000] "GET /dashboard HTTP/1.1" 200 1024
198.51.100.23 - - [03/Dec/2024:10:12:42 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:43 +0000] "GET /dashboard HTTP/1.1" 200 1024
```

### Output for the **loganalysis.py**

#### Request per IP Address
```bash
   IP Address      Request Count
  203.0.113.5             15
  198.51.100.23           8
  192.168.1.1             7
  10.0.0.2                6
  192.168.1.100           5
```

#### Most Frequently Accessed Endpoint
```bash
Endpoint: /login (Accessed 13 times)
```

#### Suspicious Activity Detected (Failed Login Attempts)
```bash
   IP Address      Failed Login Count
  203.0.113.5             15
```
### Output for Streamlit app
#### **Requests over time** *Time Series Plot (Line Plot)*
- This graph visualizes the number of requests over time, where the x-axis represents time (down to the minute), and the y-axis represents the count of requests. It helps track how the number of requests changes over time.
![image](https://github.com/user-attachments/assets/5b619efb-9dde-4ba6-95ae-ee79359c6078)

#### **Status code Distribution** *Bar Chart*
- This graph displays the distribution of HTTP status codes (e.g., 200, 404, 401) and their frequency. The x-axis represents different HTTP status codes, and the y-axis represents the count of occurrences for each status code.
![image](https://github.com/user-attachments/assets/c8547010-cad4-48bd-a11a-15c13649cdd1)

#### **Failed Login Attempts** *Heatmap*
- This graph visualizes failed login attempts (HTTP status code 401) in a heatmap format. The heatmap shows the frequency of failed login attempts by the hour of the day and day of the week. It helps identify patterns or peak times for failed logins.
![image](https://github.com/user-attachments/assets/89dc86d8-c179-454f-be57-17fc4c29c945)

#### **Endpoint Access** *Bar Chart*
- This graph shows the frequency of access for each endpoint in the log data. The x-axis represents different endpoints, and the y-axis represents the count of accesses for each endpoint.
![image](https://github.com/user-attachments/assets/d36c94d2-2658-4ef3-b04a-be7d4f44e8ab)


- **Line Plot** for visualizing time-based request trends.
- **Bar Chart** for visualizing HTTP Status code distributions and Endpoint access frequencies.
- **Heatmap** for visualizing the distribution of failed login attempts across time (hour and day)







