# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:46:09 2024

@author: Lenovo
"""

from googletrans import Translator

def translatelatin(sentence, trans_to):
    romance_languages = {
    "Spanish": "es",
    "French": "fr",
    "Italian": "it",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Catalan": "ca",
    "Galician": "gl",
    "Occitan": "oc",
    "Lombard": "lmo",
    "Sicilian": "scn",
    "Neapolitan": "nap",
    "Asturleonese": "ast",
    "Friulian": "fur",
    "Corsican": "co",
    "Aragonese": "an",
}
    lang = trans_to.title()
    
    if lang not in romance_languages:
        raise NameError(f"{lang} is not a romance language")
    
    lang_to = romance_languages[lang]
    translateto = Translator()
    translated_text = translateto.translate(sentence, dest=lang_to)

    return translated_text.text

def poor_man_chart(sentence):
    """Displays a poor mans bar chart of letters occuring in a sentence
       Parameters: input is a list 
       """
    sentence.sort()    
    letters = {}
    for ch in sentence:
        if ch.isalpha():
            if ch not in letters:
                letters[ch] = [ch]
            else:
                letters[ch].append(ch)
    for key, val in letters.items():
        print(f"'{key}': {val}")

def main():
    sentence = input("Enter a sentence: ")
    while type(sentence) !=str or (sentence == ""):
        print("Invalid input")
        sentence = input("Enter a sentence: ")
        
    trans_to = input("Enter a romance language: ")
    trans_sentence = translatelatin(sentence, trans_to.title())
    
    print(f"\nThe sentence in {trans_to.title()}:\n{trans_sentence}")
    print("Character count:")
    sentence = list(trans_sentence.lower())
    
    poor_man_chart(sentence)

if __name__ == "__main__":
    main()