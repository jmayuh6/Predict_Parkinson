<template>
  <div class="audio-page mb-5">
    <MediaRecorderHeader />

    <div class="shadow-sm p-5 bg-white rounded">
      <label for="name"><b>ID Audio</b></label>
      <input type="text" class="form-control" id="idaudio">
      <br>
      <label for="formControlRange"><b>Gender</b></label><br />
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="gender" id="gender-male" value="male">
        <label class="form-check-label" for="gender">Masculino</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="gender" id="gender-female" value="female">
        <label class="form-check-label" for="gender">Femenino</label>
      </div>
      <br>
      <br>
      <label for="name"><b>Edad</b></label>
      <input type="text" class="form-control" id="edad">
      <br>
      <b-button variant="primary" class="mr-2" @click="start" :disabled="startDisabled">Grabar</b-button>
      <b-button variant="outline-primary" class="mr-2" @click="pause" :disabled="stopDisabled">Pausar</b-button>
      <b-button variant="outline-success" class="mr-2" @click="resume" :disabled="startDisabled">Reanudar</b-button>
      <b-button variant="secondary" @click="stop" :disabled="stopDisabled">Parar y Guardar</b-button>

      <hr>

      <div v-if="hasAudios">
        <ul class="list-unstyled audio-list">
          <li v-for="(item, idx) in audioList" :key="idx" class="audio-item mb-3">
            <div class="d-flex justify-content-between">
              <audio :controls="true" :loop="false" :src="item.src" class="mr-2 w-100"></audio>
              <div class="d-flex align-items-center">
                <b-button variant="danger" size="sm" @click="removeItem(idx)"> Eliminar </b-button>
              </div>
            </div>
          </li>
        </ul>
        <br>
        <label for="name"><b>Diagnostico: </b></label>
        <br>
        <h6 class="label" id="txtLabel">Cargando...</h6>
      </div>
    </div>
  </div>
</template>

<script>
import MediaRecorderHeader from '@/components/HeaderMediaRecorderAPI'

export default {
  name: 'Audio',
  components: { MediaRecorderHeader },
  data () {
    return {
      supported: undefined,
      mediaRecorder: undefined,
      chunks: [],
      audioList: [],
      isRecording: false
    }
  },
  computed: {
    startDisabled () {
      return this.isRecording === true
    },
    stopDisabled () {
      return this.isRecording === false
    },
    hasAudios () {
      return this.audioList.length > 0
    }
  },
  methods: {
    start () {
      console.log('State: ', this.mediaRecorder.state)
      this.mediaRecorder.start()
      this.isRecording = true
    },
    stop () {
      console.log('State: ', this.mediaRecorder.state)
      this.mediaRecorder.stop()
      this.isRecording = false
    },
    pause () {
      console.log('State: ', this.mediaRecorder.state)
      this.mediaRecorder.pause()
      this.isRecording = false
    },
    resume () {
      console.log('State: ', this.mediaRecorder.state)
      this.mediaRecorder.resume()
      this.isRecording = true
    },
    removeItem (idx) {
      this.audioList.splice(idx, 1)
    }
  },
  created () {
    // Comprobar si el navegador soporta esta 'feature'
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      this.supported = true

      // Request permission for audio only
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then((stream) => {
          // La interfaz MediaStream representa una secuencia de contenido multimedia.
          // Una transmisión consta de varias pistas, como pistas de video o audio.
          console.log(stream)

          // Crea un objeto MediaRecorder dado un objeto MediaStream
          this.mediaRecorder = new MediaRecorder(stream)

          // Manejar los datos disponibles. Los guardamos en un array para usarlos luego
          this.mediaRecorder.ondataavailable = (e) => {
            this.chunks.push(e.data)
          }

          // Evento onStop
          this.mediaRecorder.onstop = (e) => {
            console.log(stream)
            console.log('recorder stopped')
            // Un objeto Blob representa un objeto tipo fichero de datos planos inmutables
            // Los Blobs representan datos que no necesariamente se encuentran en un formato nativo de JavaScript
            var blob = new Blob(this.chunks, { 'type': 'audio/wav;' })
            // Leer el archivo del objeto creado en la URL
            var reader = new FileReader()
            reader.readAsDataURL(blob)
            var objPaciente = {}
            reader.onloadend = function () {
              let base64 = reader.result
              base64 = base64.split(',')[1]
              objPaciente.idaudio = document.querySelector('#idaudio').value
              objPaciente.audio = base64
              objPaciente.genero = document.querySelector('#gender-male').checked ? 1 : 0
              objPaciente.edad = document.querySelector('#edad').value
              var jsonPaciente = JSON.stringify(objPaciente)
              // console.log(jsonPaciente)
              // console.log(base64)
              async function fetchPaciente (datos) {
                const response = await fetch('http://127.0.0.1:5000/api/audio_update', {
                  method: 'POST',
                  body: datos
                })
                return response.json()
              }
              fetchPaciente(jsonPaciente).then(({ result }) => { document.querySelector('#txtLabel').innerHTML = result })
            }
            // Vaciamos los 'trozos'
            this.chunks = []
            const audioURL = window.URL.createObjectURL(blob)
            this.audioList.push({
              src: audioURL
            })
            window.URL.revokeObjectURL(blob)
          }
        })
        .catch((err) => {
          console.log('Err: ' + err)
        })
    } else {
      this.supported = false
    }
  }
}
</script>
