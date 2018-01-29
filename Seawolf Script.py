# Reagan Yuan
# 109696144

import math
import sys
from operator import *
import ply.lex as lex
import ply.yacc as yacc

# Node Class
class Node():
    def __init__(self):
        pass
    def evaluate(self):
        pass
    def execute(self):
        pass

class Float_Node(Node):
    def __init__(self, value):
        super(Float_Node, self).__init__()
        self.value = float(value)
    def evaluate(self):
        return float(self.value)

#Number node
class Number_Node(Node):
    def __init__(self, value):
        self.value = int(value)
    def evaluate(self):
        return int(self.value)
    def __repr__(self):
        return str(self.value)

#String node
class String_Node(Node):
    def __init__(self, value):
        self.value = str(value)
    def evaluate(self):
        return self.value
    def __repr__(self):
        return str(self.value)

#Variable node
class Variable_Node(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        find_variable = grammar_stack.search_for_elem(self)
        if issubclass(type(find_variable),Node):
            return find_variable.evaluate()
        else:
            return find_variable


# Binary operations
class BinaryOperations(Node):
    def __init__(self, left_expression, right_expression,operator):

        self.left_expression = left_expression
        self.right_expression = right_expression
        self.operator = operator

    def evaluate(self):
        left_expression = self.left_expression
        right_expression = self.right_expression


        if issubclass(type(self.left_expression),Node) == True:
            left_expression = left_expression.evaluate()
        if issubclass(type(self.right_expression),Node)== True:
            right_expression = right_expression.evaluate()

        if self.operator == '*':
            return mul(left_expression, right_expression)
        elif self.operator == '/':
            return left_expression/right_expression
        elif self.operator == '//':
            return floordiv(left_expression, right_expression)
        elif self.operator == '%':
            return mod(left_expression,right_expression)
        elif self.operator == '**':
            return math.pow(left_expression,right_expression)
        elif self.operator == '+':
            return add(left_expression,right_expression)
        elif self.operator == '-':
            return sub(left_expression,right_expression)
        elif self.operator == 'and':
            return and_(left_expression,right_expression)
        elif self.operator == 'or':
            return or_(left_expression,right_expression)
        elif self.operator == '>':
            return gt(left_expression, right_expression)
        elif self.operator == '<':
            return lt(left_expression, right_expression)
        elif self.operator == '<=':
            return le(left_expression, right_expression)
        elif self.operator == '>=':
            return ge(left_expression, right_expression)
        elif self.operator == '==':
            return eq(left_expression, right_expression)
        elif self.operator == '<>':
            return ne(left_expression, right_expression)
        elif self.operator == 'in':
            return left_expression in right_expression

#List nodes
class List_Node(Node):
    def __init__(self, list_of_items):
        self.items = []

        for i in range(0,len(list_of_items)):
            if issubclass(type(list_of_items[i]),Node):
                list_of_items[i] = list_of_items[i].evaluate()

    def evaluate(self):
        return self.items


# Statement Nodes
class Statement_Node(Node):
    def __init__(self, statement, isPrint=False, can_access=False, value=None,
                 access_value=None):
        if statement != None:
            self.statement = statement
        else:
            self.statement = None

        self.print = isPrint
        self.ASSIGNVALUE = can_access
        self.value = value
        self.access_value = access_value


    def evaluate(self):
        temp_statement = self.statement
        temp_value = self.value
        temp_access = self.access_value

        if self.access_value  is not None:
            s1 = issubclass(type(temp_statement),Node)
            s2 = isinstance(temp_access,list)
            s3 = issubclass(type(temp_access),Node)
            if s1:
                temp_statement = temp_statement.evaluate()
            if s2:
                return temp_statement[temp_access[0].evaluate()][temp_access[1].evaluate()]
            if s3:
                temp_access = temp_access.evaluate()
            return temp_statement[temp_access]
        elif self.print == True:
            if issubclass(type(temp_statement), Node):
                temp_statement = temp_statement.evaluate()
            temp_statement = str(temp_statement).replace('\\n', '\n',1000)
            print(str(temp_statement), end='')
    
            return None
        elif self.ASSIGNVALUE == True:
            if not issubclass(type(temp_value), Node):
                pass
            else:
                temp_value = temp_value.evaluate()
            grammar_stack.set_elem(temp_statement, temp_value)
        return temp_statement


#Statement Lists
class Statement_List(list):
    def evaluate(self):
        # evaluate each statement
        for i in range(0,len(self)):
            self[i].evaluate()
            
# Block Nodes
class Block_Node(Node):
    def __init__(self, statements, root):
        self.executables = statements
        self.root = root
    def execute(self):
        end_stack_symbol= Scope()
        if grammar_stack != None:
            grammar_stack.push(end_stack_symbol)
            self.executables.evaluate()
            # pop off the end of stack variable
            grammar_stack.pop()

# If statements
class If_Node(Node):

    def __init__(self, conditional, block, elseblock):
        self.condition = conditional
        self.block = block
        self.elseblock = elseblock

    def evaluate(self):
        evaluate_val = bool(self.condition.evaluate())
        if evaluate_val:
            self.block.execute()
            return
        elif self.elseblock is not None:
            self.elseblock.execute()
            return

# change
# While Loop
class While_Node(Node):

    def __init__(self, condition, block):
        super(While_Node, self).__init__()
        self.condition = condition
        self.block = block

    def evaluate(self):
        retVal = self.condition.evaluate()
        while bool(retVal):
            self.block.execute()
            retVal = self.condition.evaluate()

###############################################################################
class AST(object):
    # initialize lex and yacc
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.parser = yacc.yacc(module=self)

    def compile_(self, file):
        root = yacc.parse(file.read())
        if root.root == True:
            root.execute()
            return
        print("Syntax Error")


#change name of scope
class Scope(dict):
     def __init__(self, **dp):
         return
#############################################################################################################################
#                                           Tokens                                                                          #
#############################################################################################################################
class grammar(AST):

    # reserved keywords
    reserved = {
        'not': 'NOT',
        'and': 'AND',
        'or': 'OR',
        'in': 'IN',
        'print': 'PRINT',
        'while': 'WHILE',
        'if': 'IF',
        'else': 'ELSE'

    }

    tokens = ('OR','NOT','MINUS','NUMBER','ID','PLUS','IN','AND','FLOORDIV','DIVIDE','TIMES','IS','ISNOT','GREATERTHENEQUAL',
              'LESSTHENEQUAL','GREATERTHEN','LESSTHEN','ASSIGNVALUE','EXPONENTIAL','MOD','LPAREN','RPAREN','STRING','RBRACKET',
              'LBRACKET','COMMA','LCURLYBRACKET','RCURLYBRACKET','PRINT','SEMICOLON','WHILE','IF','ELSE','FLOAT')

    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_COMMA = r','
    t_SEMICOLON = r';'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_FLOORDIV = r'//'
    t_DIVIDE = r'/'
    t_IS = r'=='
    t_ISNOT = r'<>'
    t_GREATERTHENEQUAL = r'>='
    t_LESSTHENEQUAL = r'<='
    t_GREATERTHEN = r'>'
    t_EXPONENTIAL = r'\*\*'
    t_MOD = r'%'
    t_LESSTHEN = r'<'
    t_ASSIGNVALUE = r'='
    lcurlybracket = r'{'
    rcurlybracket = r'}'
    t_ignore = ' \t'
    number = r'\d+'
    string = r'"[^"\\\r\n]*(?:\\.[^"\\\r\n]*)*"'
    newline = r'\n+'
    id = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if type(t) == None:
            return None

        val = self.reserved.get(t.value, '')
        t.type = str(val)
        if t.type == '':
            t.type = 'ID'
        if t.type == 'ID' and isinstance(t.type,str):
            t.value = Variable_Node(t.value)
        return t

    def t_FLOAT(self,t):
        r'((\.\d+)|(\d+\.\d+))'
        if type(t) == None:
            return None
        try :
            t.value = Float_Node((t.value))
        except ValueError:
            print("Semantics Error")
            t.value = 0
        return t

    def t_NUMBER(self, t):
        r'\d+'
        if type(t) == None:
            return None
        try:
            t.value = Number_Node(t.value)
        except ValueError:
            print("Semantics Error")
            t.value = 0
        return t

    def t_STRING(self, t):
        r'"[^"\\\r\n]*(?:\\.[^"\\\r\n]*)*"'
        if type(t) == None:
            return None
        s = str(t.value[1:len(str(t.value)) - 1])
        t.value = String_Node(s)
        return t

    def t_LCURLYBRACKET(self, t):
        r'{'
        if type(t) == None:
            return None
        return t


    def t_RCURLYBRACKET(self, t):
        r'}'
        if type(t) == None:
            return None
        return t

    #handle error case
    def t_error(self, t):
        print("SEMANTICS ERROR")
        t.lexer.skip(1)

    # Parsing rules ###########################################################

    # left value is associativity
    # right value is the operand
    precedence = (
        ('left', 'AND'),
        ('left', 'OR'),
        ('left', 'IS', 'ISNOT'),
        ('right', 'NOT'),
        ('left', 'TIMES', 'DIVIDE'),
        ('left', 'EXPONENTIAL')
    )

    def p_program(self, p):
        """program : LCURLYBRACKET function RCURLYBRACKET
        """
        p[0] = Block_Node(p[2], True)

    def p_function(self, p):
        """function : code
               | code function
               | conditional
               | conditional function"""

        if len(p) == 3:
            val = [p[1]] + p[2]
            p[0] = Statement_List(val)
        elif len(p) == 2:
            p[0] = Statement_List([p[1]])
        else:
            p[0] = None


    def p_conditional_while(self, p):
        """conditional : WHILE LPAREN operation RPAREN block"""
        if len(p) == 5:
            if type(p[0]) == None:
                p[0] = None
        p[0] = While_Node(p[3], p[5])

    def p_conditional_if(self, p):
        """ conditional : IF LPAREN operation RPAREN block
                   | IF LPAREN operation RPAREN block ELSE block
                   | IF RPAREN operation LPAREN block ELSE block
        """

        if len(p) == 8:
            if p[2] == ')' or p[4] == '(':
                p[0] = None
                return

            p[0] = If_Node(p[3], p[5], p[7])

        elif len(p) == 6:
            if len(p) == 5:
                if type(p[0]) == None:
                    p[0] = None
            p[0] = If_Node(p[3], p[5], None)

    def p_code(self, p):
        """code : statements
                | statements code
        """

        try:

            if len(p) == 2:
                p[0] = Statement_List([p[1]])
            elif len(p) == 3:
                val = [p[1]]+ p[2]
                p[0] = Statement_List(val)
        except:
            print("Syntax Error")

    def p_code_blocks(self,p):
        """ code : blocks
                 | blocks code"""
        try:
            if len(p) == 2:
                p[0] = Statement_List([p[1]])
            elif len(p) == 3:
                val = [p[1]] + p[2]
                p[0] = Statement_List(val)
        except:
            print("Syntax Error")

    def p_blocks(self, p):
        """blocks : block blocks
                  | block"""
        val = [p[1]] + p[2]
        if len(p) == 3:
            p[0] = Statement_List(val)
        elif len(p) == 2:
            p[0] = Statement_List([p[1]])

    def p_block(self, p):
        """block : LCURLYBRACKET function RCURLYBRACKET
                 | LCURLYBRACKET statements RCURLYBRACKET"""
        if len(p) == 4 and p[1] == '{' and p[3] == '}':
            p[0] = Block_Node(p[2],False)

    def p_statements(self, p):
        """statements : statement SEMICOLON statements
                      | statement SEMICOLON

        """
        if len(p) == 4:
            p[0] = Statement_List([p[1]] + p[3])
        elif len(p) == 3:
            p[0] = Statement_List([p[1]])


    def p_statement(self, p):
        """statement : operation
                     | list
                     | ID ASSIGNVALUE operation
                     | ID ASSIGNVALUE list
                     | list_id_string ASSIGNVALUE operation
        """
        if len(p) == 2:
            p[0] = Statement_Node(p[1], False, False, None, None)
        elif isinstance(p[2],str) and p[2] == '=':
            p[0] = Statement_Node(p[1], False, True, p[3], None)
        elif isinstance(p[1],str) and p[1] == 'print':
            if type(p[3]) != None:
                p[0] = Statement_Node(p[3], True, False, None, None)

    def p_statement_print(self,p):
        """statement : PRINT LPAREN operation RPAREN
                     | PRINT LPAREN list RPAREN"""
        if isinstance(p[2], str) and p[2] == '=':
            p[0] = Statement_Node(p[1], False, True, p[3], None)
        elif isinstance(p[1], str) and p[1] == 'print':
            if type(p[3]) != None:
                p[0] = Statement_Node(p[3], True, False, None, None)

    def p_list_id_string(self, p):
        """list_id_string : list LBRACKET expression RBRACKET
                  | list LBRACKET list_id_string RBRACKET
                  | list LBRACKET expression RBRACKET LBRACKET expression RBRACKET
                  | LBRACKET list RBRACKET LBRACKET expression RBRACKET
                  | LBRACKET expression RBRACKET LBRACKET expression RBRACKET
                  | LBRACKET list RBRACKET LBRACKET ID RBRACKET
                  | LBRACKET expression RBRACKET LBRACKET ID RBRACKET
                  """
        try:
            if len(p) == 5:
                p[0] = Statement_Node(p[1], False, False, None, p[3])
            elif len(p) == 8:
                p[0] = Statement_Node(p[1], False, False, None, [p[3], p[6]])
        except IndexError:
            print("SEMANTIC ERROR")


    def p_list_id_string_ID(self,p):
        """ list_id_string : ID LBRACKET list_id_string RBRACKET
                    |  ID LBRACKET expression RBRACKET
                    | ID LBRACKET expression RBRACKET LBRACKET expression RBRACKET """
        try:
            if len(p) == 5:
                p[0] = Statement_Node(p[1], False, False, None, p[3])
            elif len(p) == 8:
                p[0] = Statement_Node(p[1], False, False, None, [p[3], p[6]])
        except IndexError:
            print("SEMANTIC ERROR")

    def p_list_id_string_string(self,p):
        """ list_id_string : STRING LBRACKET list_id_string RBRACKET
                  | STRING LBRACKET expression RBRACKET
                  | STRING LBRACKET expression RBRACKET LBRACKET expression RBRACKET
        """
        try:
            if len(p) == 5:
                p[0] = Statement_Node(p[1], False, False, None, p[3])
            elif len(p) == 8:
                p[0] = Statement_Node(p[1], False, False, None, [p[3], p[6]])
        except IndexError:
            print("SEMANTIC ERROR")

    def p_list(self, p):
        """list : LBRACKET items RBRACKET"""
        p[0] = List_Node(p[2])

    def p_items(self, p):
        """items : operation COMMA items
                 | operation
                 | list
                 | list COMMA items
                 """
        if len(p) == 4:
            p[0] = [p[1]] + p[3]
        elif len(p) == 2:
            p[0] = [p[1]]

    def p_operations_equal(self, p):
        """operation : equal
        """
        p[0] = p[1]

    def p_eq_condition(self, p):
        """equal : condition"""
        p[0] = p[1]

    def p_cond_expression(self, p):
        """condition : expression"""
        p[0] = p[1]

    def p_term_factor(self, p):
        """term : factor"""
        p[0] = p[1]

    def p_expr_term(self, p):
        """expression : term"""
        p[0] = p[1]

    def p_not(self, p):
        """equal : NOT equal"""
        if p[1] == 'not':
            p[0] = not p[2]

    def p_binops_operation(self, p):
        """
      operation : expression IN list
                | operation OR equal
                | operation AND equal
        """
        p[0] = BinaryOperations(p[1], p[3], p[2])

    def p_binop_expression(self,p):
        """
         expression : expression PLUS term
                | expression MINUS term
        """
        p[0] = BinaryOperations(p[1], p[3], p[2])

    def p_binops_term(self,p):
        """     term : term TIMES factor
                | term DIVIDE factor
                | term FLOORDIV factor
                | term MOD factor
              | term EXPONENTIAL factor
                """
        p[0]= BinaryOperations(p[1],p[3],p[2])

    def p_binops_condition(self,p):
        """      condition : condition GREATERTHEN expression
                | condition GREATERTHENEQUAL expression
                | condition LESSTHENEQUAL expression
                | condition LESSTHEN expression
        """

        p[0]= BinaryOperations(p[1],p[3],p[2])


    def p_binops_equal(self,p):
        """  equal   : equal IS condition
                     | equal ISNOT condition"""
        p[0]= BinaryOperations(p[1],p[3],p[2])


    def p_factor_id(self, p):
        """factor : ID """
        p[0] = p[1]
    def p_factor_number(self, p):
        """factor : NUMBER"""
        p[0] = p[1]
    def p_factor_float(self,p):
        """factor : FLOAT """
        p[0] = p[1]
    def p_factor_string(self, p):
        """factor : STRING"""
        p[0] = str(p[1])
    def p_factor_expression(self, p):
        """factor : LPAREN operation RPAREN"""
        p[0] = p[2]

    def p_factor_list_id_string(self, p):
        """factor : list_id_string"""
        p[0] = p[1]

    def p_error(self, p):
        tok = ''
        while True:
            tok = self.parser.token()
            if tok == None or tok.value == ';' or tok.value == '\n' or not tok:
                break
        self.parser.errok()
        if not tok:
            exit(0)


class parseStack(list):

    def push(self, item):
        self.append(item)

    def search_for_elem(self, variable):

        reverse = reversed(self)
        for i in reverse:
            if variable.name in i:
                return i[variable.name]
        return None

    def set_elem(self, variable, value):
        v_or_s = 0
        if type(variable) == Variable_Node:
           for current_scope in reversed(self):
               if variable.name not in current_scope:
                   continue
               else:
                   current_scope[variable.name]= value
                   return
           v_or_s = 1

        elif type(variable) == Statement_Node:
            list = []
            list.append(variable.access_value )
            list.append(variable.statement)

            while issubclass(type(list[0]), Node):
                list[0] = list[0].evaluate()


            for scope in reversed(self):
                if list[1].name not in scope:
                    continue
                else:
                    scope[list[1].name][list[0]] = value
                    return
            v_or_s = 2

        if v_or_s == 1:
            self[-1][variable.name] = value
        elif v_or_s == 2:
            self[-1][list[1].name] = value
            
argument = sys.argv
read = open(argument[1],"r")
hw5 = grammar()
grammar_stack = parseStack()
hw5.compile_(read)




