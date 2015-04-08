from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for, flash)
from splash import *
from main import app
from alchemyapi import AlchemyAPI
import json
import pdb

splash = Blueprint('splash', __name__, template_folder="templates")

alchemyapi = AlchemyAPI()

@splash.route('/')
def index():
    return render_template('home.html')

@splash.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text-analysis']
    taxonomy = alchemyapi.taxonomy('text', text)
    if not taxonomy['status'] == 'OK':
        return jsonify({'success': 'false'})

    concepts = alchemyapi.concepts('text', text)
    if not concepts['status'] == 'OK':
        return jsonify({'success': 'false'})

    return jsonify({'taxonomy': taxonomy, 'concepts': concepts})
