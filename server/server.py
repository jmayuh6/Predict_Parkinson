from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
import json
import base64
from predict import predict
import warnings
import soundfile as sf
import os

warnings.simplefilter("ignore")

# Iniciacion de la aplicacion
app = Flask(__name__)
cors = CORS(app, resources = {r"/api/*": {"origins": "*"}})

@app.route("/api/audio_update", methods = ['POST'])
def audio_update():
    ## Request de datos enviados por el Vue
    dataPaciente = request.data
    ## Carga del JSON
    jsonPaciente = json.loads(dataPaciente)
    #print("Edad: ",jsonPaciente['edad'])
    #print("Genero: ",jsonPaciente['genero'])
    #print(jsonPaciente['audio'][:5])
    ## Exportar a archivo .wav
    decodedData = base64.b64decode(jsonPaciente['audio'])
    filename = jsonPaciente['idaudio'] + '.webm'
    wav_file = open(filename, "wb")
    wav_file.write(decodedData) 
    wav_file.close()
    #data, samplerate = sf.read(filename)
    path="D:/9no ciclo/ST415U - Inteligencia Artificial Avanzada/Trabajo/voice-recorder-parkinson/server/"
    command = 'ffmpeg.exe -i "' + path + filename + '" "' + path + jsonPaciente['idaudio']+'.wav"'
    #print(command)
    os.system(command)
    '''
    with wave.open(filename,'wb') as wav:
        wav.setparams((2, 2, 5000, 0, 'NONE', 'NONE'))
        wav.writeframes(decodedData)
        wav.close()
    '''
    print ('Se importó correctamente el audio desde ffmpeg')
    prediccion=predict(jsonPaciente['idaudio'],jsonPaciente['edad'],jsonPaciente['genero'])[0]
    if(prediccion==1):
        return jsonify({'result':'El paciente será propenso a contraer Parkinson'})
    else:
        return jsonify({'result':'El paciente no será propenso a contraer Parkinson'})

if __name__ == "__main__":
    app.run(debug=True)