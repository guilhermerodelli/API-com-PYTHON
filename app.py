from flask import Flask, jsonify, request

app = Flask(__name__)

emprestimo = [
    {
        'id': 1,
        'tipo': 'Empréstimo pessoal'
    },
    {
        'id': 2,
        'tipo': 'Empréstimo com garantia'
    },
    {
        'id': 3,
        'tipo': 'Empréstimo consignado'
    },
]

@app.route('/emprestimo', methods=['GET'])
def verificar_emprestimos1():
    data = request.args
    emprestimos_disponiveis = verificar_emprestimos(data)
    return jsonify(emprestimos_disponiveis)


@app.route('/emprestimo', methods=['POST'])
def verificar_emprestimos():
    print(request.get_json())
    data = request.get_json()
    emprestimos_disponiveis = verificar_emprestimos(data)
    return jsonify(emprestimos_disponiveis)


def verificar_emprestimos(cliente):
    emprestimos_disponiveis = []
    income=int(cliente['income'])
    age=int(cliente['age'])

    if income <= 3000:
        emprestimos_disponiveis.append({'tipo': 'pessoal', 'taxas': 4})
    elif 3000 < income < 5000 and cliente['location'] != 'SP':
        emprestimos_disponiveis.append({'tipo': 'pessoal', 'taxas': 4})

    if income > 3000:
        if age < 30:
            emprestimos_disponiveis.append({'tipo': 'garantido', 'taxas': 3})
        elif cliente['location'] == 'SP':
            emprestimos_disponiveis.append({'tipo': 'garantido', 'taxas': 3})

    if income >= 5000 or (income > 3000 and cliente['location'] == 'SP' and age < 30):
        emprestimos_disponiveis.append({'tipo': 'consignado', 'taxas': 2})

    return emprestimos_disponiveis

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)