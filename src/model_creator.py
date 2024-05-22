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

# Hörverstehen-Modelle: Audio -> Text + Romaji
def create_audio_to_text_model(name, model_id, text_field, prompt):
    fields = ["Audio", text_field, "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': f'Zeichne {prompt} von: ' + '{{Romaji}}' + f'<br>{{{{Audio}}}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{' + text_field + '}}',
        }
    ]
    return create_basic_model(model_id, name, fields, templates)

def create_hiragana_audio_to_text_model():
    return create_audio_to_text_model("Hörverstehen Hiragana", 1607392339, "Hiragana", "Hiragana")

def create_katakana_audio_to_text_model():
    return create_audio_to_text_model("Hörverstehen Katakana", 1607392340, "Katakana", "Katakana")

# Vokabel-Modelle: Audio + Text -> Deutsch + Romaji
def create_audio_text_to_deutsch_model(name, model_id, text_field, prompt):
    fields = ["Audio", text_field, "Deutsch", "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': f'Übersetze: {{{{' + text_field + '}} <br>{{{{Audio}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Deutsch}} ({{Romaji}})',
        }
    ]
    return create_basic_model(model_id, name, fields, templates)

def create_hiragana_audio_to_deutsch_model():
    return create_audio_text_to_deutsch_model("Vokabel Hiragana", 1607392341, "Hiragana", "Hiragana")

def create_katakana_audio_to_deutsch_model():
    return create_audio_text_to_deutsch_model("Vokabel Katakana", 1607392342, "Katakana", "Katakana")

# Aussprache-Modelle: Text -> Audio + Romaji
def create_text_to_audio_model(name, model_id, text_field, prompt):
    fields = [text_field, "Audio", "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': f'Spreche: {{{{' + text_field + '}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}<br>({{Romaji}})',
        }
    ]
    return create_basic_model(model_id, name, fields, templates)

def create_hiragana_text_to_audio_model():
    return create_text_to_audio_model("Aussprache Hiragana", 1607392343, "Hiragana", "Hiragana")

def create_katakana_text_to_audio_model():
    return create_text_to_audio_model("Aussprache Katakana", 1607392344, "Katakana", "Katakana")

# Bild-Modelle: Bild -> Audio + Text + Romaji
def create_image_to_audio_text_model(name, model_id, text_field, prompt):
    fields = ["Image", "Audio", text_field, "Romaji"]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': f'Was ist auf diesem Bild zu sehen? (Denken Sie an das entsprechende {prompt}).<br>{{{{Image}}}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}<br>{{' + text_field + '}}<br>({{Romaji}})',
        }
    ]
    return create_basic_model(model_id, name, fields, templates)

def create_image_to_hiragana_model():
    return create_image_to_audio_text_model("Bild zu Hiragana", 1607392345, "Hiragana", "Hiragana")

def create_image_to_katakana_model():
    return create_image_to_audio_text_model("Bild zu Katakana", 1607392346, "Katakana", "Katakana")
