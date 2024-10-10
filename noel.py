from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

enfants = []
livraisons = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajouter_enfant', methods=['GET', 'POST'])
def ajouter_enfant():
    if request.method == 'POST':
        nom = request.form['nom']
        age = request.form['age']
        adresse = request.form['adresse']
        souhaits = request.form['souhaits']
        enfants.append({'nom': nom, 'age': age, 'adresse': adresse, 'souhaits': souhaits})
        return redirect(url_for('index'))
    return render_template('ajouter_enfant.html')

@app.route('/planifier_livraison', methods=['GET', 'POST'])
def planifier_livraison():
    if request.method == 'POST':
        ville = request.form['ville']
        date = request.form['date']
        enfants_par_ville = [e for e in enfants if e['adresse'] == ville]
        livraisons.append({'ville': ville, 'date': date, 'enfants': enfants_par_ville})
        return redirect(url_for('index'))
    return render_template('planifier_livraison.html')

@app.route('/details_livraison')
def details_livraison():
    return render_template('details_livraison.html', livraisons=livraisons)

if __name__ == '__main__':
    app.run(debug=True)
