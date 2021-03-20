// store.js
import { writable } from 'svelte/store';

export const user = writable({
  name: "Avishek",
  tickers: "TSLA, TWTR, SPY, GME",
  email: "*****@gmail.com"
})
