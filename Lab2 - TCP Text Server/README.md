
# Lab2 - Text Service - Chapter 3 (TCP) - Python Network Programming


## Description

It is console app. We can send two types of mode from client terminal to the server

**Change Text**:
- We send our text and which words to change in .json format. The server will do it and sends the processed text back to us.

**Encoder/Decoder**:
- We send our text and key file. The server will do it in XOR and then sends the processed text back to us (client).

## Requirements

- Pyhton3
- Windows/\*nix OS

## Installation

```
git clone https://github.com/ahmedvuqarsoy/Network-Programming.git
cd "Lab2 - TCP Text Server"
pip install -r requirements.txt
```

## Usage

**Options** for the program:

```
-h, --help			Help Menu
--host				Destination IP Address
-m					Client working mode
-p 					Destination Port
-f 					File
-a 					Additional file
```


**Server** mode:

```
python3 TextService.py server -p <PORT>
```

**Client** mode:

```
python3 TextService.py client -h <DST-IP> -p <PORT> -m <MODE> -f <FILE> -a <ADDITIONAL>
```