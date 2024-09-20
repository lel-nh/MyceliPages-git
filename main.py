from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

files = []

noms_fichiers = os.listdir('templates')

# Afficher les noms de fichiers
for nom in noms_fichiers:
    files.append(nom)
    files.append("<br>")

@app.route('/')
def index():
    fichiers = os.listdir("templates")
    return render_template('main.html', fichiers=files)

@app.route('/page1.html')
def page1():
    fichiers = os.listdir("templates")
    return render_template('page1.html', fichiers=files)

@app.route('/main.html')
def main():
    fichiers = os.listdir("templates")
    return render_template('main.html', fichiers=files)


if __name__ == "__main.py__":
    app.debug(Debug = True)
