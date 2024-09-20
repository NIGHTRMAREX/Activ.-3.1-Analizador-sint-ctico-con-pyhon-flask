import ply.yacc as yacc
from lexer import tokens

# Definir reglas gramaticales
def p_for_loop(p):
    '''for_loop : FOR WORD WORD WORD'''
    p[0] = ('for_loop', p[2], p[3], p[4])

def p_expression_word(p):
    '''expression : WORD'''
    p[0] = ('word', p[1])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('number', p[1])

def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para analizar la estructura sintáctica del código
def parse_code(code):
    return parser.parse(code)
