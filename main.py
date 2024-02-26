"""Multimídia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ea5F6LiglUeJa3Hx8b8BFVfdVJeq401a

#Instalar a Librosa pra poder fazer o mashup e o Spleeter pra poder separar
"""

"""!pip install librosa;
   !pip install spleeter;
"""
"""# Separar os sons por meio do spleeter (usar arquivos .wav)"""


import separate_vocals_instruments

# recebe músicas de entrada, cria saídas das músicas separadas em vocal e instrumentos
if __name__ == "__main__":
    input_music1= "" # Colocar o caminho pra música 1
    input_music2 = "" # Colocar caminho pra música 2
    output_music1 = "/content/separateMusic1" # Cria pasta
    output_music2 = "/content/separateMusic2" # Cria pasta

    separate_vocals_instruments(input_music1, output_music1, input_music2, output_music2)


"""# Juntar os sons usando Librosa (usar arquivos .wav)"""

import create_mashup

# recebe duas entradas de áudio .wav e retorna o mashup
if __name__ == "__main__":
    file1 = "" #input q vai determinar a duração
    file2 = ""
    output_file = "/content/mashup.wav"  # Exemplo de caminho de saída no Google Colab

    create_mashup(file1, file2, output_file)
