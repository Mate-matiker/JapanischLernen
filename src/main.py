from model_creator import (
    create_hiragana_audio_to_text_model,
    create_katakana_audio_to_text_model,
    create_hiragana_audio_to_deutsch_model,
    create_katakana_audio_to_deutsch_model,
    create_hiragana_text_to_audio_model,
    create_katakana_text_to_audio_model,
    create_image_to_hiragana_model,
    create_image_to_katakana_model
)
from data_loader import DataLoader
from deck_builder import create_subdeck_structure
from deck_structure import deck_info
import genanki

def main():
    unsplash_access_key = 'YOUR_UNSPLASH_ACCESS_KEY'  # Ersetzen Sie dies durch Ihren tatsächlichen Unsplash API-Schlüssel
    data_loader = DataLoader('data/csv/', 'data/images/', 'data/audio/', unsplash_access_key)
    
    models = {
        "hiragana_audio_to_text": create_hiragana_audio_to_text_model(),
        "katakana_audio_to_text": create_katakana_audio_to_text_model(),
        "hiragana_audio_to_deutsch": create_hiragana_audio_to_deutsch_model(),
        "katakana_audio_to_deutsch": create_katakana_audio_to_deutsch_model(),
        "hiragana_text_to_audio": create_hiragana_text_to_audio_model(),
        "katakana_text_to_audio": create_katakana_text_to_audio_model(),
        "image_to_hiragana": create_image_to_hiragana_model(),
        "image_to_katakana": create_image_to_katakana_model()
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
