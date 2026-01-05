import requests
import json
import os
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")

CHANNEL_HANDLE = 'MrBeast'


def playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)
        data = response.json()

        response.raise_for_status()

        #print(json.dumps(data, indent=4))

        Channel_playlistID = data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        print(Channel_playlistID)

        return Channel_playlistID
    
    except requests.exceptions.RequestException as e:
       raise e
    
if __name__ == "__main__":
    playlist_id()