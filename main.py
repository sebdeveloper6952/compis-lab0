import sys
from antlr4 import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafListener import DecafListener

class Printer(DecafListener):
    def __init__(self):
        self.indent = 0

    def enterProgram(self, ctx: DecafParser.ProgramContext):
        print('Program')

    def enterBlock(self, ctx: DecafParser.BlockContext):
        print(f'{" " * self.indent} block | {ctx.getText()}')
        self.indent += 2

    def exitBlock(self, ctx: DecafParser.BlockContext):
        self.indent -= 2

    def enterDeclaration(self, ctx: DecafParser.DeclarationContext):
        print(f'{" " * self.indent} declaration  | {ctx.getText()}')

    def enterVarDeclaration(self, ctx: DecafParser.VarDeclarationContext):
        print(f'{" " * self.indent} varDeclaration  | {ctx.getText()}')

    def enterStructDeclaration(self, ctx: DecafParser.StructDeclarationContext):
        print(f'{" " * self.indent} structDeclaration | {ctx.getText()}')

    def enterVarType(self, ctx: DecafParser.VarTypeContext):
        print(f'{" " * self.indent} varType | {ctx.getText()}')

    def enterMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        print(f'{" " * self.indent} methodDeclaration | ID {ctx.ID()} | {ctx.getText()}')

    def enterMethodType(self, ctx: DecafParser.MethodTypeContext):
        print(f'{" " * self.indent} methodType | {ctx.getText()}')

    def enterParameter(self, ctx: DecafParser.ParameterContext):
        print(f'{" " * self.indent} parameter | ID {ctx.ID()} | {ctx.getText()}')

    def enterParameterType(self, ctx: DecafParser.ParameterTypeContext):
        print(f'{" " * self.indent} parameterType | {ctx.getText()}')

    def enterStatement(self, ctx: DecafParser.StatementContext):
        print(f'{" " * self.indent} statement | {ctx.getText()}')

    def enterLocation(self, ctx: DecafParser.LocationContext):
        print(f'{" " * self.indent} location | ID {ctx.ID()} | {ctx.getText()}')

    def enterExpression(self, ctx: DecafParser.ExpressionContext):
        print(f'{" " * self.indent} expression | {ctx.getText()}')

    def enterMethodCall(self, ctx: DecafParser.MethodCallContext):
        print(f'{" " * self.indent} methodCall | ID {ctx.ID()} | {ctx.getText()}')

    def enterArg(self, ctx: DecafParser.ArgContext):
        print(f'{" " * self.indent} arg | {ctx.getText()}')

    def enterOp(self, ctx: DecafParser.OpContext):
        print(f'{" " * self.indent} op | {ctx.getText()}')

    def enterArith_op(self, ctx: DecafParser.Arith_opContext):
        print(f'{" " * self.indent} arith_op | {ctx.getText()}')

    def enterRel_op(self, ctx: DecafParser.Rel_opContext):
        print(f'{" " * self.indent} rel_op | {ctx.getText()}')

    def enterEq_op(self, ctx: DecafParser.Eq_opContext):
        print(f'{" " * self.indent} eq_op | {ctx.getText()}')

    def enterCond_op(self, ctx: DecafParser.Cond_opContext):
        print(f'{" " * self.indent} cond_op | {ctx.getText()}')

    def enterInt_literal(self, ctx: DecafParser.Int_literalContext):
        print(f'{" " * self.indent} int_literal | {ctx.getText()}')

    def enterChar_literal(self, ctx: DecafParser.Char_literalContext):
        print(f'{" " * self.indent} char_literal | {ctx.getText()}')

    def enterBool_literal(self, ctx: DecafParser.Bool_literalContext):
        print(f'{" " * self.indent} bool_literal | {ctx.getText()}')
        

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DecafLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()

    printer = Printer()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
 
if __name__ == '__main__':
    main(sys.argv)