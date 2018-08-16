<template>
  <QrcodeReader
    :paused="paused"
    :track="repaintLocation"
    @decode="onDecode"
    @init="onInit">

    <div class="content">{{ content }}</div>

    <LoadingIndicator v-show="loading" />
  </QrcodeReader>
</template>

<script>
import { QrcodeReader } from 'vue-qrcode-reader'
import InitHandler from '@/mixins/InitHandler'

import tickets from '@/data/tickets.json'

const symbols = {
  info: 'Ⓘ',
  check : '✓',
  poop : '💩',
  cancel : '✘',
}

const beep = () => {
  const ctxClass = window.audioContext
    || window.AudioContext
    || window.AudioContext
    || window.webkitAudioContext

  const ctx = new ctxClass()

  const play = (duration, type = 0, callback = ()=>{}) => {
      // Only 0-4 are valid types.
      type = (type % 5) || 0
      var osc = ctx.createOscillator()
      osc.type = type
      osc.connect(ctx.destination)
      if (osc.noteOn) osc.noteOn(0) // old browsers
      if (osc.start) osc.start() // new browsers
      setTimeout(function () {
          if (osc.noteOff) osc.noteOff(0) // old browsers
          if (osc.stop) osc.stop() // new browsers
          callback()
      }, duration);
  }

  play(100, 4)
}

export default {
  name: 'Scanner',
  components: { QrcodeReader },

  mixins: [ InitHandler ],

  data () {
    return {
      content: 'Ready to scan ...',
      paused: false,
      timer: null,
    }
  },

  methods: {
    onDecode (content) {
      const ticketId = content
      const docid = tickets[ticketId]

      if(docid){
        // you can use this.paused=true
        // to stop scanner from decoding the image
        this.content = `${symbols.check} Valid ticket ${ticketId.split('-')[0]} ...`
        // you can do much more, e.g. fetch & display more Ⓘ data etc...
        beep()
      } else {
        this.content = `${symbols.cancel} Invalid ticket...`
      }

      if(this.timer){
        window.clearTimeout(this.timer)
        delete this.timer
      }
      this.timer = window.setTimeout(() => {
        this.content = 'Ready to scan ...'
      }, 2000)
    },

    repaintLocation (location, ctx) {
      //no-op instead

      // if (location !== null) {
      //   const {
      //     topLeftCorner,
      //     topRightCorner,
      //     bottomLeftCorner,
      //     bottomRightCorner,
      //   } = location

      //   ctx.strokeStyle = 'blue' // instead of red

      //   ctx.beginPath()
      //   ctx.moveTo(topLeftCorner.x, topLeftCorner.y)
      //   ctx.lineTo(bottomLeftCorner.x, bottomLeftCorner.y)
      //   ctx.lineTo(bottomRightCorner.x, bottomRightCorner.y)
      //   ctx.lineTo(topRightCorner.x, topRightCorner.y)
      //   ctx.lineTo(topLeftCorner.x, topLeftCorner.y)
      //   ctx.closePath()

      //   ctx.stroke()
      // }
    }
  }
}
</script>

<style scoped>
.content {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  max-width: 100%;

  padding: 0px 20px;
  color: #fff;
  font-weight: bold;
  padding: 10px;
  background-color: rgba(0, 0, 0, 0.5);
}
</style>
