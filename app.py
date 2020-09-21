from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

carros = [
    {
        'modelo': 'Fusca',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1982',
        'preco': '15.000'
    },

    {
        'modelo': 'Monza',
        'motor': '1.6',
        'marca': 'Chevrolet',
        'ano': '1982',
        'preco': '10.000'
    },

    {
        'modelo': 'Mustang GT',
        'motor': '390 V8',
        'marca': 'Ford',
        'ano': '1966',
        'preco': '150.000'
    },
    {
        'modelo': 'Chevette',
        'motor': '1.6',
        'marca': 'Chevrolet',
        'ano': '1987',
        'preco': '10.000'

    },

    {
        'modelo': 'Gol',
        'motor': '1.8',
        'marca': 'Volkswagen',
        'ano': '1988',
        'preco': '25.000'
    },
    {
        'modelo': 'Uno Mille',
        'motor': '1.5',
        'marca': 'Fiat',
        'ano': '1984',
        'preco': '20.000'
    },
    {
        'modelo': 'Passat',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1982',
        'preco': '10.000'
    },

    {
        'modelo': 'Opala',
        'motor': '2.5',
        'marca': 'Chevrolet',
        'ano': '1981',
        'preco': '15.000'
    },

    {
        'modelo': 'Maverick',
        'motor': '4.9 V8',
        'marca': 'Ford',
        'ano': '1976',
        'preco': '60.000'
    },
    {
        'modelo': 'Kadett',
        'motor': '1.8',
        'marca': 'Chevrolet',
        'ano': '1989',
        'preco': '15.000'
    },

    {
        'modelo': 'Kombi',
        'motor': '1.4',
        'marca': 'Volkswagen',
        'ano': ' 1957',
        'preco': '25.000'
    },


    {
        'modelo': 'Santana',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1984',
        'preco': '10.000'
    },
    
]

class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50))
    motor = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    ano = db.Column(db.String(50))
    preco = db.Column(db.String(50))

    def __repr__(self):
            return '<Cars %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        pass
    else:
        
        return render_template('index.html', carros = carros)

if __name__ == "__main__":
    app.run(debug=True)