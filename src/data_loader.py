import csv
import os
from gtts import gTTS
import requests

class DataLoader:
    def __init__(self, csv_dir, image_dir, audio_dir, unsplash_access_key):
        self.csv_dir = csv_dir
        self.image_dir = image_dir
        self.audio_dir = audio_dir
        self.unsplash_access_key = unsplash_access_key
        self.media_files = []

    def generate_audio(self, text, filename):
        tts = gTTS(text, lang='ja')
        tts.save(filename)

    def search_unsplash_images(self, search_term):
        url = "https://api.unsplash.com/search/photos"
        headers = {
            "Authorization": f"Client-ID {self.unsplash_access_key}",
            "User-Agent": "JapanischLernenApp/1.0 (https://example.com/contact; email@example.com)"
        }
        params = {
            "query": search_term,
            "per_page": 1  # Anzahl der gewünschten Ergebnisse pro Seite
        }
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data['results']:
                    return data['results'][0]['urls']['small']  # URL des ersten Bildes
                else:
                    print(f"No results found for {search_term}")
            except requests.exceptions.JSONDecodeError:
                print("Error decoding JSON response")
        else:
            print(f"Failed to fetch image for {search_term}, status code: {response.status_code}")
        return None

    def download_image(self, search_term, filename):
        image_url = self.search_unsplash_images(search_term)
        if image_url:
            img_data = requests.get(image_url).content
            with open(filename, 'wb') as handler:
                handler.write(img_data)
            print(f"Downloaded image to {filename}")

    def load_data(self, card_type, parent_deck):
        # Konvention: Verwende die CSV-Datei, die den Namen des übergeordneten Stapels hat
        csv_filename = f"{parent_deck}.csv"
        csv_path = os.path.join(self.csv_dir, csv_filename)
        
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        
        with open(csv_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            result = []
            for row in reader:
                romaji = row['Romaji']
                hiragana = row['Hiragana']
                katakana = row['Katakana']
                deutsch = row['Deutsch']

                # Generate file names for media
                img_filename = f"{romaji}.png".replace(' ', '_')
                audio_filename_hiragana = f"hiragana_{romaji}.mp3".replace(' ', '_')
                audio_filename_katakana = f"katakana_{romaji}.mp3".replace(' ', '_')
                img_path = os.path.join(self.image_dir, img_filename)
                audio_path_hiragana = os.path.join(self.audio_dir, audio_filename_hiragana)
                audio_path_katakana = os.path.join(self.audio_dir, audio_filename_katakana)

                # Generate audio files if they don't exist
                if not os.path.exists(audio_path_hiragana):
                    self.generate_audio(hiragana, audio_path_hiragana)
                if not os.path.exists(audio_path_katakana):
                    self.generate_audio(katakana, audio_path_katakana)

                # Download images if they don't exist
                if not os.path.exists(img_path):
                    pass #self.download_image(deutsch, img_path)

                # Add media files to the list
                if os.path.exists(img_path):
                    self.media_files.append(img_path)
                if os.path.exists(audio_path_hiragana):
                    self.media_files.append(audio_path_hiragana)
                if os.path.exists(audio_path_katakana):
                    self.media_files.append(audio_path_katakana)

                # Append data according to card type
                if card_type == "hiragana_audio_to_text":
                    result.append([f'[sound:{audio_filename_hiragana}]', hiragana, romaji])
                elif card_type == "katakana_audio_to_text":
                    result.append([f'[sound:{audio_filename_katakana}]', katakana, romaji])
                elif card_type == "hiragana_audio_to_deutsch":
                    result.append([f'[sound:{audio_filename_hiragana}]', hiragana, deutsch, romaji])
                elif card_type == "katakana_audio_to_deutsch":
                    result.append([f'[sound:{audio_filename_katakana}]', katakana, deutsch, romaji])
                elif card_type == "hiragana_text_to_audio":
                    result.append([hiragana, f'[sound:{audio_filename_hiragana}]', romaji])
                elif card_type == "katakana_text_to_audio":
                    result.append([katakana, f'[sound:{audio_filename_katakana}]', romaji])
                elif card_type == "image_to_hiragana":
                    result.append([f'<img src="{img_filename}">', f'[sound:{audio_filename_hiragana}]', hiragana, romaji])
                elif card_type == "image_to_katakana":
                    result.append([f'<img src="{img_filename}">', f'[sound:{audio_filename_katakana}]', katakana, romaji])

            return result

    def get_media_files(self):
        return list(set(self.media_files))
