#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Created: 2014-03-12
# デザインパターン練習用

class FigureSkate:

    def play_program(self):
        self.jump()
        self.spin()
        self.step()

    def jump(self, elements = []):
        print "oh... you have to jump..."

    def spin(self, elements = []):
        print "oh... you must spin..."

    def step(self, elements = []):
        print "oh... you have to step..."

class Debut(FigureSkate):

    def jump(self, elements = ["loop"]):
        print "----jump----"
        for element in elements:
            print element

    def spin(self, elements = ["stand"]):
        print "----spin----"
        for element in elements:
            print element

    def step(self, elements = ["straight"]):
        print "----step----"
        for element in elements:
            print element

if __name__ == '__main__':
    debut = Debut()
    debut.play_program()
