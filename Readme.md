Input File:
1. Is an excel for eg. Verb_paradigm_kara.xlsx pasted in the same folder as that of script/ given with correct path as argument.

Output File:
1. It is a text file with output in tagged format.
2. Also, the output is appended under <pardefs></pardefs> tag in apertium_ben_in_canonical_forms.dix

Steps of execution:
1. Optional - Paste your input excel sheet in the Automate_bangla_dix_generation folder
2. Run the following command -
**python main.py path_to_input_excel**

where main.py - is the script name
path_to_input_excel - denotes the input file excel sheet. If it is pasted in the same folder as script, only give name_of_excel.xlsx otherwise give proper path to the excel file.

for eg. 
**python main.py Verb_paradigm_kara.xlsx**
