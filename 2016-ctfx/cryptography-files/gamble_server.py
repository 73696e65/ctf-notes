#/usr/bin/env python
from Crypto.Random import random, atfork
from Crypto.Util.number import *

import SocketServer,threading,os,time
import signal

from secret1 import FLAG

PORT = 3001

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def createRandom():
    mbl = getRandomRange(65,100)
    m = getPrime(mbl)
    abl = getRandomRange(64,mbl)
    a = getPrime(abl)
    c = getRandomRange(0, m)
    s = getRandomRange(1, m)
    return Rand(m, a, c, s)

class Rand:
    def __init__(self, m, a, c, s):
        self.s = s
        self.a = a
        self.c = c
        self.m = m
    def next(self):
        self.s = (self.a*self.s+self.c)%self.m
        return self.s

class incoming(SocketServer.BaseRequestHandler):
    def handle(self):
        atfork()
        req = self.request

        def recvline():
            buf = ""
            while not buf.endswith("\n"):
                buf += req.recv(1)
            return buf
        signal.alarm(120)

        req.sendall("#############################\n")
        req.sendall("Welcome to the Gambling game!\n")
        req.sendall("#############################\n")
        req.sendall("\n")

        money = 20
        random = createRandom()
        while True:
            req.sendall("You currently have $%d\n"%money)
            req.sendall("How much would you like to bet?: \n")
            bet = recvline()
            if isInt(bet):
                bet = int(bet)
                if bet>=1 and bet<=money:
                    req.sendall("Guess a number!: \n")
                    guess = recvline()
                    if isInt(guess):
                        guess= int(guess)
                        rand = random.next()
                        if guess==rand:
                            req.sendall("You won the bet!\n")
                            money += bet
                            req.sendall("You now have $%d\n"%money)
                            req.sendall("\n")
                            if money>=10**6:
                                req.sendall("Wow! You're a millionaire!\n")
                                req.sendall(FLAG+"\n")
                            req.sendall("Would you like to play again? (Y/N): \n")
                            if recvline().strip()=="Y":
                                random = createRandom()
                                continue
                            else:
                                break
                        else:
                            req.sendall("You lost the bet!\n")
                            req.sendall("You should have guessed %d. :(\n"%rand)
                            money -= bet
                            if money==0:
                                req.sendall("You're all out of money! You lose!\n")
                                break
                            else:
                                req.sendall("Would you like to play again? (Y/N): \n")
                                if recvline().strip()!="Y":
                                    break
                    else:
                        req.sendall("Invalid input!\n")
                        break
                else:
                    req.sendall("Invalid bet!\n")
                    break
            else:
                req.sendall("Invalid input!\n")
                break
        req.sendall("Bye!\n")
        req.close()

class ReusableTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
  pass

SocketServer.TCPServer.allow_reuse_address = True
server = ReusableTCPServer(("0.0.0.0", PORT), incoming)

print "Server listening on port %d" % PORT
server.serve_forever()
