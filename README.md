Here's the updated `README.md` file with the added points:

```markdown
# VRV Assignment

This repository contains a log analysis solution and a Streamlit-based web application for visualizing log data.

## Project Structure

### 1. Root Directory
- **`log_analysis.ipynb`**: A Jupyter Notebook showcasing the process of analyzing log files step-by-step. Ideal for interactive exploration.
- **`log_analysis.py`**: A standalone Python script that performs log analysis. Use this script for automated or large-scale analysis.
- **`log_analysis_results.csv`**: The log analysis output is saved as a CSV file. It includes processed insights from the sample log file.
- **`sample.log`**: A sample log file used for demonstration and testing the analysis scripts.

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
   ```
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
  - **Matplotlib/Seaborn**: For data visualization
  - Install all dependencies using `requirements.txt` if provided:
    ```bash
    pip install -r requirements.txt
    ```

---

## Future Enhancements
- Integration with real-time log monitoring systems.
- Advanced analytics like anomaly detection.
```

This updated `README.md` includes the points you mentioned. You can directly use this content. Let me know if you need further modifications!
