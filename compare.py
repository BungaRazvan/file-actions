import os
import json


if __name__ == '__main__':
    main_dir_path = '/Users/razvanbunga/Desktop/documents/playlists'
    download_dir_path = '/Users/razvanbunga/Downloads/'
    file_to_read = [x for x in os.listdir(download_dir_path) if x.startswith('foo')][0]
    main_file_path = f'{main_dir_path}/playlists.json'


    with open(main_file_path, 'r') as file:
        f2_songs = []
        f1_songs = []
        file_data = json.load(file)

        with open(f'{download_dir_path}/{file_to_read}', 'r') as f2:
            file_read_data = json.load(f2)

            for key, value in file_read_data.items():
                f2_songs = value
            
            f1_songs = file_data[list(file_read_data.keys())[0]]
            os.remove(f'{download_dir_path}/{file_to_read}')
        
        for song in f1_songs:
            if song not in f2_songs:
                print(song)
