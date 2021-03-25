<svelte:head>
	<title>Ideal Size</title>
</svelte:head>
<h1>💎 Oracle: How much should I buy?</h1>

<script>
import { fade } from 'svelte/transition';
let ticker ='TSLA';
let portfolio_size = 100;
let amt_invest=0;
let api_output = {};
let show_entry_card = true;
let ticker_array_wsb = ['GME','AMC','SPY','PLTR','TSLA']
let ticker_array_gvip = ['MELI','TWTR','IAC','SE','LBRDK']

function calculateKelly() {
        fetch("https://www.insuremystock.com/options/kelly/"+ticker)
            .then(d => d.text())
            .then(d => {
                            api_output = JSON.parse(d);
                            console.log(api_output);
                            amt_invest = currencyFormat(api_output.kelly2*portfolio_size);
                            show_entry_card=false;
            });

}
function goback(){
    show_entry_card = true;
}


function currencyFormat(num) {
  return '$' + num.toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}
</script>

<style>


	figure, img {
		width: 100%;
		margin: 0;
	}
</style>

<div class="row">
    {#if show_entry_card}
    <div class="card col-8 bg-light" >
      <header>
        <h4>Select from popular stock</h4>
        {#each ticker_array_wsb as tx}
            <button class="secondary button"  style="font:1.5rem;padding:1rem 0.8rem" on:click={e => ticker=tx}>{tx}</button>
        {/each}
        <br>
        {#each ticker_array_gvip as tx}
            <button class="secondary button"  style="font:1.5rem;padding:1rem 0.8rem" on:click={e => ticker=tx}>{tx}</button>
        {/each}
      </header>
      <div class="row">
          <div class="col-6"> Or enter symbol:</div>
          <div class="col-6"> Your portfolio size:</div>
      </div>
      <div class="row">
          <div class="col-6"> <input bind:value={ticker}/></div>
          <div class="col-6"> <input bind:value={portfolio_size}/></div>
      </div>
        <button class="button primary" on:click={calculateKelly}>Calculate</button>
    </div>
    {:else}
    <div class="card col-8 bg-light" >
      <header>
        <h4>Oracle says do not invest more than:</h4>
      </header>
        <h2>{amt_invest} in {ticker}</h2>
        <button class="button primary" on:click={goback}>Start Again</button>
    </div>
    {/if}
</div>
