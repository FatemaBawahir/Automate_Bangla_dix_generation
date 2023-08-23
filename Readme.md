Input File:
1. Is an excel for eg. - Verb_paradigm.xlsx pasted in the same folder as that of script
2. The input excel sheet can have sub sheets.

Output File:
1. It is a text file with output in tagged format

Steps of execution:
1. Paste your input excel sheet in the Automate_bangla_dix_generation folder
2. Go to main.py and update -
   1. file_path = '**excel_sheet_name.xlsx**'
   
      df = pd.read_excel(file_path, sheet_name='**sub_sheet name**')
   
   2. for eg. file_path = 'Verb_paradigm.xlsx' 
      
      df = pd.read_excel(file_path, sheet_name='kara')
3. Run the following command -
**python main.py prefix**

where main.py - is the script name
prefix - denotes the variable part for which dix generation is done

for eg. 
**python main.py kar**
