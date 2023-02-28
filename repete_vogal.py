"""
Repete vogais
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.
ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""
#VOGAIS = "aeiouãõâôêéáíó"  # constante

words = []
while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()
    if not word: # condição de parada
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuação com função.
        if letter.lower() in "aeiouãõâôêéáíó":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)
    
for word in words:
    print(word)     
