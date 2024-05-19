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
        input {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
        """
    )

# Hörverstehen: Audio -> Text (Hiragana/Katakana)
def create_audio_to_text_model():
    fields = ["Audio", "Text"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Audio}}<br><input type="text" id="typeans" />',
            'afmt': '{{FrontSide}}<hr id="answer">{{type:Text}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Audio}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Text}}',
        },
    ]
    return create_basic_model(1607392319, "Audio to Text", fields, templates)

# Vokabel: Audio+Text (Hiragana/Katakana) -> Text (Romaji)
def create_audio_text_to_romaji_model():
    fields = ["Audio", "Text", "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Audio}}<br>{{Text}}<br><input type="text" id="typeans" />',
            'afmt': '{{FrontSide}}<hr id="answer">{{type:Romaji}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Audio}}<br>{{Text}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Romaji}}',
        },
    ]
    return create_basic_model(1607392320, "Audio+Text to Romaji", fields, templates)

# Aussprache: Text (Hiragana/Katakana) -> Audio + Text (Romaji)
def create_text_to_audio_model():
    fields = ["Text", "Audio", "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Text}}<br><input type="text" id="typeans" />',
            'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}<br>{{type:Romaji}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Text}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}<br>{{Romaji}}',
        },
    ]
    return create_basic_model(1607392321, "Text to Audio", fields, templates)

# Optionale Modelle für Eingaben in Hiragana und Katakana
def create_hiragana_input_model():
    fields = ["Prompt", "Hiragana"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Prompt}}<br><input type="text" id="typeans" />',
            'afmt': '{{FrontSide}}<hr id="answer">{{type:Hiragana}}',
        },
    ]
    return create_basic_model(1607392339, "Hiragana Input", fields, templates)

def create_katakana_input_model():
    fields = ["Prompt", "Katakana"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Prompt}}<br><input type="text" id="typeans" />',
            'afmt': '{{FrontSide}}<hr id="answer">{{type:Katakana}}',
        },
    ]
    return create_basic_model(1607392340, "Katakana Input", fields, templates)
