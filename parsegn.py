from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from GNLexer import GNLexer
from GNParser import GNParser
from GNListener import GNListener


class Printer(GNListener):
  def enterImport_stmt(self, ctx):
    importPath =  ctx.getChild(0, GNParser.StringContext).getText()[1:-1]
    print("import '%s'" % importPath)
  def enterRule_stmt(self, ctx):
    ruleType = ctx.getChild(0).symbol.text
    nameString = ctx.getChild(0, GNParser.StringContext)
    name = "" if nameString == None else nameString.getText()[1:-1]
    print("%s '%s'" % (ruleType, name))

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