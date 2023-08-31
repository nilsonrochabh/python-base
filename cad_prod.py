#!/usr/bin/env python3

"""cad prod"""
__version__="0.1.0"

# prod_nome = "Caneta"
# prod_cor1= "Azul"
# prod_cor2= "branco"
# prod_preco = 3.23
# prod_dime_altura = 12.1
# prod_dime_largura = 0.8
# prod_estoque = True
# prod_cod = 45678
# prod_codebar = None
import pprint
#dicionario
prod = {
    "nome": "Caneta",
    "cores": [ "azul", "branca"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,    
    },
    "estoque": True,
    "cod": 456789,
    "codebar": None,
}
cliente={
    "nome":"Nilson"
    
}
compra ={
    "cliente" : cliente,
    "produto" : prod,
    "quantidade": 3
    
}
pprint.pprint(compra)