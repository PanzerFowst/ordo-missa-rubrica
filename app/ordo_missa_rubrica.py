# /app/ordo_missa_rubrica.py

import os
from typing import Type

from flask import Flask, render_template, request, jsonify

from ordo_missa.ordo_missa_abc import OrdoMissaABC
from ordo_missa.parishes.epiphany.mass_text import Epiphany
from ordo_missa.parishes.st_agnes.mass_text import StAgnes

# Set environment variables (for running as a Python file instead of a VS Code debugging process):
# os.environ['FLASK_APP'] = 'app.py'
# os.environ['FLASK_ENV'] = 'development'  # For production environment, use 'production' instead of 'development'.


# Mapping of parish names to their classes:
parish_classes: dict[str, Type[OrdoMissaABC]] = {
    "st_agnes": StAgnes,
    "epiphany": Epiphany,
}


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    parish: str = request.form.get('parish', '')
    num_deacons: int = int(request.form.get('num_deacons', 0))
    num_servers: int = int(request.form.get('num_servers', 2))

    parish_class = parish_classes.get(parish)

    if parish_class is None:
        return jsonify({'error': 'Parish not found'}), 404

    try:
        parish_instance = parish_class(num_deacons, num_servers)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    # Generate the text for the Mass:
    mass_text = {
        "introductory_rites": parish_instance.introductory_rites(),
        "liturgy_of_the_word": parish_instance.liturgy_of_the_word(),
        "liturgy_of_the_eucharist": parish_instance.liturgy_of_the_eucharist(),
        "communion_rite": parish_instance.communion_rite(),
        "concluding_rites": parish_instance.concluding_rites()
    }

    return jsonify(mass_text)


if __name__ == '__main__':
    app.run(debug=True)
