#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Observer, the design pattern
# This program is originated from Expert Python Programing

# Created: 2014-04-17

class Event:
    _observer = []

    def __init__(self, subject):
        self.subject = subject

    @classmethod
    def register(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def unregister(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def notify(cls, subject):
        event = cls(subject)
        for o in cls._observers:
            o(event)

class WriteEvent(Event):
    _observers = []
    def __repr__(self):
        return 'WriteEvent'

class AnotherObserver:
    def __call__(self, event):
        print "Yeah %s told me !" % event

if __name__ == "__main__":
    def log(event):
        print '%s was written' % event.subject
    WriteEvent.register(log)
    WriteEvent.register(AnotherObserver())
    WriteEvent.notify('a given file')
