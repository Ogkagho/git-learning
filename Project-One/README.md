# Sentence Translator and Character Frequency Chart

This Python script allows users to translate a given sentence into a specified Romance language using the Google Translate API. Additionally, it displays a simple text-based bar chart of the character occurrences in the translated sentence.

## Features

- **Translate to Romance Languages**: The script translates the input sentence into various Romance languages, including Spanish, French, Italian, and others.
- **Character Frequency Chart**: It generates a text-based bar chart that shows the frequency of each alphabetic character in the translated sentence.

## Functions

- **`translatelatin(sentence, trans_to)`**: 
  - Translates the input sentence to the specified Romance language.
  - **Parameters**: 
    - `sentence` (str): The sentence to translate.
    - `trans_to` (str): The target Romance language for translation.
  
- **`poor_man_chart(sentence)`**: 
  - Displays a text-based bar chart showing the frequency of each alphabetic character in the input sentence.
  - **Parameters**: 
    - `sentence` (list): A list of characters in the sentence.

- **`main()`**: 
  - The main entry point for user interaction.
  - Takes user input for a sentence and the target Romance language, processes the translation, and generates the character frequency chart.

## Usage

1. Run the script:
   ```bash
   python your_script_name.py
