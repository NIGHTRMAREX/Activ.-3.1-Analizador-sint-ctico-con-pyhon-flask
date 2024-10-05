import ply.lex as lex

# Lista de tokens
tokens = (
    'INT',
    'MAIN',
    'ID',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'READ',
    'PRINT',
    'END',
    'PROGRAMA',
    'COMMA',
    'STRING',
    'NUMBER',
    'ASSIGN',  # Token para el símbolo '='
    'PLUS'      # Token para el símbolo '+'
)

# Reglas para los tokens
def t_INT(t):
    r'\bint\b'
    t.type = 'INT'
    t.description = 'Palabra Reservada'
    return t

def t_PROGRAMA(t):
    r'\bprograma\b'
    t.type = 'PROGRAMA'
    t.description = 'Palabra Reservada'
    return t

def t_READ(t):
    r'\bread\b'
    t.type = 'READ'
    t.description = 'Palabra clave read'
    return t

def t_PRINT(t):
    r'\bprintf\b'
    t.type = 'PRINT'
    t.description = 'Palabra Reservada'
    return t

def t_END(t):
    r'\bend\b'
    t.type = 'END'
    t.description = 'Palabra Reservada'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    t.description = 'Identificador'
    return t

def t_NUMBER(t):
    r'\d+'  # Para reconocer números
    t.type = 'NUMBER'
    t.description = 'Número'
    return t

def t_LPAREN(t):
    r'\('
    t.type = 'LPAREN'
    t.description = 'Paréntesis de apertura'
    return t

def t_RPAREN(t):
    r'\)'
    t.type = 'RPAREN'
    t.description = 'Paréntesis de cierre'
    return t

def t_LBRACE(t):
    r'\{'
    t.type = 'LBRACE'
    t.description = 'Llave de apertura'
    return t

def t_RBRACE(t):
    r'\}'
    t.type = 'RBRACE'
    t.description = 'Llave de cierre'
    return t

def t_SEMICOLON(t):
    r';'
    t.type = 'SEMICOLON'
    t.description = 'Punto y coma'
    return t

def t_COMMA(t):
    r','
    t.type = 'COMMA'
    t.description = 'Coma'
    return t

def t_STRING(t):
    r'"([^\\"]|\\.)*"'  # Para reconocer cadenas entre comillas
    t.description = 'Cadena de texto'
    return t

def t_ASSIGN(t):
    r'='  # Para el símbolo '='
    t.type = 'ASSIGN'
    t.description = 'Asignación'
    return t

def t_PLUS(t):
    r'\+'  # Para el símbolo '+'
    t.type = 'PLUS'
    t.description = 'Suma'
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para tokenizar el texto
def tokenize(text):
    lexer.input(text)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        # Determinación de tipos de tokens
        tok.is_reserved = tok.type in ['INT', 'READ', 'PRINT', 'END', 'PROGRAMA']
        tok.is_identifier = tok.type == 'ID'
        tok.is_string = tok.type == 'STRING'
        tok.is_number = tok.type == 'NUMBER'
        tok.is_symbol = tok.type in ['LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'ASSIGN', 'PLUS']
        tokens.append(tok)
    return tokens
