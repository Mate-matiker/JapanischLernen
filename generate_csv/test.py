import requests

def search_unsplash_images(search_term, access_key):
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {access_key}",
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

def download_image(image_url, filename):
    img_data = requests.get(image_url).content
    with open(filename, 'wb') as handler:
        handler.write(img_data)
    print(f"Downloaded image to {filename}")

# Beispiel-Aufruf der Funktionen
access_key = 'CzoP4hmkj3t9odZcL3NapS_kFqxOoVqXENAvRHJToAM'  # Ersetzen Sie dies durch Ihren tatsächlichen Unsplash API-Schlüssel
search_term = "Handtuch"
image_url = search_unsplash_images(search_term, access_key)
if image_url:
    download_image(image_url, f"{search_term}.jpg")
