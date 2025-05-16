import json
import os

TRANSLATIONS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "lang")
DEFAULT_LANG = "fr"

# Récupère la traduction d'une clé donnée dans le fichier de langue spécifié
def get_translation(key: str, lang: str = DEFAULT_LANG) -> str:
    try:
        lang_file = os.path.join(TRANSLATIONS_DIR, f"{lang}.json")
        if not os.path.exists(lang_file):
            raise FileNotFoundError(f"Fichier de traduction pour '{lang}' introuvable.")

        with open(lang_file, "r", encoding="utf-8") as file:
            translations = json.load(file)

        return translations.get(key, key)
    except Exception as e:
        print(f"Erreur lors de la récupération de la traduction : {e}")
        return key

# Formatte la traduction avec les arguments fournis
def translate(key: str, lang: str = DEFAULT_LANG, **kwargs) -> str:
    translation = get_translation(key, lang)
    if kwargs:
        try:
            return translation.format(**kwargs)
        except (KeyError, ValueError) as e:
            print(f"Erreur lors du formatage de la traduction : {e}")
            return translation
    return translation