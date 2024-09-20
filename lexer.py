import ply.lex as lex

# Lista de tokens
tokens = (
    'FOR',
    'WORD',  # Token para otras palabras
    'NUMBER',  # Para capturar números
)

# Reglas de expresiones regulares para los tokens
def t_FOR(t):
    r'\b[Ff][Oo][Rr]\b'  # Detecta la palabra 'for' en cualquier combinación de mayúsculas y minúsculas
    return t

# Token genérico para capturar palabras
def t_WORD(t):
    r'[a-zA-Z]+'  # Captura cualquier secuencia de letras
    return t

# Token para capturar números
def t_NUMBER(t):
    r'\d+'  # Captura secuencias de dígitos
    t.value = int(t.value)  # Convertir a número entero
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Manejar errores
def t_error(t):
    if t:
        print(f"Caracter ilegal: {t.value[0]}")
        t.lexer.skip(1)  # Saltar el carácter ilegal
    else:
        print("Error: Token no válido o inesperado.")
        
# Construir el analizador léxico
lexer = lex.lex()

# Función para tokenizar el texto
def lexico(text):
    lexer.input(text)
    tokens = []
    while True:
        tok = lexer.token()
        if tok:  # Solo añadir si el token no es None
            tokens.append(tok)
        else:
            break
    return tokens
