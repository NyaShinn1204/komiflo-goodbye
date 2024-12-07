import random
import sys
import json
import time

def h(e):
    return list(range(e))

def i():
    e = 4022871197
    def inner(t=None):
        nonlocal e
        if t is not None:
            t = str(t)
            for n in range(len(t)):
                e += ord(t[n])
                i_val = 0.02519603282416938 * e
                e = int(e)
                e = e & 0xFFFFFFFF  # e >>> 0
                i_val -= e
                i_val *= e
                e = int(i_val) & 0xFFFFFFFF
                i_val -= e
                e += 4294967296 * i_val
            return 2.3283064365386963e-10 * (int(e) & 0xFFFFFFFF)
        else:
            e = 4022871197
    return inner

def r_t(e=None):
    class D:
        def __init__(self):
            self.r = 48
            self.a = 1
            self.o = self.r
            self.s = [0] * self.r
            self.c = 0
            self.l = i()
            for t in range(self.r):
                self.s[t] = self.l(random.random())
            if e is not None:
                self.seed(e)
        
        def u(self):
            self.o += 1
            if self.o >= self.r:
                self.o = 0
            e = 1768863 * self.s[self.o] + 2.3283064365386963e-10 * self.a
            self.a = int(e)
            self.s[self.o] = e - self.a
            return self.s[self.o]

        def d(self, e_value):
            return int(e_value * (self.u() + 1.1102230246251565e-16 * int(2097152 * self.u())))
        
        def string(self, e_length):
            n = ''
            for t in range(e_length):
                n += chr(33 + self.d(94))
            return n
        
        def p(self, *args):
            e_args = ''.join(map(str,args))
            for t in e_args:
                for n in range(self.r):
                    value = self.l(t)
                    self.s[n] -= value
                    if self.s[n] < 0:
                        self.s[n] += 1
        
        def cleanString(self, e_str):
            e_str = e_str.strip()
            e_str = ''.join(ch for ch in e_str if ord(ch) >= 32)
            e_str = e_str.replace('\n ', '\n')
            return e_str
        
        def hashString(self, e_str):
            e_str = self.cleanString(e_str)
            self.l(e_str)
            for t in range(len(e_str)):
                c = ord(e_str[t])
                for n in range(self.r):
                    self.s[n] -= self.l(c)
                    if self.s[n] < 0:
                        self.s[n] += 1
        
        def seed(self, e_value=None):
            if e_value is None:
                e_value = random.random()
            if not isinstance(e_value, str):
                e_value = json.dumps(e_value)
            self.initState()
            self.hashString(e_value)
        
        def addEntropy(self, *args):
            e_list = args
            self.c += 1
            e_str = str(self.c) + str(int(time.time() * 1000)) + ''.join(map(str, e_list)) + str(random.random())
            self.p(e_str)
        
        def initState(self):
            self.l()
            for t in range(self.r):
                self.s[t] = self.l(" ")
            self.a = 1
            self.o = self.r
        
        def done(self):
            self.l = None
        
        def range(self, e_value):
            return self.d(e_value)
        
        def random(self):
            return self.d(sys.float_info.max - 1) / sys.float_info.max
        
        def floatBetween(self, e_start, e_end):
            return self.random() * (e_end - e_start) + e_start
        
        def intBetween(self, e_start, e_end):
            return int(self.random() * (e_end - e_start + 1)) + e_start

    return D()

def g(e, t):
    n = r_t(t)
    s = e[:]
    i = len(s)
    while i:
        a = int(n.random() * i)
        i -=1
        o = s[a]
        s[a] = s[i]
        s[i] = o
    return s

#seed = 12257281
#y_h = (h(11*15))
#print(y_h)
#test_map = g(y_h, seed)
#print("map:", json.dumps(test_map, indent=2))