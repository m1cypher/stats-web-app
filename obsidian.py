import pandas as pd
import os
import pprint

# Imports for Obsidian
# Frontmatter Documentation https://pypi.org/project/python-frontmatter/
# Primary collection module is pyfront
import frontmatter as pyfront
from yaml.scanner import ScannerError






vault_path = r"C:\Users\emerg\OneDrive\Documents\_Mimir Cyber\Coding\Personal Projects\obsidian-notes\Journal\Daily"

def create_nested_dictionary_from_vault(directory):
    daily_dic = {}

    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)


        if os.path.isfile(file_path):
            # Remove the file extension to get the key
            date_key = os.path.splitext(filename)[0]
            

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    post = pyfront.loads(file.read())
                    daily_dic[date_key] = post.metadata
            except (UnicodeDecodeError, ScannerError) as e:
                print(f"Error in file {filename}: {e}")
                continue  # Skips the file causing the error
                # For complete data, go to the skipped files and fix the errors


    return daily_dic

result_nested_dictionary = create_nested_dictionary_from_vault(vault_path)

pprint(result_nested_dictionary["2023-12-01"]) # Test print of the nested dictionary to make sure it 


ob_df = pd.DataFrame(result_nested_dictionary).T

