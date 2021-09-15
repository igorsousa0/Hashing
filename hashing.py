from copy import copy
from Crypto import Random
import binascii
import os
import platform

key = dict.fromkeys(['Privado','Publico'])
hash_send = ''

def generate_keys():
    global key
    key_private = binascii.hexlify(Random.get_random_bytes(10))
    key_public = binascii.hexlify(Random.get_random_bytes(5))
    key['Privado'] = key_private
    key['Publico'] = key_public
    print(f'Chave Privado: {key["Privado"]}\nChave Publica: {key["Publico"]}')

def send(text):
    global hash_send
    hash_send = binascii.hexlify(Random.get_random_bytes(15))
    msg_cifrada = dict.fromkeys(['Mensagem','Chave_publica'])
    msg_cifrada['Mensagem'] = hash_send.decode("utf-8") + text
    msg_cifrada['Chave_publica'] = key['Publico']
    return msg_cifrada

def receive(text):
    if text["Chave_publica"] == key["Publico"]:
        global hash_send
        hash = text['Mensagem']
        hash = hash[0:30]
        if hash_send == hash.encode(encoding='utf-8'):
            msg = text['Mensagem']
            msg = msg.replace(msg[0:30],'')
            return msg
        else:
            return None    
    else:
        print("Chave Modificada")

def main():
    op_sys = platform.system()
    if op_sys == "Linux":
        os.system("clear")
    elif op_sys == "Windows":
        os.system("cls")
    global key
    msg = 'Teste'
    generate_keys()
    msg_cifrada = send(msg)
    msg_retornado = receive(msg_cifrada)
    print(f"Mensagem cifrada: {msg_cifrada['Mensagem']}")
    if msg_retornado != None:
        print (f"Mensagem de retorno: {msg_retornado}")
    

if __name__ == "__main__":
    main()    