from random import choice
import string
#funções do codigo.

def gerador_n(tamanho):
 valores= string.digits
 senha=''
 for i in range(tamanho):
  senha += choice(valores)
 return senha

def gerador_l(tamanho):
 valores= string.ascii_lowercase
 senha=''
 for i in range(tamanho):
  senha += choice(valores)
 return senha

def gerador_m(tamanho):
 valores_l= string.ascii_lowercase
 valores_n=string.digits
 valores=valores_l+valores_n
 senha=''
 for i in range(tamanho):
  senha += choice(valores)
 return senha

#estrutura de escolha
print("-"*30)
print("---gerador de senha---")
tamanho=int(input("tamanho da senha:"))
print("-"*30)
print("escolha entre:")
print("senha numerica--n")
print("senha alfabetica--a")
print("senha mista---m")
escolha=str(input("digite sua escoliada:"))
print("-"*30)
if(escolha=="n"):
 print("sua senha:")
 print(gerador_n(tamanho))
elif(escolha=="a"):
  print("sua senha:") 
  print(gerador_l(tamanho))
elif(escolha=="m"):
  print("sua senha:")
  print(gerador_m(tamanho))
print("-"*30)

