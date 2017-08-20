#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# measurement of accessor method
# Created: 2014/04/19

#toeLoop
#salchow
#loop
#flip
#lutz
#axel

class listAccessor:

    def __init__(self):
        self.toeLoop = None
        self.salchow = None
        self.loop = None
        self.flip = None
        self.lutz = None
        self.axel = None

    def setToeLoop(self, value):
        self.toeLoop = value

    def getToeLoop(self):
        return self.toeLoop

    def setSalchow(self, value):
        self.salchow = value

    def getSalchow(self):
        return self.salchow

    def setLoop(self, value):
        self.loop = value

    def getLoop(self):
        return self.loop

    def setFlip(self, value):
        self.flip = value

    def getFlip(self):
        return self.flip

    def setLutz(self, value):
        self.lutx = value

    def getLutz(self):
        return self.lutz

    def setAxel(self, value):
        self.axel = value

    def getAxel(self):
        return self.axel

class decoAccessor:

    def __init__(self):
        self.x = None

    def getx(self):
        return self.x

    def setx(self, x):
        self.x = x

    x = property(getx, setx)

if __name__ == '__main__':
    import time
    t = time.time()
    for n in range(1,10000000):
        a = listAccessor()
        a.setLoop(n)
        a.setSalchow(n)
        a.setToeLoop(n)
        a.setFlip(n)
        a.setLutz(n)
        a.setAxel(n)
        b = a.getLoop()
        b = a.getSalchow()
        b = a.getToeLoop()
        b = a.getFlip()
        b = a.getLutz()
        b = a.getAxel()
    print "listAccessor: %s sec." % (t - time.time())
    t = time.time()
    for n in range(1,10000000):
        A = decoAccessor()
        A.loop = n
        A.salchow = n
        A.toeLoop = n
        A.flip = n
        A.lutz = n
        A.axel = n
        B = A.toeLoop
        B = A.salchow
        B = A.loop
        B = A.flip
        B = A.lutz
        B = A.axel
    print "decoAccessor: %s sec." % (t - time.time())
    t = time.time()
    for n in range(1,10000000):
        A = decoAccessor()
        A.loop = n
        A.salchow = n
        A.toeLoop = n
        A.flip = n
        A.lutz = n
        A.axel = n
        B = A.toeLoop
        B = A.salchow
        B = A.loop
        B = A.flip
        B = A.lutz
        B = A.axel
    print "decoAccessor: %s sec." % (t - time.time())
    t = time.time()
    for n in range(1,10000000):
        a = listAccessor()
        a.setLoop(n)
        a.setSalchow(n)
        a.setToeLoop(n)
        a.setFlip(n)
        a.setLutz(n)
        a.setAxel(n)
        b = a.getLoop()
        b = a.getSalchow()
        b = a.getToeLoop()
        b = a.getFlip()
        b = a.getLutz()
        b = a.getAxel()
    print "listAccessor: %s sec." % (t - time.time())

