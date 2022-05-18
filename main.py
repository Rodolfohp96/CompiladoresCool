from antlr4 import *
from antlr.coolLexer import coolLexer
from antlr.coolParser import coolParser

from listeners.dummy import dummyListener
from listeners.tree import TreePrinter

def compile(file):
    parser = coolParser(CommonTokenStream(coolLexer(FileStream(file))))
    tree = parser.program()

    walker = ParseTreeWalker()
    
    #walker.walk(dummyListener(), tree)

    walker.walk(TreePrinter(), tree)


def dummy():
    raise SystemExit(1)

if __name__ == '__main__':
    compile('resources/semantic/input/anattributenamedself.cool')
