from flask import Flask, render_template, request
from lexer import tokenize  # Asegúrate de tener una función tokenize
from parser import parse_code

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    tokens = []
    error_message = None

    if request.method == 'POST':
        text = request.form['text']
        lines = text.splitlines()

        # Tokenizar cada línea y asignar el número de línea correspondiente
        for line_number, line in enumerate(lines, start=1):
            line_tokens = tokenize(line)  # Tokenizar la línea actual
            for token in line_tokens:
                token.line = line_number  # Asignar el número de línea a cada token
            tokens.extend(line_tokens)  # Agregar tokens a la lista total

        # Realizar el análisis sintáctico y capturar mensajes de error
        error_message = parse_code(text)

    return render_template('index.html', text=text, tokens=tokens, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
