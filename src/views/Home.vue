<template>
    <div class="container">
      <div v-for="error in errors" class="alert alert-danger" role="alert">
        {{ error }}

        <button type="button" class="close" aria-label="Close" @click="closeError(error)">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <Scanner @error="openError" @success="clearErrors" />
    </div>
</template>

<script>

import Scanner from '@/components/Scanner.vue';

export default {
  name: 'home',

  components: {
    Scanner,
  },

  data () {
    return {
      errors: []
    }
  },

  methods: {
    openError (error) {
      this.errors.push(error)
    },

    closeError (error) {
      const index = this.errors.indexOf(error)

      this.errors.splice(index, 1)
    },

    clearErrors () {
      this.errors = []
    }
  }
}
</script>
