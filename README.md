# JapanischLernen

Ein Python-basiertes Tool zur Erstellung von Anki-Karten für das Erlernen der japanischen Sprache. Das Tool generiert Audiodateien für japanische Zeichen und lädt automatisch Bilder von Wikimedia Commons herunter, um das Vokabellernen zu unterstützen.

## Funktionen
- Generiert Audiodateien für japanische Hiragana und Katakana Zeichen.
- Lädt automatisch Bilder von Wikimedia Commons herunter, um Vokabeln zu illustrieren.
- Erstellt strukturierte Anki-Kartendecks basierend auf definierten CSV-Dateien.

## Installation
1. Klonen Sie das Repository:
    ```sh
    git clone https://github.com/<username>/JapanischLernen.git
    cd JapanischLernen
    ```

2. Erstellen und aktivieren Sie eine virtuelle Umgebung:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Auf Windows: venv\Scripts\activate
    ```

3. Installieren Sie die Abhängigkeiten:
    ```sh
    pip install -r requirements.txt
    ```

## Verwendung
1. Stellen Sie sicher, dass die CSV-Dateien im `data/csv`-Verzeichnis vorhanden sind und die Pfade korrekt sind.
2. Führen Sie das Hauptskript aus, um die Anki-Decks zu generieren:
    ```sh
    python src/main.py
    ```

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Siehe die [LICENSE](LICENSE)-Datei für weitere Details.
