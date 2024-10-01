import ply.lex as lex

# Lista de tokens
tokens = (
    'INT',
    'MAIN',
    'ID',  # Identificadores como x
    'LPAREN',  # Paréntesis izquierdo
    'RPAREN',  # Paréntesis derecho
    'LBRACE',  # Llave izquierda
    'RBRACE',  # Llave derecha
    'SEMICOLON'  # Punto y coma
)

# Reglas para los tokens
def t_INT(t):
    r'\bint\b'
    t.type = 'INT'
    t.description = 'Palabra Reservada'
    return t

def t_MAIN(t):
    r'\bmain\b'
    t.type = 'MAIN'
    t.description = 'Reservada main'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    t.description = 'Identificador'
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
        tokens.append(tok)
    return tokens
