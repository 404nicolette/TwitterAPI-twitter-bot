from bs4 import BeautifulSoup
import requests
import time
import os
url = 'https://www.azlyrics.com/lyrics/hozier/{}.html'
songs = ["takemetochurch","someonenew", "tobealone", "fromeden", "worksong",
         "likerealpeopledo", "cherrywine", "arsonistslullabye", "shrike",
         "ninacriedpower", "almostsweetmusic", "be", "talk", "wouldthati",
         "sunlight", "firsttime", "francesca", "icarrionicarian", "eatyouryoung",
         "damagegetsdone", "whoweare", "allthingsend", "unknownnth", "firstlight",
         "abstractpsychopomp"]

# create a folder to store the data
folder_name = 'songs'

try:
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
        print('Directory already exist')
except Exception as e:
    print(f'Something went wrong with creating the directory: {str(e)}')

# get the html of each song and store inside the folder
with open("song_lyrics.txt", "a") as output_file:
    # get the html of each song and store inside the folder
    for song in songs:
        url_song = url.format(song)
        data = requests.get(url_song)  # request to get the content of the html
        time.sleep(5)  # buffer to avoid time out error

        # store the raw html inside the created folder.
        with open(os.path.join(folder_name, f"{song}.html"), "w+") as f:
            f.write(data.text)

        # clean up the html
        with open(os.path.join(folder_name, f"{song}.html"), "r") as f:
            page = f.read()

            upper_bound = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
            lower_bound = '<!-- MxM banner -->'

            starting_pos = page.find(upper_bound)
            end_pos = page.find(lower_bound)

            if starting_pos != -1 and end_pos != -1:
                extract_content = page[starting_pos + len(upper_bound):end_pos]

                # parse the extracted content
                soup = BeautifulSoup(extract_content, 'html.parser')

                # erase html tags
                for tag in soup.find_all():
                    tag.decompose()

                lyrics_only = soup.get_text().strip()

                # Append lyrics to the output file
                output_file.write(lyrics_only + "\n")
