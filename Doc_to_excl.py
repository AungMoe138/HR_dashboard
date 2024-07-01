from docx import Document
import pandas as pd

# Function to extract tables from a Word document
def extract_tables(doc_path):
    doc = Document(doc_path)
    all_data = []
    header = None
    
    # Iterate through the tables and append to the list
    for table in doc.tables:
        for i, row in enumerate(table.rows):
            if i == 0:
                # Capture the header from the first table
                if header is None:
                    header = [cell.text.strip() for cell in row.cells]
            else:
                row_data = [cell.text.strip() for cell in row.cells]
                all_data.append(row_data)
    
    # Create DataFrame
    df = pd.DataFrame(all_data, columns=header)
    return df

# Function to save DataFrame to Excel
def save_to_excel(df, output_path):
    df.to_excel(output_path, index=False, sheet_name='Combined_Tables')

# Main execution
doc_path = 'D:\Python101\Recruitment2024.docx'  # Update with your document path
output_path = 'D:\Python101\Recruitment_excel_2024.xlsx'  # Update with your desired output path

df = extract_tables(doc_path)
save_to_excel(df, output_path)

print(f"Tables extracted and saved to {output_path}")
