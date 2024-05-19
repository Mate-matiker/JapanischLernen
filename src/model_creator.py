import genanki

def create_basic_model(model_id, name, fields, templates):
    return genanki.Model(
        model_id=model_id,
        name=name,
        fields=[{'name': field} for field in fields],
        templates=templates,
        css="""
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
        """
    )

def create_hiragana_to_romaji_model():
    fields = ["Hiragana", "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Hiragana}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Romaji}}',
        },
    ]
    return create_basic_model(1607392319, "Hiragana to Romaji", fields, templates)

def create_romaji_to_hiragana_model():
    fields = ["Romaji", "Hiragana"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Romaji}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Hiragana}}',
        },
    ]
    return create_basic_model(1607392320, "Romaji to Hiragana", fields, templates)

def create_audio_to_hiragana_model():
    fields = ["Audio", "Hiragana"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Audio}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Hiragana}}',
        },
    ]
    return create_basic_model(1607392321, "Audio to Hiragana", fields, templates)

def create_hiragana_to_audio_model():
    fields = ["Hiragana", "Audio"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Hiragana}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}',
        },
    ]
    return create_basic_model(1607392322, "Hiragana to Audio", fields, templates)

def create_hiragana_to_deutsch_model():
    fields = ["Hiragana", "Deutsch"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Hiragana}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Deutsch}}',
        },
    ]
    return create_basic_model(1607392323, "Hiragana to Deutsch", fields, templates)

def create_image_to_hiragana_model():
    fields = ["Image", "Hiragana"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Image}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Hiragana}}',
        },
    ]
    return create_basic_model(1607392324, "Image to Hiragana", fields, templates)

def create_deutsch_to_hiragana_model():
    fields = ["Deutsch", "Hiragana"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Deutsch}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Hiragana}}',
        },
    ]
    return create_basic_model(1607392325, "Deutsch to Hiragana", fields, templates)

def create_deutsch_to_katakana_model():
    fields = ["Deutsch", "Katakana"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Deutsch}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Katakana}}',
        },
    ]
    return create_basic_model(1607392326, "Deutsch to Katakana", fields, templates)

def create_hiragana_to_katakana_model():
    fields = ["Hiragana", "Katakana"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Hiragana}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Katakana}}',
        },
    ]
    return create_basic_model(1607392327, "Hiragana to Katakana", fields, templates)

def create_image_to_deutsch_model():
    fields = ["Image", "Deutsch"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Image}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Deutsch}}',
        },
    ]
    return create_basic_model(1607392328, "Image to Deutsch", fields, templates)

def create_audio_to_deutsch_hiragana_model():
    fields = ["Audio", "Deutsch"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Audio}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Deutsch}}',
        },
    ]
    return create_basic_model(1607392329, "Audio to Deutsch Hiragana", fields, templates)

def create_audio_to_deutsch_katakana_model():
    fields = ["Audio", "Deutsch"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Audio}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Deutsch}}',
        },
    ]
    return create_basic_model(1607392330, "Audio to Deutsch Katakana", fields, templates)

def create_dakuten_to_romaji_model():
    fields = ["Dakuten", "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Dakuten}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Romaji}}',
        },
    ]
    return create_basic_model(1607392331, "Dakuten to Romaji", fields, templates)

def create_romaji_to_dakuten_model():
    fields = ["Romaji", "Dakuten"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Romaji}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Dakuten}}',
        },
    ]
    return create_basic_model(1607392332, "Romaji to Dakuten", fields, templates)

def create_audio_to_dakuten_model():
    fields = ["Audio", "Dakuten"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Audio}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Dakuten}}',
        },
    ]
    return create_basic_model(1607392333, "Audio to Dakuten", fields, templates)

def create_dakuten_to_audio_model():
    fields = ["Dakuten", "Audio"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Dakuten}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}',
        },
    ]
    return create_basic_model(1607392334, "Dakuten to Audio", fields, templates)

def create_yo_on_to_romaji_model():
    fields = ["Yōon", "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Yōon}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Romaji}}',
        },
    ]
    return create_basic_model(1607392335, "Yōon to Romaji", fields, templates)

def create_romaji_to_yo_on_model():
    fields = ["Romaji", "Yōon"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Romaji}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Yōon}}',
        },
    ]
    return create_basic_model(1607392336, "Romaji to Yōon", fields, templates)

def create_audio_to_yo_on_model():
    fields = ["Audio", "Yōon"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Audio}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Yōon}}',
        },
    ]
    return create_basic_model(1607392337, "Audio to Yōon", fields, templates)

def create_yo_on_to_audio_model():
    fields = ["Yōon", "Audio"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Yōon}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}',
        },
    ]
    return create_basic_model(1607392338, "Yōon to Audio", fields, templates)
