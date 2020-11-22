#!/usr/bin/python3


from bs4 import BeautifulSoup
import requests
import socket
import argparse
import sys


HOST = '127.0.0.1'
PORT = 1234
MAX_BYTES = 65535

# Using a default header to be seen as a legitimate user
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

class Server:

    def __init__(self, interface, port):
        self.interface = interface
        self.port = port


    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.interface, self.port))
        s.listen(1)
        print(f"[LISTENING] - Server is listening at {s.getsockname()}")


        while True:
            print("="*30)
            conn, addr = s.accept()
            print(f"[CONNECTED] - Client is connected from {addr}")
            url = (conn.recv(MAX_BYTES)).decode('utf-8')
            data = f"[+] The number of <img> tag(s): {str(self.countImage(url))}\n[+] The number of leaf <p> tag(s): {str(self.countParagraph(url))}"
            conn.sendall(data.encode('utf-8'))
            print(f"[SENDING] - Server is sending request to the client at {conn.getpeername()}")
            print("="*30)
        s.close()



    def countParagraph(self, url):
        webpage = requests.get(url, headers)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        count = 0
        pTags = soup.find_all('p')
        for p in pTags:
            if not p.find_all('p'):
                count += 1
        return count


    def countImage(self, url):
        webpage = requests.get(url, headers)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        count = 0
        imgs = soup.find_all('img')
        for _ in imgs:
            count += 1
        return count



class Client:
    def __init__(self, interface, port):
        self.interface = interface
        self.port =port


    def process(self, url):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.interface, self.port))
        s.sendall(url.encode('utf-8'))
        print("="*30)
        print("[ACCEPTED] - The result is accepted:") 
        print(f"{s.recv(MAX_BYTES).decode('utf-8')}")
        print("="*30)
        s.close()



def main():
    parser = argparse.ArgumentParser(description="Web Scrapper by Hajiahmad Ahmadzada")
    roles = {'client': Client, 'server': Server}
    parser.add_argument("role", choices=roles, help="Roles: 1.Server 2.Client")
    
    if sys.argv[1] == 'client':
        parser.add_argument('-p', metavar='webpage', type=str, help='The target URL')
    args = parser.parse_args()


    if args.role == 'server':
        Server(HOST, PORT).start()
    
    elif args.role == 'client':
        Client(HOST, PORT).process(args.p if "http://" in args.p or "https://" in args.p else f"https://{args.p}")

if __name__ == "__main__":
    main()
