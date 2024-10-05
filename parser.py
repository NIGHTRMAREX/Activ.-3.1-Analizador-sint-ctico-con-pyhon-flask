import ply.yacc as yacc
from lexer import tokens  # Importar los tokens definidos en el lexer

# Variable global para almacenar el mensaje de error
syntax_error_message = []

# Definir las reglas gramaticales
def p_program(p):
    '''program : PROGRAMA ID LPAREN RPAREN LBRACE declarations instructions RBRACE END SEMICOLON'''
    p[0] = ('program', p[2], p[6], p[7])

# Regla para permitir múltiples declaraciones separadas por comas
def p_declarations(p):
    '''declarations : declaration SEMICOLON
                    | declaration SEMICOLON declarations'''
    if len(p) == 3:
        p[0] = [p[1]]  # Una declaración simple
    else:
        p[0] = [p[1]] + p[3]  # Varias declaraciones

# Aquí ajustamos para permitir múltiples variables con comas
def p_declaration(p):
    '''declaration : INT var_list'''  # Declaración de múltiples variables separadas por comas
    p[0] = ('declaration', p[2])

# Nueva regla para una lista de variables separadas por comas
def p_var_list(p):
    '''var_list : ID
                | ID COMMA var_list'''
    if len(p) == 2:
        p[0] = [p[1]]  # Solo una variable
    else:
        p[0] = [p[1]] + p[3]  # Múltiples variables

# Regla para las instrucciones
def p_instructions(p):
    '''instructions : instruction SEMICOLON
                    | instruction SEMICOLON instructions'''
    if len(p) == 3:
        p[0] = [p[1]]  # Una instrucción
    else:
        p[0] = [p[1]] + p[3]  # Varias instrucciones

def p_instruction(p):
    '''instruction : READ ID
                   | PRINT LPAREN STRING RPAREN
                   | assignment'''
    if len(p) == 3:  # Para read
        p[0] = ('instruction', p[1], p[2])
    elif len(p) == 5:  # Para printf con paréntesis
        p[0] = ('print', p[3])  # Instrucción print con cadena
    else:  # Para asignaciones
        p[0] = p[1]  # Simplemente pasa la instrucción de asignación

def p_assignment(p):
    '''assignment : ID ASSIGN expression'''
    p[0] = ('assignment', p[1], p[3])  # Variable = expresión

def p_expression(p):
    '''expression : ID PLUS ID
                  | NUMBER'''
    if len(p) == 4:
        p[0] = ('addition', p[1], p[3])  # a + b
    else:
        p[0] = ('number', p[1])  # número

# Regla de manejo de errores
def p_error(p):
    global syntax_error_message  # Usar la variable global para almacenar errores
    if p:
        syntax_error_message.append(f"Error de sintaxis cerca de '{p.value}'")
    else:
        syntax_error_message.append("Error de sintaxis: fin de entrada inesperado")

# Construir el parser
parser = yacc.yacc()

# Función para analizar la estructura sintáctica del código
def parse_code(code):
    global syntax_error_message
    syntax_error_message = []  # Reiniciar el mensaje de error antes de cada análisis
    parser.parse(code)
    return syntax_error_message  # Retornar el mensaje de error
