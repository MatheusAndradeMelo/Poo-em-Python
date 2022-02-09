from flask import Flask, render_template
# route -> nome do site/
# função -> o que você quer mostrar
# template -> arquivo html da pagina
# Servidor do heroku
#criar arquivo procfiletxt
#instalar o gunicorn
#pip freeze > requirements.txt no terminal
#heroku login no terminal
#seguir passo a passo do heroku
# https://sitepythonvideoyoutube.herokuapp.com/
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)
#coloca no ar
if __name__ == '__main__':
    app.run(debug = True)
