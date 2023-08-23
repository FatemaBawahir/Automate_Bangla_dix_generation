import sys
import pandas as pd

DIX = "apertium_ben_in_canonical_forms.dix"

person_info_dict ={
        "first_person_val" : "u",
        "second_person_tucCartha_val" : "m_h0",
        "second_person_val" : "m_h1",
        "second_person_honorific_val" : "m_h2",
        "third_person_val" : "a",
        "third_person_honorific_val" : "a_h"
    }

def fetch_tam_data(tam):
    tam_val = []
    tam_info = tam.split('-', 1)
    for i in range(len(tam_info)):
        if i == 0:
            temp = 'tam:' + tam_info[i]
            tam_val.append(temp)
        else:
            additional_data = tam_info[1].strip('()')
            additional_data_lst = additional_data.split(' ')
            additional_data_lst.reverse()
            for ele in additional_data_lst:
                ele_list = ele.split('=')
                temp = ele_list[0] + ':' + ele_list[1]
                tam_val.append(temp)

    return tam_val

def write_output(output):
    file_path = 'output.txt'
    with open(file_path, 'w') as file:
        file.write(output)
        file.close()

def update_dix(output):
    with open(DIX, 'r') as file:
        xml_content = file.read()

    # Specify the tag you want to find and append text after
    target_tag = "pardefs"

    # Find the index of the target tag's closing bracket
    target_start = xml_content.find(f"<{target_tag}>")
    target_end = xml_content.find(f"</{target_tag}>", target_start)

    if target_start != -1 and target_end != -1:
        # Insert the new text after the closing bracket of the target tag
        modified_content = (
                xml_content[:target_start + len(target_tag) + 3] + "\n"
                + text_to_append
                + xml_content[target_start + len(target_tag) + 3:]
        )

        # Save the modified content back to the file
        with open(DIX, 'w') as file:
            file.write(modified_content)
    else:
        print(f"Target tag '{target_tag}' not found in the Dix.")

def fetch_first_person_dix_entry(first_person_val, category_val, line):
    dix_entry_lst = []
    if (isinstance(first_person_val, str) and first_person_val.lower() != 'nan'):
        postfix_lst = first_person_val.split('/')
        for postfix in postfix_lst:
            # remove kar
            postfix = postfix[prefix_len:]
            person_info = person_info_dict["first_person_val"]
            dix_entry = f"<e><p><l>{postfix}</l><r>a<s n=\"cat:{category_val}\"/><s n=\"per:{person_info}\"/>"
            dix_entry = dix_entry + line
            if len(dix_entry):
                dix_entry_lst.append(dix_entry)
    return dix_entry_lst

def fetch_second_person_tucCartha_dix_entry(second_person_tucCartha_val, category_val, line):
    dix_entry_lst = []
    if (isinstance(second_person_tucCartha_val, str) and second_person_tucCartha_val.lower() != 'nan'):
        postfix_lst = second_person_tucCartha_val.split('/')
        for postfix in postfix_lst:
            # remove kar
            postfix = postfix[prefix_len:]
            person_info = person_info_dict["second_person_tucCartha_val"]
            dix_entry = f"<e><p><l>{postfix}</l><r>a<s n=\"cat:{category_val}\"/><s n=\"per:{person_info}\"/>"
            dix_entry = dix_entry + line
            if len(dix_entry):
                dix_entry_lst.append(dix_entry)
    return dix_entry_lst

def fetch_second_person_dix_entry(second_person_val, category_val, line):
    dix_entry_lst = []
    if (isinstance(second_person_val, str) and second_person_val.lower() != 'nan'):
        postfix_lst = second_person_val.split('/')
        for postfix in postfix_lst:
            # remove kar
            postfix = postfix[prefix_len:]
            person_info = person_info_dict["second_person_val"]
            dix_entry = f"<e><p><l>{postfix}</l><r>a<s n=\"cat:{category_val}\"/><s n=\"per:{person_info}\"/>"
            dix_entry = dix_entry + line
            if len(dix_entry):
                dix_entry_lst.append(dix_entry)
    return dix_entry_lst

def fetch_second_person_honorific_dix_entry(second_person_honorific_val, category_val, line):
    dix_entry_lst = []
    if (isinstance(second_person_honorific_val, str) and second_person_honorific_val.lower() != 'nan'):
        postfix_lst = second_person_honorific_val.split('/')
        for postfix in postfix_lst:
            # remove kar
            postfix = postfix[prefix_len:]
            person_info = person_info_dict["second_person_honorific_val"]
            dix_entry = f"<e><p><l>{postfix}</l><r>a<s n=\"cat:{category_val}\"/><s n=\"per:{person_info}\"/>"
            dix_entry = dix_entry + line
            if len(dix_entry):
                dix_entry_lst.append(dix_entry)
    return dix_entry_lst

def fetch_third_person_dix_entry(third_person_val, category_val, line):
    dix_entry_lst = []
    if (isinstance(third_person_val, str) and third_person_val.lower() != 'nan'):
        postfix_lst = third_person_val.split('/')
        for postfix in postfix_lst:
            # remove kar
            postfix = postfix[prefix_len:]
            person_info = person_info_dict["third_person_val"]
            dix_entry = f"<e><p><l>{postfix}</l><r>a<s n=\"cat:{category_val}\"/><s n=\"per:{person_info}\"/>"
            dix_entry = dix_entry + line
            if len(dix_entry):
                dix_entry_lst.append(dix_entry)
    return dix_entry_lst

