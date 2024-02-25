import pandas as pd
import numpy as np
from scipy.stats import mode

def read_data():
    try:
        file_path = input("Hey there! Please enter the file path of your data: ").strip()
        file_extension = file_path.split(".")[-1].lower()
        if file_extension == "csv":
            data = pd.read_csv(file_path)
        elif file_extension in ["xlsx", "xls"]:
            data = pd.read_excel(file_path)
        elif file_extension == "json":
            data = pd.read_json(file_path)
        else:
            print(f"Oops! It seems like I don't support '{file_extension}' file format yet.")
            return None
        return data
    except FileNotFoundError:
        print(f"Hmm...I couldn't find the file '{file_path}'. Please double-check the path and try again.")
        return None
    except Exception as e:
        print(f"Oh no! Something went wrong while reading the file: {e}")
        return None
    
def handle_missing_values(data):
    while True:
        print("\nWhat would you like to do with missing values?")
        print("1. Remove rows with missing values")
        print("2. Fill in missing values")
        print("3. Skip this step")
        
        choice = input("Enter the number of your choice: ").strip()
        
        if choice == '1':
            data_cleaned = data.dropna()
            print("Done! I've removed the rows with missing values from your data.")
            return data_cleaned
        elif choice == '2':
            while True:
                print("\nOkay! How would you like to fill in the missing values?")
                print("1. Fill numeric columns with the mean")
                print("2. Fill numeric columns with the median")
                print("3. Fill numeric columns with the mode")
                print("4. Fill text columns with the most frequent value")
                print("5. Fill text columns with a constant value")
                print("6. Go back to the main menu")
                impute_choice = input("Enter the number of your choice: ").strip()
                if impute_choice == '1':
                    numeric_strategy = 'mean'
                    break
                elif impute_choice == '2':
                    numeric_strategy = 'median'
                    break
                elif impute_choice == '3':
                    numeric_strategy = 'mode'
                    break
                elif impute_choice == '4':
                    text_strategy = 'most_frequent'
                    break
                elif impute_choice == '5':
                    text_strategy = 'constant'
                    constant_value = input("Please enter the constant value for filling text columns: ").strip()
                    break
                elif impute_choice == '6':
                    return data
                else:
                    print("Oops! That's an invalid choice. Please enter a number from 1 to 6.")

            data_cleaned = data.copy()
            if 'numeric_strategy' in locals():
                data_cleaned = data_cleaned.fillna(data_cleaned.select_dtypes(include=['number']).agg(numeric_strategy))
            if 'text_strategy' in locals():
                if text_strategy == 'most_frequent':
                    data_cleaned = data_cleaned.fillna(data_cleaned.select_dtypes(exclude=['number']).mode().iloc[0])
                elif text_strategy == 'constant':
                    data_cleaned = data_cleaned.fillna(constant_value)
            print("Done! I've filled in the missing values in your data.")
            return data_cleaned
        elif choice == '3':
            print("Alright! Let's move on.")
            return data
        else:
            print("Oops! That's an invalid choice. Please enter a number from 1 to 3.")

    
def check_missing_values(data):
    if data.isna().sum().sum() > 0:
        print("It looks like there are missing values in your data.")
        while True:
            print("\nWhat would you like to do?")
            print("1. Handle missing values")
            print("2. Show only rows with missing values")
            choice = input("Enter the number of your choice: ").strip()
            if choice == '1':
                return handle_missing_values(data)
            elif choice == '2':
                missing_rows = data[data.isna().any(axis=1)]
                print("Here are the rows containing missing values:")
                print(missing_rows)
            else:
                print("Oops! That's an invalid choice. Please enter '1' or '2'.")
    else:
        print("Great news! There are no missing values in your data.")
        return data
    
def calculate_summary_stats(data, column_name):
    if column_name not in data.columns:
        print(f"Hmm...I couldn't find the column '{column_name}' in your data.")
        return None
    column_data = data[column_name]
    if np.issubdtype(column_data.dtype, np.number):
        column_data = column_data.fillna(0)
        summary_stats = {
            'mean': np.mean(column_data),
            'median': np.median(column_data),
            'standard deviation': np.std(column_data)
        }
    else:
        column_data = column_data.fillna(None)
        mode_result = mode(column_data)
        if np.isnan(mode_result.mode[0]):
            mode_val = "NaN"
        else:
            mode_val = mode_result.mode[0]
        summary_stats = {
            'mode': mode_val
        }

    return summary_stats

def ordinal_encode(data):
    print("Here are the columns in your data:")
    for column in data.columns:
        print(column)
    column_name = input("Which column would you like to encode? ").strip()
    while column_name not in data.columns:
        print(f"Oops! It seems like '{column_name}' is not a valid column name.")
        column_name = input("Please enter another column name: ").strip()
    categories = data[column_name].unique()
    encoding_map = {cat: idx for idx, cat in enumerate(categories)}
    data_encoded = data.copy()
    data_encoded[column_name] = data_encoded[column_name].map(encoding_map)   
    print("Done! I've encoded the column for you.")
    return data_encoded
    
def main():
    print("Welcome! Let's get started.")
    data = read_data()
    if data is None:
        print("Sorry, I couldn't proceed without the data. Exiting...")
        return
    while True:
        print("\nWhat would you like to do next?")
        print("1. Check for missing values")
        print("2. Perform summary statistics for a column")
        print("3. Encode a categorical column")
        print("4. Exit")
        choice = input("Enter the number of your choice: ").strip()
        if choice == '1':
            check_missing_values(data)
        elif choice == '2':
            print("Here are the columns in your data:")
            print(data.columns)
            column_name = input("Which column would you like to analyze? ").strip()
            summary_stats = calculate_summary_stats(data, column_name)
            if summary_stats:
                print(f"Here are the summary statistics for column '{column_name}':")
                for stat, value in summary_stats.items():
                    print(f"{stat.capitalize()}: {value}")
        elif choice == '3':
            data = ordinal_encode(data)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Oops! That's an invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
