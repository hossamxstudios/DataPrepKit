# DataPrepKit

DataPrepKit is a Python package designed to simplify the preprocessing of datasets, providing a comprehensive toolkit for data cleaning, summarization, and transformation.

## Key Features
- **Data Reading**: Easily read data from various file formats such as CSV, Excel, and JSON.
- **Missing Value Handling**: Effortlessly handle missing values by removing or imputing them using customizable strategies.
- **Summary Statistics**: Calculate essential statistical summaries for your data, including mean, median, and mode.
- **Categorical Data Encoding**: Encode categorical data into numerical formats for analysis.
- **Package Deployment**: Follow PyPI guidelines for seamless deployment and accessibility.


# Usage

To use DataPrepKit, follow these steps:
1. **Read Data from a File:**
    - Run the `read_data()` function, which prompts you to enter the file path of your data. The function automatically detects the file format and reads the data accordingly.

2. **Check for Missing Values:**
    - After reading the data, you can check for missing values by running the `check_missing_values(data)` function. This function gives you options to handle missing values, including removing rows or imputing missing values.

3. **Perform Summary Statistics:**
    - To calculate summary statistics for a specific column, use the `calculate_summary_stats(data, column_name)` function. Enter the name of the column you want to analyze, and the function will return statistics such as mean, median, and mode.

4. **Encode Categorical Columns:**
    - If you have categorical columns that need to be encoded, run the `ordinal_encode(data)` function. This function prompts you to choose a column and encodes its categories into numerical values.

5. **Repeat or Exit:**
    - After performing any of the above steps, you can choose to repeat the process for another task or exit the program by entering the corresponding number.

## Installation

You can install DataPrepKit via pip:

```bash
pip install dataprepkit


