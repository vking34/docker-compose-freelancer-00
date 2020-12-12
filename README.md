# RSA Encryption System

## General Goal
- Provide a safe system that can encrypt your message. You don't have to worry about hackers or strangers  know about content of your chat. 

## Implementation

- Golang(Calculation): Golang will play as both encrypter and decryptor. Since Go is extremely good at calculation, using Go for this task will guarantee faster speed for server 
- Python (REST API): Since it's easy to import functions and data from other languages to Python, it is use as the bridge between client and  calculation. 
Here I use Flask framework.
- JavaScript (Front-end) Javascript is known for its diversity and ability to work in web enviroment. ReactJS is used to generate UI and speed up development process.


## Instruction 
- If you are running from home machine.
    + Step 1: install python 3 

## Communication
- We are separate the system into 3 parts: Calculator, Server and Client. Calculator will communicate with Server via Python "ctyes" and native library. 
- Communication between Server- Client (or front end - back end) will be set up via REST API (Flask). Server will receive request from client via HTTPS

## Feature
- Able to encrypt the message
- Able to decrypt the message
- In the future, I can save the chat log for each user so the message that they sent or receive will be save in the server. 