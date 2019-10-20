<template>
  <qrcode-stream
    id="qr"
    :paused='paused'
    :track='repaintLocation'
    @decode='onDecode'
    @init='onInit'>

    <div class='content'>{{ content }}</div>

    <LoadingIndicator v-show='loading' />
  </qrcode-stream>
</template>

<script>
import {  QrcodeStream } from 'vue-qrcode-reader'
import InitHandler from '@/mixins/InitHandler'

import databaseDumpTicketIds from '@/data/tickets.json'

const symbols = {
  info: 'Ⓘ',
  check : '✓',
  poop : '💩',
  cancel : '✘',
}

const audioContext = new (window.audioContext
    || window.AudioContext
    || window.AudioContext
    || window.webkitAudioContext)()

const beep = (duration, type = 0, callback = ()=>{}) => {
  const types = [
    'sine', 'square', 'sawtooth', 'triangle'
  ]

  type = (type % types.length) || 0

  const osc = audioContext.createOscillator()
  osc.type = types[type]
  osc.connect(audioContext.destination)
  if (osc.noteOn) osc.noteOn(0) // old browsers
  if (osc.start) osc.start() // new browsers
  osc.onended = callback
  setTimeout(function () {
      if (osc.noteOff) osc.noteOff(0) // old browsers
      if (osc.stop) osc.stop() // new browsers
      callback()
  }, duration);
}

const makeValidTicketBeep = () => {
  beep(60, 1)
  //beep(50, 1, () => beep(5, 0))
}

const makeInvalidTicketBeep = () => {
  beep(100, 2)
}

const dumpTicketsData = Object.freeze((() => {
  const exportIdsDict = {}
  databaseDumpTicketIds.forEach(el => {
    exportIdsDict[el] = true
  })

  return exportIdsDict
})())

export default {
  name: 'Scanner',
  components: { QrcodeStream },

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
      const present = dumpTicketsData[ticketId]

      if(present){
        makeValidTicketBeep()
        // you can use this.paused=true
        // to stop scanner from decoding the image
        this.content = `${symbols.check} Valid ticket ${ticketId.split('-')[0]} ...`
        // you can do much more, e.g. fetch & display more Ⓘ data etc...
      } else {
        makeInvalidTicketBeep()
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
