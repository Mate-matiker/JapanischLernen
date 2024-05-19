import pandas as pd

# Erstellen von spezifischen Vokabeln für verschiedene Übungen

# Zusätzliche Vokabeln für Hiragana Vokabeln
hiragana_vokabeln_data = {
    "Deutsch": ["Katze", "Hund", "Vogel", "Pferd", "Fisch", "Haus", "Baum", "Auto", "Buch", "Stuhl", "Tasse", "Kuchen", "Schere", "Zug", "Apfel", "Banane", "Brot", "Wasser", "Milch", "Ei"],
    "Romaji": ["neko", "inu", "tori", "uma", "sakana", "ie", "ki", "kuruma", "hon", "isu", "kappu", "keeki", "hasami", "densha", "ringo", "banana", "pan", "mizu", "miruku", "tamago"],
    "Hiragana": ["ねこ", "いぬ", "とり", "うま", "さかな", "いえ", "き", "くるま", "ほん", "いす", "かっぷ", "けえき", "はさみ", "でんしゃ", "りんご", "ばなな", "ぱん", "みず", "みるく", "たまご"],
    "Katakana": ["ネコ", "イヌ", "トリ", "ウマ", "サカナ", "イエ", "キ", "クルマ", "ホン", "イス", "カップ", "ケーキ", "ハサミ", "デンシャ", "リンゴ", "バナナ", "パン", "ミズ", "ミルク", "タマゴ"]
}

hiragana_vokabeln_df = pd.DataFrame(hiragana_vokabeln_data)

# Zusätzliche Vokabeln für Katakana Vokabeln
katakana_vokabeln_data = {
    "Deutsch": ["Fernseher", "Radio", "Kamera", "Computer", "Telefon", "Lehrer", "Schüler", "Tisch", "Stuhl", "Fenster", "Tür", "Boden", "Decke", "Wand", "Lampe", "Bett", "Schrank", "Buch", "Heft", "Stift"],
    "Romaji": ["terebi", "rajio", "kamera", "konpyuuta", "denwa", "sensei", "gakusei", "tsukue", "isu", "mado", "doa", "yuka", "tenjou", "kabe", "ranpu", "beddo", "tana", "hon", "nooto", "pen"],
    "Hiragana": ["てれび", "らじお", "かめら", "こんぴゅうたあ", "でんわ", "せんせい", "がくせい", "つくえ", "いす", "まど", "どあ", "ゆか", "てんじょう", "かべ", "らんぷ", "べっど", "たな", "ほん", "のーと", "ぺん"],
    "Katakana": ["テレビ", "ラジオ", "カメラ", "コンピュータ", "デンワ", "センセイ", "ガクセイ", "ツクエ", "イス", "マド", "ドア", "ユカ", "テンジョウ", "カベ", "ランプ", "ベッド", "タナ", "ホン", "ノート", "ペン"]
}
katakana_vokabeln_df = pd.DataFrame(katakana_vokabeln_data)

# Zusätzliche Vokabeln für Dakuten und Handakuten
dakuten_handakuten_vokabeln_data = {
    "Deutsch": ["Flasche", "Löffel", "Gabel", "Messer", "Pfanne", "Topf", "Küche", "Bad", "Zimmer", "Schrank", "Handtuch", "Seife", "Shampoo", "Dusche", "Wasserhahn", "Spiegel", "Bürste", "Kamm", "Zahnbürste", "Zahnpasta"],
    "Romaji": ["bin", "supuun", "fooku", "naifu", "furaipan", "nabe", "kicchin", "ofuro", "heya", "tana", "taoru", "sekken", "shampoo", "shawaa", "suihou", "kagami", "burasu", "kushi", "haburashi", "hamigaki"],
    "Hiragana": ["びん", "すぷーん", "ふぉーく", "ないふ", "ふらいぱん", "なべ", "きっちん", "おふろ", "へや", "たな", "たおる", "せっけん", "しゃんぷう", "しゃわあ", "すいほう", "かがみ", "ぶらす", "くし", "はぶらし", "はみがき"],
    "Katakana": ["ビン", "スプーン", "フォーク", "ナイフ", "フライパン", "ナベ", "キッチン", "オフロ", "ヘヤ", "タナ", "タオル", "セッケン", "シャンプー", "シャワー", "スイホウ", "カガミ", "ブラシ", "クシ", "ハブラシ", "ハミガキ"]
}
dakuten_handakuten_vokabeln_df = pd.DataFrame(dakuten_handakuten_vokabeln_data)

# Zusätzliche Vokabeln für Yoon Kombinationen
yo_on_vokabeln_data = {
    "Deutsch": ["Familie", "Freund", "Freundin", "Mutter", "Vater", "Schwester", "Bruder", "Oma", "Opa", "Kind", "Baby", "Onkel", "Tante", "Cousin", "Cousine", "Nachbar", "Kollege", "Arzt", "Lehrer", "Schüler"],
    "Romaji": ["kazoku", "tomodachi", "kanojo", "haha", "chichi", "ane", "ani", "obaasan", "ojiisan", "kodomo", "akachan", "oji", "oba", "itoko", "itoko", "rinjin", "douryou", "isha", "sensei", "gakusei"],
    "Hiragana": ["かぞく", "ともだち", "かのじょ", "はは", "ちち", "あね", "あに", "おばあさん", "おじいさん", "こども", "あかちゃん", "おじ", "おば", "いとこ", "いとこ", "りんじん", "どうりょう", "いしゃ", "せんせい", "がくせい"],
    "Katakana": ["カゾク", "トモダチ", "カノジョ", "ハハ", "チチ", "アネ", "アニ", "オバアサン", "オジイサン", "コドモ", "アカチャン", "オジ", "オバ", "イトコ", "イトコ", "リンジン", "ドウリョウ", "イシャ", "センセイ", "ガクセイ"]
}
yo_on_vokabeln_df = pd.DataFrame(yo_on_vokabeln_data)

# CSV-Dateien speichern
hiragana_vokabeln_df.to_csv('../data/csv/Hiragana_Vokabeln.csv', index=False)
katakana_vokabeln_df.to_csv('../data/csv/Katakana_Vokabeln.csv', index=False)
dakuten_handakuten_vokabeln_df.to_csv('../data/csv/Dakuten_und_Handakuten_Vokabeln.csv', index=False)
yo_on_vokabeln_df.to_csv('../data/csv/Yoon_Kombinationen_Vokabeln.csv', index=False)
