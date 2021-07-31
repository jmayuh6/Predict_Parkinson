<template>
  <div class="home text-light">
    <BaseHeaderTitle
      title="Detección de Parkinson mediante algoritmos de Inteligencia Artificial, utilizando audios"
      subtitle1="Mayuri Hidalgo, Jesus"
      subtitle2="Medina Apaico, Walter"
    >
    </BaseHeaderTitle>

    <div class="mb-5" align="center">
      <img src="../../assets/logouni.png" alt="Logo UNI" class="w-15">
    </div>

    <div class="text-monospace">
      <p class="lead" align="justify">
        La enfermedad del Parkinson es una enfermedad progresiva y degenerativa que afecta al
sistema nervioso, los síntomas son conocidos recién
después de 4 años del inicio de la enfermedad, por lo que
existe la necesidad de aplicar ciertos métodos para
realizar un diagnóstico temprano de esta enfermedad, y
uno de ellos está relacionado con la voz. Para ello, se
aplicarán diversas técnicas actuales de Machine
Learning con el objetivo de encontrar el algoritmo
adecuado que permita la detección de Parkinson en
estados tempranos.
      </p>
    </div>
  </div>
</template>

<script>
import BaseHeaderTitle from '@/components/BaseHeaderTitle'

export default {
  name: 'home',
  components: {
    BaseHeaderTitle
  }
}
</script>
