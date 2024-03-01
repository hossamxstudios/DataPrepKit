#  HossamDataPrepKit 


# Description
HossamDataPrepKit is a Python package designed to streamline the data preparation process by providing various functions for data cleaning, handling missing values, and calculating summary statistics. It simplifies data preprocessing tasks, making it easier for data scientists and analysts to prepare their datasets for analysis and modeling.

# Key Features
- Read data from CSV, Excel, or JSON files with a simple interface.
- Check for missing values and provide options to handle them, including removal or imputation.
- Calculate summary statistics for numeric columns, such as mean, mode, median, highest value, and most frequent value.
- Encode categorical columns into ordinal values for machine learning tasks.
- Easy-to-use functions with clear prompts and error handling for improved user experience.

# Installation
### You can install XDataPrepKitX using pip:
@pip install HossamDataPrepKit

# Usage
import HossamDataPrepKit as hdpk

# Example:
## Read data from a CSV file
data = hdpk.read_data()
--- the user will be asked to enter file path

## Check for missing values and handle them
cleaned_data = hdpk.check_missing_values(data)

## Calculate summary statistics for a specific column
summary_stats = hdpk.calculate_summary_stats(data)
-- the user will be asked to choose a column from the table

## Encode categorical column into ordinal values
encoded_data = hdpk.ordinal_encode(data)

# Contributors
Hossam Farid - @hossamxstudios

# License
This project is licensed under the MIT License - see the LICENSE file for details.
