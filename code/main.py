from googletrans import Translator

def languages_list():
    print("----------Languages list----------")
    print("1 - English")  # en
    print("2 - French")  # fr
    print("3 - German")  # de
    print("4 - Greek")  # el
    print("5 - Italian")  # it
    print("6 - Japanese")  # ja
    print("7 - Portuguese Brazil")  # pt
    print("8 - Russian")  # ru
    print("9 - Spanish")  # es
    print("10 - Traditional Chinese")  # zh-cn
    print("--------------------------------------")

menu = {
    1: 'en',
    2: 'fr',
    3: 'de',
    4: 'el',
    5: 'it',
    6: 'ja',
    7: 'pt',
    8: 'ru',
    9: 'es',
    10: 'zh-cn'
}

def translateMessage(message, source_language, translation_language):
    translator = Translator()
    translation = translator.translate(message, src=source_language, dest=translation_language)
    return translation.text

languages_list()

select_source_language = None
source_language = None
while select_source_language not in menu:
    try:
        select_source_language = int(input("Enter source language code: "))
        if select_source_language in menu:
            source_language = menu.get(select_source_language)
            print(f"Selected: {source_language}")
        else:
            print("Invalid source language")
    except ValueError:
        print("Invalid input. Please enter an integer.")

select_translation_language = None
translation_language = None
while select_translation_language not in menu:
    try:
        select_translation_language = int(input("Enter language code for translation: "))
        if select_translation_language in menu:
            translation_language = menu.get(select_translation_language)
            print(f"Selected: {translation_language}")
        else:
            print("Invalid translation language")
    except ValueError:
        print("Invalid input. Please enter an integer.")

message = input("\nEnter the message to be translated: ")

translate_message = translateMessage(message, source_language, translation_language)
print(f"Message translated from {source_language} to {translation_language}: {translate_message}")
