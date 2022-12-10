from app.app.app import *

# Testet Eingaben mit Sonderzeichen
def test_remove_special_characters():
    assert remove_special_characters("John Doe") == "John Doe"
    assert remove_special_characters("John Doe!") == "John Doe"
    assert remove_special_characters("Jön Döe") == "Jn De"
    assert remove_special_characters("!@#") == ""

# Teste Eingaben ohne Sonderzeichen
def test_without_special_characters():
    assert remove_special_characters("Hello world") == "Hello world"
    assert remove_special_characters("H3ll0 w0rld") == "H3ll0 w0rld"

# Teste leere Eingaben
def test_empty_name():
    assert remove_special_characters("") == ""

# Teste Eingaben mit anderem Zeichensatz
def test_other_character_set():
    assert remove_special_characters("Ce texte contient des caractères spéciaux comme é et è") == "Ce texte contient des caractres spciaux comme  et "
