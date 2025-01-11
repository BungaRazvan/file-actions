import os
import json


if __name__ == '__main__':
    main_dir_path = '/Users/razvanbunga/Desktop/documents/playlists'
    download_dir_path = '/Users/razvanbunga/Downloads/'
    files_to_read = [x for x in os.listdir(download_dir_path) if x.endswith('_songs.json')]
    main_file_path = f'{main_dir_path}/playlists.json'

    new_songs = []
    previous_songs = []


    with open(main_file_path, 'r') as file:
        previous_data = json.load(file)

        for file in files_to_read:
            with open(f'{download_dir_path}/{file}', 'r') as f2:
                new_read_data = json.load(f2)

                for key, value in new_read_data.items():
                    new_songs = value
                
                previous_songs = previous_data[list(new_read_data.keys())[0]]
                os.remove(f'{download_dir_path}/{file}')

            print(file)
            print(json.dumps([s for s in previous_songs if not any(x in s for x in new_songs)], indent=2))
