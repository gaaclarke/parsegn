from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from GNLexer import GNLexer
from GNParser import GNParser
from GNListener import GNListener

class Printer(GNListener):
  def enterGn_file(self, ctx):
    print("enter gn file")
  def enterImport_stmt(self, ctx):
    print("import")
  def enterRule_stmt(self, ctx):
    print("enter rule" + str(type(ctx)))

def main():
  input_stream = FileStream(sys.argv[1])
  lexer = GNLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = GNParser(stream)
  tree = parser.gn_file()
  walker = ParseTreeWalker()
  printer = Printer()
  walker.walk(printer, tree)

if __name__ == "__main__":
  main()