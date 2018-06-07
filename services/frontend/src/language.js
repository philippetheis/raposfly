// ------------------------------------------------------------------------- //
// IMPORTS                                                                   //
// ------------------------------------------------------------------------- //

// Vue imports
import Vue from 'vue'
import VueI18n from 'vue-i18n'

// Languages imports
import en from './assets/i18n/en.json'
import fr from './assets/i18n/fr.json'
import de from './assets/i18n/de.json'

// ------------------------------------------------------------------------- //
// CONFIGURATION                                                             //
// ------------------------------------------------------------------------- //

// Use vue-i18n
Vue.use(VueI18n)

// Define languages
var messages = {
    en: en,
    fr: fr,
    de: de
}

export default new VueI18n({
    locale: 'en',
    fallbackLocale: 'en',
    messages
})
