import os


if __name__ == '__main__':
    dir_path = '/Users/razvanbunga/Desktop/documents/payslips'
    files_to_rename = [x for x in os.listdir(dir_path) if x.startswith('Payslip')]
    
    for file in files_to_rename:
        new_name = '-'.join(file.split(' ')[-1].split('-')[::-1]).replace('.pdf', '')
        os.rename(f'{dir_path}/{file}', f'{dir_path}/{new_name}.pdf')
    
    print(f'{len(files_to_rename)} files renamed')