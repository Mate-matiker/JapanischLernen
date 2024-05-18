import genanki

def create_hiragana_to_romaji_model():
    return genanki.Model(
        model_id=abs(hash("Hiragana to Romaji Model")),
        name='Hiragana to Romaji Model',
        fields=[
            {'name': 'Frage'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Frage}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_romaji_to_hiragana_model():
    return genanki.Model(
        model_id=abs(hash("Romaji to Hiragana Model")),
        name='Romaji to Hiragana Model',
        fields=[
            {'name': 'Frage'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Frage}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_audio_to_hiragana_model():
    return genanki.Model(
        model_id=abs(hash("Audio to Hiragana Model")),
        name='Audio to Hiragana Model',
        fields=[
            {'name': 'Audio'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Audio}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_hiragana_to_audio_model():
    return genanki.Model(
        model_id=abs(hash("Hiragana to Audio Model")),
        name='Hiragana to Audio Model',
        fields=[
            {'name': 'Frage'},
            {'name': 'Audio'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Frage}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}',
            },
        ])

def create_hiragana_to_deutsch_model():
    return genanki.Model(
        model_id=abs(hash("Hiragana to Deutsch Model")),
        name='Hiragana to Deutsch Model',
        fields=[
            {'name': 'Frage'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Frage}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_image_to_hiragana_model():
    return genanki.Model(
        model_id=abs(hash("Image to Hiragana Model")),
        name='Image to Hiragana Model',
        fields=[
            {'name': 'Bild'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Bild}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_deutsch_to_hiragana_model():
    return genanki.Model(
        model_id=abs(hash("Deutsch to Hiragana Model")),
        name='Deutsch to Hiragana Model',
        fields=[
            {'name': 'Frage'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Frage}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_deutsch_to_katakana_model():
    return genanki.Model(
        model_id=abs(hash("Deutsch to Katakana Model")),
        name='Deutsch to Katakana Model',
        fields=[
            {'name': 'Frage'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Frage}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_hiragana_to_katakana_model():
    return genanki.Model(
        model_id=abs(hash("Hiragana to Katakana Model")),
        name='Hiragana to Katakana Model',
        fields=[
            {'name': 'Frage'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Frage}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_image_to_deutsch_model():
    return genanki.Model(
        model_id=abs(hash("Image to Deutsch Model")),
        name='Image to Deutsch Model',
        fields=[
            {'name': 'Bild'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Bild}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_audio_to_deutsch_hiragana_model():
    return genanki.Model(
        model_id=abs(hash("Audio to Deutsch Hiragana Model")),
        name='Audio to Deutsch Hiragana Model',
        fields=[
            {'name': 'Audio'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Audio}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

def create_audio_to_deutsch_katakana_model():
    return genanki.Model(
        model_id=abs(hash("Audio to Deutsch Katakana Model")),
        name='Audio to Deutsch Katakana Model',
        fields=[
            {'name': 'Audio'},
            {'name': 'Antwort'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Audio}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])
