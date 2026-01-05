import requests
import json
import os
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")

CHANNEL_HANDLE = 'MrBeast'

max_results = 50

video_ids = []


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
    
def get_video_id(playlist_id):
    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={max_results}&playlistId={playlist_id}&key={API_KEY}"
    page_token = None
    try:
        while True:
            url = base_url
            if page_token:
                url += f"&pageToken={page_token}"

            response = requests.get(url)
            data = response.json()

            response.raise_for_status()

            for item in data["items"]:
                video_id = item["contentDetails"]["videoId"]
                video_ids.append(video_id)

            page_token = data.get("nextPageToken")
            if not page_token:
                break

    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    playlist_id = playlist_id()
    get_video_id(playlist_id)
    print(video_ids)