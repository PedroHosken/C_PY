# Laçõs de Repetição
# While Loop
#%%
i = 0
while i <= 10:
    print(i)
    i += 1
# %%
while True:
    i = int(input("Digite um número (0 para sair): "))
    if i == 0:
        print("Saindo do loop...")
        break
    print(f"Você digitou: {i}")
    
# Exercícios da lista
# %%
# Ex01 = Contagem de letras a
palavra = input("Digite uma palavra: ")
contador = 0
