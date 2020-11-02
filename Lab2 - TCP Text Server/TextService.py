
import socket, json, os, sys, optparse


class Server:

    def __init__(self, port):
        self.interface = '127.0.0.1'
        self.port = port

    def listen(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.interface, self.port))
        s.listen(0)
        print("[LISTENING] - Server is listeninig for coming connections")
        self.connection, address = s.accept()
        print("[CONNECTED] device from" + str(address))


    def send(self, data):
        msg = json.dumps(data)
        self.connection.send(msg.encode())


    def receiver(self):
    	msg = ""
    	while True:
    		try:
    			msg = msg + self.connection.recv(1024).decode()
    			return json.loads(msg)
    		except ValueError:
    			continue


    def run(self):
    	self.listen()
    	packet = self.receiver()
    	if (packet[0] == 'encode_decode'):
    		res = self.textEncoder(packet[1], packet[2])
    	if (packet[0] == 'change_text'):
    		res = self.textChanger(packet[1], packet[2])
    	self.send(res)


    def textEncoder(self, text, key):
    	encoded = ""
    	for i in range(len(text)):
    		char = text[i]
    		k = key[i%len(key)]
    		encoded += chr(ord(char) ^ ord(k))
    	return encoded


    def textChanger(self, text, swaps):
    	txt = text.split()
    	swap = eval(swaps)
    	for word in txt:
    		if word in swap.keys():
    			text = text.replace(word, swap[word])
    	return text



class Client:

	def __init__(self, mode):
		self.mode = mode


	def connect(self, interface, port):
		self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.connection.connect((interface, port))


	def send(self, data):
		msg = json.dumps(data)
		self.connection.send(msg.encode())


	def receiver(self):
		msg = ""
		while True:
			try:
				msg = msg + self.connection.recv(1024).decode()
				return json.loads(msg)
			except ValueError:
				continue


	def processor(self, f, a):
		msg = open(f, 'r').read()
		add = open(a, 'r').read()
		data = []
		data.append(self.mode)
		data.append(msg)
		data.append(add)
		self.send(data)
		packet = self.receiver()
		print(packet)



def main():
	parser = optparse.OptionParser()
	parser.add_option("-p", metavar="PORT", type= int, help="Listening Port")
	if sys.argv[1] == "client":
		parser.add_option("--host", dest = "interface", help="Destination IP Address")
		parser.add_option("-m", dest = "mode", help="Operating Mode")
		parser.add_option("-f", dest = "f", help="File")
		parser.add_option("-a", dest = "a", help="[JSON/KEY]")
	(options,arguments) = parser.parse_args()
	if sys.argv[1] == "client":
		client = Client(options.mode)
		client.connect(options.interface, options.p)
		client.processor(options.f, options.a)
	else:
		server = Server(options.p)
		server.run()

if __name__== "__main__":
	main()