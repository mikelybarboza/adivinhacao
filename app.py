from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def jogo_adivinhacao():
    if request.method == 'POST':
       
        palpite = int(request.form['palpite'])
        numero_secreto = int(request.form['numero_secreto'])
        tentativas = int(request.form['tentativas'])
        tentativas_anteriores = request.form['tentativas_anteriores']
        
        
        tentativas_anteriores = tentativas_anteriores.split(',') if tentativas_anteriores else []
        tentativas_anteriores.append(str(palpite))  
        
        if palpite < numero_secreto:
            dica = "O número secreto é maior!"
        elif palpite > numero_secreto:
            dica = "O número secreto é menor!"
        else:
            dica = f"Parabéns! Você acertou o número em {tentativas} tentativas."
            numero_secreto = random.randint(1, 100)  
            tentativas = 0  
            tentativas_anteriores = []  

        
        return render_template(
            'index.html',
            dica=dica,
            numero_secreto=numero_secreto,
            tentativas=tentativas,
            palpite=palpite,
            tentativas_anteriores=",".join(tentativas_anteriores)  
        )

    
    numero_secreto = random.randint(1, 100)  
    tentativas = 0  
    tentativas_anteriores = ""  
    return render_template(
        'index.html',
        dica='',
        numero_secreto=numero_secreto,
        tentativas=tentativas,
        palpite='',
        tentativas_anteriores=tentativas_anteriores
    )

if __name__ == "__main__":
    app.run(debug=True)