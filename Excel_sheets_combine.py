import pandas as pd

def combine_columns_from_all_sheets(file_path, columns_to_extract, output_file):

    # Read the Excel file and get all sheet names
    xls = pd.ExcelFile(file_path)
    combined_df = pd.DataFrame(columns=columns_to_extract)

    # Iterate over all sheet names
    for sheet_name in xls.sheet_names:
        sheet_df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        
        # Create a temporary DataFrame to store valid columns
        temp_df = pd.DataFrame()

        # Extract specified columns
        for column in columns_to_extract:
            if column in sheet_df.columns:
                temp_df[column] = sheet_df[column]
            else:
                print(f"Column '{column}' not found in sheet '{sheet_name}'")
        
        # Append the temp_df to combined_df
        combined_df = pd.concat([combined_df, temp_df], axis=0, ignore_index=True)

    # Format date columns
    for date_column in date_columns:
        if date_column in combined_df.columns:
            combined_df[date_column] = pd.to_datetime(combined_df[date_column], errors='coerce').dt.strftime('%d-%m-%y')
        else:
            print(f"Date column '{date_column}' not found in combined data")
    
    combined_df.to_excel(output_file, index=False)
    print(f"Combined data saved to {output_file}")

# Example usage
file_path = 'HR_lotteria_2024.xlsx'
columns_to_extract = ['ID', 'Name', 'Department', 'Position', 'Branch', 'Location', 'Join Date', 'Service Year', 'Resign Date', 'Termination', 'Reason']
date_columns = ['Join Date', 'Resign Date']

output_file = 'HR_2024_output.xlsx'


combine_columns_from_all_sheets(file_path, columns_to_extract, output_file)
