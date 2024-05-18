import genanki

def create_subdeck_structure(deck_name, subdeck_info, models, data_loader):
    decks = {}
    main_deck = genanki.Deck(deck_id=abs(hash(deck_name)), name=deck_name)
    decks[deck_name] = main_deck

    for subdeck_name, subdeck_content in subdeck_info.items():
        full_subdeck_name = f"{deck_name}::{subdeck_name}"
        sub_deck_id = abs(hash(full_subdeck_name))
        sub_deck = genanki.Deck(deck_id=sub_deck_id, name=full_subdeck_name)
        decks[full_subdeck_name] = sub_deck

        if isinstance(subdeck_content, dict):
            if subdeck_content:  # Nur weiter nach Unterstapeln suchen, wenn vorhanden
                nested_deck = create_subdeck_structure(full_subdeck_name, subdeck_content, models, data_loader)
                decks.update(nested_deck)
            else:
                continue  # Überspringe leere Unterstapel
        else:
            model_name = subdeck_content
            model = models.get(model_name)
            # Verwende den direkten übergeordneten Stapelname für die CSV-Datei
            parent_deck = subdeck_name if "::" not in deck_name else deck_name.split("::")[-1]
            card_data = data_loader.load_data(model_name, parent_deck)
            for fields in card_data:
                if len(fields) == len(model.fields):  # Sicherstellen, dass die Note die richtige Anzahl Felder hat
                    note = genanki.Note(model=model, fields=fields)
                    sub_deck.add_note(note)
                    # Debug-Ausgabe für die Note
                    print(f"Note created with fields: {fields}")
    return decks
