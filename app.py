from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)

# initialise un objet de la classe Sqalchemy 
app.config['SECRET_KEY'] = "cle secrete"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passer@localhost:5432/postgres' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

# creation de la table 
class Etudiants(db.Model): 
    id  = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String , nullable=True)
    mail = db.Column(db.String, nullable=True)

    def __repr__(self) -> str:
        return f"<{self.nom}>"


@app.route("/")
def index(): 
    etudiant = Etudiants.query.all()
    return render_template('index.html', etudiant=etudiant)

@app.route('/add', methods=["POST"])
def add(): 
    nom = request.form.get('nom')
    mail = request.form.get('mail')
    pers = Etudiants(nom=nom, mail=mail)
    db.session.add(pers)
    db.session.commit()
    return redirect(url_for('index'))


with app.app_context(): 
    db.create_all()

if __name__ == "__main__": 
    app.run(debug=True, port=5003)


