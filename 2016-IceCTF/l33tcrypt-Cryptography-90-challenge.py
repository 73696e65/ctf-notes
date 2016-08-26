#!/usr/bin/python
from Crypto.Cipher.AES import AESCipher
import SocketServer as ss
import signal
import base64

from secret import KEY, FLAG

PORT = 6001

def pad(text, bs):
    text = text + FLAG
    pad_num = (bs - len(text) % bs)
    return text + chr(pad_num) * pad_num


def recvline(req):
    buf = b""
    while not buf.endswith(b"\n"):
        buf += req.recv(1)
    return buf


class RequestHandler(ss.BaseRequestHandler):
    def handle(self):
        req = self.request

        signal.alarm(5)

        req.sendall("Welcome to l33tserver where all your encryption needs are served.\n")
        req.sendall("Send me something to encrypt:\n")
        data = recvline(req).strip()
        try:
            data = base64.b64decode(data)
        except:
            req.sendall("bad data\n")
            req.close()
            return
        if not data.startswith("l33tserver please"):
            req.sendall("You didnt say the magic word :(\n")
            req.close()
            return
        c = AESCipher(KEY).encrypt(pad(data, 16))
        req.sendall("Your l33tcrypted data:\n")
        req.sendall(base64.b64encode(c) + "\n")
        req.close()


class TCPServer(ss.ForkingMixIn, ss.TCPServer):
    pass


ss.TCPServer.allow_reuse_address = True
server = TCPServer(("0.0.0.0", PORT), RequestHandler)

print("Server listening on port %d" % PORT)
server.serve_forever()