def fetch_third_person_honorific_dix_entry(third_person_honorific_val, category_val, line):
    dix_entry_lst = []
    if (isinstance(third_person_honorific_val, str) and third_person_honorific_val.lower() != 'nan'):
        postfix_lst = third_person_honorific_val.split('/')
        for postfix in postfix_lst:
            # remove kar
            postfix = postfix[prefix_len:]
            person_info = person_info_dict["third_person_honorific_val"]
            dix_entry = f"<e><p><l>{postfix}</l><r>a<s n=\"cat:{category_val}\"/><s n=\"per:{person_info}\"/>"
            dix_entry = dix_entry + line
            if len(dix_entry):
                dix_entry_lst.append(dix_entry)
    return dix_entry_lst

def fetch_no_person_dix_entry(no_person_val, category_val, line):
    dix_entry_lst = []
    if (isinstance(no_person_val, str) and no_person_val.lower() != 'nan'):
        postfix_lst = no_person_val.split('/')
        for postfix in postfix_lst:
            # remove kar
            postfix = postfix[prefix_len:]
            dix_entry = f"<e><p><l>{postfix}</l><r>a<s n=\"cat:{category_val}\"/>"
            dix_entry = dix_entry + line
            if len(dix_entry):
                dix_entry_lst.append(dix_entry)
    return dix_entry_lst

if __name__ == '__main__':
    # Update the file_path and sheet_name as per requirement
    file_path = 'Verb_paradigm.xlsx'
    df = pd.read_excel(file_path, sheet_name='kara')

    global prefix_len
    prefix = sys.argv[1]
    prefix_len = len(prefix)
    HEADER = "<pardef n=\"kar/a__v\">"
    FOOTER = "</pardef>"

    col_names = df.columns.tolist()
    # rename column names
    category = col_names[1]
    tam = col_names[2]
    first_person = col_names[3]
    second_person_tucCartha = col_names[4]
    second_person = col_names[5]
    second_person_honorific = col_names[6]
    third_person = col_names[7]
    third_person_honorific = col_names[8]
    no_person = col_names[9]

    # fetch all column values as lists
    category_lst = df[category].tolist()
    tam_lst = df[tam].tolist()
    first_person_lst = df[first_person].tolist()
    second_person_tucCartha_lst = df[second_person_tucCartha].tolist()
    second_person_lst = df[second_person].tolist()
    second_person_honorific_lst = df[second_person_honorific].tolist()
    third_person_lst = df[third_person].tolist()
    third_person_honorific_lst = df[third_person_honorific].tolist()
    no_person_lst = df[no_person].tolist()
    zipped_lists = zip(category_lst, tam_lst, first_person_lst, second_person_tucCartha_lst, second_person_lst, second_person_honorific_lst, third_person_lst, third_person_honorific_lst, no_person_lst)

    output = ''
    for category_val, tam_val, first_person_val, second_person_tucCartha_val, second_person_val, second_person_honorific_val, \
            third_person_val, third_person_honorific_val, no_person_val in zipped_lists:

        if (isinstance(tam_val, str) and tam_val.lower() != 'nan'):
            tam_data = fetch_tam_data(tam_val)
            line = ""
            for data in tam_data:
                line = line + f"<s n=\"{data}\"/>"
            line = line + "</r></p></e>"

        # first person
        dix_entry_lst = fetch_first_person_dix_entry(first_person_val, category_val, line)
        for dix_entry in dix_entry_lst:
            output = output + dix_entry + '\n'

        # second person tucCartha
        dix_entry_lst = fetch_second_person_tucCartha_dix_entry(second_person_tucCartha_val, category_val, line)
        for dix_entry in dix_entry_lst:
            output = output + dix_entry + '\n'

        # second person
        dix_entry_lst = fetch_second_person_dix_entry(second_person_val, category_val, line)
        for dix_entry in dix_entry_lst:
            output = output + dix_entry + '\n'

        # second person honorific
        dix_entry_lst = fetch_second_person_honorific_dix_entry(second_person_honorific_val, category_val, line)
        for dix_entry in dix_entry_lst:
            output = output + dix_entry + '\n'

        # third person
        dix_entry_lst = fetch_third_person_dix_entry(third_person_val, category_val, line)
        for dix_entry in dix_entry_lst:
            output = output + dix_entry + '\n'

        # third person honorific
        dix_entry_lst = fetch_third_person_honorific_dix_entry(third_person_honorific_val, category_val, line)
        for dix_entry in dix_entry_lst:
            output = output + dix_entry + '\n'

        # no_person
        dix_entry_lst = fetch_no_person_dix_entry(no_person_val, category_val, line)
        for dix_entry in dix_entry_lst:
            output = output + dix_entry + '\n'

        output = output + '\n'
        # Define the text you want to append in DIX
        text_to_append = HEADER + "\n" + output + "\n" + FOOTER

    write_output(output)
    update_dix(text_to_append)




