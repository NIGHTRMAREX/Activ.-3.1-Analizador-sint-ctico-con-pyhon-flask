from flask import Flask, request, render_template
from lexer import lexico
from parser import parse_code

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = None
    text = None
    
    if request.method == 'POST':
        text = request.form['text']
        tokens = lexico(text)  # Realizar análisis léxico
    
    return render_template('index.html', tokens=tokens, text=text)

if __name__ == '__main__':
    app.run(debug=True)
