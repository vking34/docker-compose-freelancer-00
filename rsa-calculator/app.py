#!flask/bin/python
from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from ctypes import *
import ctypes

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app = Flask(__name__)

en_msg = ""
encrypted_msg = ""
keyPair = RSA.generate(3072)

lib = cdll.LoadLibrary("./cryptography.so")
class Cryptography_return(Structure):
    _fields_ = [("modulus", c_longlong), ("carmichael", c_longlong),("e", c_longlong), ("d", c_longlong)]
class go_string(Structure):
 _fields_ = [
 ("p", c_char_p),
 ("n", c_longlong)]

lib.isPrime.argtypes = [c_longlong]
#print ("awesome.isPrime(7) = %d" % lib.isPrime(7))

lib.Start.argtypes = [c_longlong, c_longlong]
lib.Start.restype = Cryptography_return
c= lib.Start(2,5)

lib.getEncryptedMessage.restype = c_char_p
str1 = "input"
v = go_string(c_char_p(str1.encode('utf-8')), len(str1))
encryptedMsg = lib.getEncryptedMessage(v, c.modulus, c.e)
print (encryptedMsg.decode())

#lib.getDecryptedMessage.argtypes = [c_char_p, c_longlong, c_longlong, c_longlong]
lib.getDecryptedMessage.restype = c_char_p
b = go_string(c_char_p(encryptedMsg), len(encryptedMsg))
print (lib.getDecryptedMessage(b, c.d,c.modulus).decode('utf-8'))
#print (lib.getDecryptedMessage(b, c.d,c.prime1, c.prime2))



@app.route('/')
def index():
    return redirect(url_for('welcome'))


def check_prime(num):
    if num > 1:
       # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
        # if input number is less than
        # or equal to 1, it is not prime
    else:
        return False


@app.route('/get_pubkey', methods=['POST'])
def get_pubkey():
    public_key = "54321 09876"
    res = {}
    res['success'] = True
    res['public_key'] = public_key
    return res


@app.route('/check_prime', methods=['POST'])
def welcome():
    req = request.get_json()
    first = req['first_num']
    second = req['second_num']
    res = {}
    if check_prime(int(first)) and check_prime(int(second)):
        res['success'] = True
        c= lib.Start(first,second)
        private_key = str(c.d)+ " "+ str(c.modulus)
        public_key = str(c.modulus) + " "+str(c.e) 
        res['private_key'] = private_key
        res['public_key'] = public_key
        return res
    else:
        res['success'] = False
        res['message'] = "Error! Please find another numbers. It is not prime number."
        return res
    pass


@app.route('/encrypt_msg', methods=['POST'])
def encrypt():
    req = request.get_json()
    global en_msg, encrypted_msg
    # This is get public key from frontend
    #public_key = req['pub_key1'] + req['pub_key2']

    global keyPair
    public_key = keyPair.publickey()
    message = req['message']
    # msg = ''.join(format(ord(i), 'b') for i in message)
    #msg = message.encode('ascii')
    v = go_string(c_char_p(message.encode('utf-8')), len(message))
    encryptedMsg = lib.getEncryptedMessage(v, c.modulus, c.e)
    #encryptor = PKCS1_OAEP.new(public_key)
    #encrypted = encryptor.encrypt(msg)
    encryptedMsg = encrypted.decode()
    res = {}
    res['success'] = True
    """ encrypted_msg = encrypted
    en_msg = binascii.hexlify(encrypted).decode('ascii')
    res['message'] = binascii.hexlify(encrypted).decode('ascii') """
    res['message'] = encryptedMsg
    return res

# Decryptor function for frontend (first call)


@app.route('/decrypt_msg', methods=['POST'])
def decrypt_msg():
    req = request.get_json()
    global encrypted_msg
    en_msg = req['en_message']
    private_key1 = req['pri_key1']
    private_key2 = req['pri_key2']
    #encrypted = binascii.unhexlify(en_msg.encode('ascii'))
    print(en_msg)
    #decryptor = PKCS1_OAEP.new(keyPair)
    print(encrypted_msg)
    #decrypted = decryptor.decrypt(encrypted_msg)
    encryptedMsgStruct = go_string(c_char_p(en_msg), len(en_msg))
    decrypted = lib.getDecryptedMessage(encryptedMsgStruct, private_key1,private_key2).decode('utf-8')
    res = {}
    res['success'] = True
    """ print(binascii.hexlify(decrypted).decode('ascii'))
    res['message'] = binascii.hexlify(decrypted).decode('ascii') """
    print(decrypted)
    res['message'] = decrypted
    return res


@app.route('/get_enmsg', methods=['POST'])
def get_enmsg():
    global en_msg
    res = {}
    res['success'] = True
    res['msg'] = en_msg
    return res


if __name__ == '__main__':
    app.run(debug=True)