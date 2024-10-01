import ply.yacc as yacc
from lexer import tokens  # Importar los tokens definidos en el lexer

# Variable global para almacenar el mensaje de error
syntax_error_message = []

# Definir las reglas gramaticales
def p_program(p):
    '''program : INT MAIN LPAREN RPAREN LBRACE declarations RBRACE'''
    p[0] = ('program', p[6])

def p_declarations(p):
    '''declarations : declaration SEMICOLON
                    | declaration SEMICOLON declarations'''
    if len(p) == 3:
        p[0] = [p[1]]  # Una declaración simple
    else:
        p[0] = [p[1]] + p[3]  # Varias declaraciones

def p_declaration(p):
    '''declaration : INT ID'''
    p[0] = ('declaration', p[2])

# Regla de manejo de errores
def p_error(p):
    global syntax_error_message  # Usar la variable global para almacenar errores
    if p:
        if p.type == 'INT':
            syntax_error_message.append(f"Error de sintaxis: falta '{{' ")
        elif p.type == 'MAIN':
            syntax_error_message.append(f"Error de sintaxis: se encontró '{p.value}' donde no se esperaba.")
        elif p.type == 'LPAREN':
            syntax_error_message.append("Error de sintaxis: falta ''")
        elif p.type == 'RPAREN':
            syntax_error_message.append("Error de sintaxis: falta '('")
        elif p.type == 'LBRACE':
            syntax_error_message.append("Error de sintaxis: falta ')'")
        elif p.type == 'RBRACE':
            syntax_error_message.append("Error de sintaxis: falta ';'")
        elif p.type == 'SEMICOLON':
            syntax_error_message.append("Error de sintaxis: falta 'un identificador'")
        else:
            syntax_error_message.append(f"Error de sintaxis cerca de '{p.value}'")
    else:
        syntax_error_message.append("Error de sintaxis: falta '}")

# Construir el parser
parser = yacc.yacc()

# Función para analizar la estructura sintáctica del código
def parse_code(code):
    global syntax_error_message
    syntax_error_message = []  # Reiniciar el mensaje de error antes de cada análisis
    parser.parse(code)
    return syntax_error_message  # Retornar el mensaje de error