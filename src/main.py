from model_creator import (
    create_hiragana_to_romaji_model,
    create_romaji_to_hiragana_model,
    create_audio_to_hiragana_model,
    create_hiragana_to_audio_model,
    create_hiragana_to_deutsch_model,
    create_image_to_hiragana_model,
    create_deutsch_to_hiragana_model,
    create_deutsch_to_katakana_model,
    create_hiragana_to_katakana_model,
    create_image_to_deutsch_model,
    create_audio_to_deutsch_hiragana_model,
    create_audio_to_deutsch_katakana_model,
    create_dakuten_to_romaji_model,
    create_romaji_to_dakuten_model,
    create_audio_to_dakuten_model,
    create_dakuten_to_audio_model,
    create_yo_on_to_romaji_model,
    create_romaji_to_yo_on_model,
    create_audio_to_yo_on_model,
    create_yo_on_to_audio_model
)
from data_loader import DataLoader
from deck_builder import create_subdeck_structure
from deck_structure import deck_info
import genanki

def main():
    unsplash_access_key = 'key'  # Ersetzen Sie dies durch Ihren tatsächlichen Unsplash API-Schlüssel
    data_loader = DataLoader('data/csv/', 'data/images/', 'data/audio/', unsplash_access_key)
    
    models = {
        "hiragana_to_romaji": create_hiragana_to_romaji_model(),
        "romaji_to_hiragana": create_romaji_to_hiragana_model(),
        "audio_to_hiragana": create_audio_to_hiragana_model(),
        "hiragana_to_audio": create_hiragana_to_audio_model(),
        "hiragana_to_deutsch": create_hiragana_to_deutsch_model(),
        "image_to_hiragana": create_image_to_hiragana_model(),
        "deutsch_to_hiragana": create_deutsch_to_hiragana_model(),
        "deutsch_to_katakana": create_deutsch_to_katakana_model(),
        "hiragana_to_katakana": create_hiragana_to_katakana_model(),
        "image_to_deutsch": create_image_to_deutsch_model(),
        "audio_to_deutsch_hiragana": create_audio_to_deutsch_hiragana_model(),
        "audio_to_deutsch_katakana": create_audio_to_deutsch_katakana_model(),
        "dakuten_to_romaji": create_dakuten_to_romaji_model(),
        "romaji_to_dakuten": create_romaji_to_dakuten_model(),
        "audio_to_dakuten": create_audio_to_dakuten_model(),
        "dakuten_to_audio": create_dakuten_to_audio_model(),
        "yo_on_to_romaji": create_yo_on_to_romaji_model(),
        "romaji_to_yo_on": create_romaji_to_yo_on_model(),
        "audio_to_yo_on": create_audio_to_yo_on_model(),
        "yo_on_to_audio": create_yo_on_to_audio_model()
    }
    
    decks = create_subdeck_structure("Japanisch", deck_info, models, data_loader)
    japanisch_deck = decks["Japanisch"]
    del decks["Japanisch"]
    
    package = genanki.Package(japanisch_deck)
    package.media_files = data_loader.get_media_files()
    
    for deck_name, deck in decks.items():
        package.decks.append(deck)
    
    # Debug-Ausgabe für Medien-Dateien
    print("Media files to be added to the package:")
    for media_file in package.media_files:
        print(media_file)
    
    package.write_to_file('output/Japanisch.apkg')

if __name__ == "__main__":
    main()
