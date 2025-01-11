import os
import json


if __name__ == '__main__':
    main_dir_path = '/Users/razvanbunga/Desktop/documents/playlists'
    download_dir_path = '/Users/razvanbunga/Downloads/'
    main_file_path = f'{main_dir_path}/playlists.json'
    files_to_read = [x for x in os.listdir(download_dir_path) if x.endswith('_songs.json')]
    exist_main_file = os.path.isfile(main_file_path)
    file_operation = 'w'

    if exist_main_file:
        file_operation = 'r+'

    with open(main_file_path, file_operation, encoding='utf-8') as file:
        file_data = {}

        if exist_main_file:
            file.seek(0)
            file_data = json.load(file)

        for file_to_read in reversed(files_to_read):
            print(file_to_read)
            with open(f'{download_dir_path}/{file_to_read}', 'r', encoding='utf-8') as f2:
                file_read_data = json.load(f2)

                for key, value in file_read_data.items():
                    file_data[key] = value
                
                os.remove(f'{download_dir_path}/{file_to_read}')

        file.seek(0)
        json.dump(file_data, file, ensure_ascii=False, indent=2)

    print(f'{len(files_to_read)} files combined')