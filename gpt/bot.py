from flask import Flask, jsonify
import gdown
import schedule
import time
import subprocess
app = Flask(__name__)

@app.route('/')
def run_colab():
    gdown.download('https://drive.google.com/drive/folders/1Nr72-Pfu6Nu4XdJZ4Kfrfz0dvq6jgBwU', 'FinRL_Ensemble_StockTrading_ICAIF_2020.ipynb', quiet=False, fuzzy=True)
    return jsonify(message='colab notebook ran successfully')

def schedule_ai_bot():
    
    schedule.every().day.at("00:00").do(run_colab)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # schedule_ai_bot()
    app.run()
    

# https://colab.research.google.com/drive/1gJyqi9Kc8C4092t91NHIb3XGqpsomcrd?usp=share_link

