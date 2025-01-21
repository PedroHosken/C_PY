# Aprendendo if:

#%%

idade = int(input("Entre com sua idade:"))

if 64 >=idade >= 18: # PERMITIDO
    print("Você ser de maior :-)")
    print("Beba à vontade")
elif idade > 64:
    print("Calma, vovô")
else:
    print ("Você ser de menor, seu merda")
# ELIF: else-if, para caso de excessão.
# EXERCÍCIOS DE IF
#%%
# 1. Vender garrafa de água:
garrafa = input("Você gostaria de água com ou sem gás?")
if garrafa == "com gás":
    print("Você será cobrado por 2,50")
else:
    if garrafa == "natural":
        print("Você será cobradopor 1,50")
    else:
        print("Não vendemos nada além de água por aqui")

# %%
# 2. 
