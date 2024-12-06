# VRV Assignment

This repository contains a log analysis solution and a Streamlit-based web application for visualizing log data.

## Project Structure

### 1. Root Directory
- **`log_analysis.ipynb`**: A Jupyter Notebook showcasing the process of analyzing log files step-by-step. Ideal for interactive exploration.
- **`log_analysis.py`**: A standalone Python script that performs log analysis. Use this script for automated or large-scale analysis.
- **`log_analysis_results.csv`**: The log analysis output is saved as a CSV file. It includes processed insights from the sample log file.
- **`sample.log`**: This is a sample log file used for demonstration and testing the analysis scripts. Added 10,000 logs to the sample logs to test the model's capability.

### 2. Streamlit_APP Directory
- **`app.py`**: The main script for the Streamlit web application. Run this script to launch the log analysis tool in a browser.
- **`utils.py`**: This file contains helper functions used by the Streamlit app to process logs and display results.
- **`temp/`**: The application uses a temporary folder to store intermediate files like uploaded logs.
  - **`sample.log`**: A placeholder log file in the `temp` folder for testing purposes.

---

## Usage Instructions

### 1. Analyzing Logs with the Jupyter Notebook
1. Open `log_analysis.ipynb` in Jupyter Notebook.
2. Follow the markdown instructions and run the cells sequentially.

### 2. Running the Python Script
1. Execute `log_analysis.py` using the command:
   ```bash
   python log_analysis.py
2. Results will be saved in `log_analysis_results.csv`.
3. Analyze the generated `log_analysis_results.csv` file to extract actionable insights.

### 3. Launching the Streamlit Application
1. Navigate to the `Streamlit_APP` directory.
2. Run the app using:
   ```bash
   streamlit run app.py
   ```
3. Upload your log files and explore the results in your browser.
4. Utilize interactive charts and filters to visualize the log data effectively.

---

## Prerequisites
- Python 3.8 or later
- Required libraries:
  - **Pandas**: For data analysis
  - **Streamlit**: For building the web application
  - **Matplotlib**: For data visualization
  - Install all dependencies using `requirements.txt` if provided:
    ```bash
    pip install -r requirements.txt
    ```

---

## Sample Input
```bash
Here is a sample log file you will use for this assignment. Save it as sample.log:
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
203.0.113.5 - - [03/Dec/2024:10:12:44 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
203.0.113.5 - - [03/Dec/2024:10:12:45 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:46 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:47 +0000] "GET /profile HTTP/1.1" 200 768
192.168.1.1 - - [03/Dec/2024:10:12:48 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:49 +0000] "POST /feedback HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:50 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.1 - - [03/Dec/2024:10:12:51 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:52 +0000] "GET /about HTTP/1.1" 200 256
203.0.113.5 - - [03/Dec/2024:10:12:53 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:54 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:55 +0000] "GET /contact HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:56 +0000] "GET /home HTTP/1.1" 200 512
192.168.1.100 - - [03/Dec/2024:10:12:57 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
203.0.113.5 - - [03/Dec/2024:10:12:58 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:59 +0000] "GET /dashboard HTTP/1.1" 200 1024
192.168.1.1 - - [03/Dec/2024:10:13:00 +0000] "GET /about HTTP/1.1" 200 256
198.51.100.23 - - [03/Dec/2024:10:13:01 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:13:02 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:13:03 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:13:04 +0000] "GET /profile HTTP/1.1" 200 768
198.51.100.23 - - [03/Dec/2024:10:13:05 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:13:06 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:13:07 +0000] "POST /feedback HTTP/1.1" 200 128
```

### Output
```bash
Request per IP Address:
   IP Address  Request Count
  203.0.113.5              15
198.51.100.23              8
  192.168.1.1              7
     10.0.0.2              6
192.168.1.100              5

Most Frequently Accessed Endpoint:
/login (Accessed 13 times)

Suspicious Activity Detected:
 IP Address  Failed Login Count
203.0.113.5                   15
```



