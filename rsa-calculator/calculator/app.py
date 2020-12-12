#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_cors import CORS
from ctypes import *
import ctypes

app = Flask(__name__)
CORS(app)

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
decryptedMsg = lib.getEncryptedMessage(v, c.modulus, c.e)
print (decryptedMsg.decode())

#lib.getDecryptedMessage.argtypes = [c_char_p, c_longlong, c_longlong, c_longlong]
lib.getDecryptedMessage.restype = c_char_p
b = go_string(c_char_p(decryptedMsg), len(decryptedMsg))
print (lib.getDecryptedMessage(b, c.d,c.modulus).decode('utf-8'))
#print (lib.getDecryptedMessage(b, c.d,c.prime1, c.prime2))


tasks = [
    {
        'id': 1,
        'arr': [0, 0, 0, 0, 0, 0],
        'data': []
    }
]

