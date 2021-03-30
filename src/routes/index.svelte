<svelte:head>
	<title>Social Trader</title>
</svelte:head>
<h1>💎 Oracle, How much should I buy?</h1>

<script>
import { stores } from '@sapper/app';
const { preloading, page, session } = stores();
const { host, path, params, query } = $page;

let ticker ='TSLA';
let portfolio_size = 100;

let my_kelly = 0;
let api_output = {};
let show_entry_card = true;
let ticker_array_wsb = ['GME ','AMC ','SPY ','PLTR']
let ticker_array_gvip = ['MELI','TWTR','IAC ','TSLA']

function calculateKelly() {
        fetch("https://www.insuremystock.com/options/kelly/"+ticker)
            .then(d => d.text())
            .then(d => {
                            api_output = JSON.parse(d);
                            console.log(api_output);
                            my_kelly = api_output.kelly2;
                            show_entry_card=false;
            });

}
function goback(){
    show_entry_card = true;

    portfolio_size = 100;
}

function currencyFormat(num,decimals) {
  return num.toFixed(decimals).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}


if ('symbol' in  query){
    console.log("here");
    ticker = query['symbol'];
    if (process.browser)
        calculateKelly();
}

function updateClipboard(newClip) {
  navigator.clipboard.writeText(newClip).then(function() {

    window.open("https://www.robinhood.com/stocks/"+ticker);
  }, function() {
    /* clipboard write failed */
  });
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
         <!-- <div class="col-6"> Your portfolio size:</div> -->
      </div>
      <div class="row">
          <div class="col-6"> <input bind:value={ticker}/></div>
         <!--  <div class="col-6"> <input bind:value={portfolio_size}/></div> -->
      </div>
        <button class="button primary" on:click={calculateKelly}>Calculate</button>
    </div>
    {:else}
    <div class="card col-8 bg-light" >
      <header>
        <h4>Oracle says do not invest more than:</h4>
      </header>
        <h2 style="margin-bottom:0;">${currencyFormat(my_kelly*portfolio_size,2)} in {ticker}</h2>
        My Portfolio Size (${currencyFormat(portfolio_size,0)}):
        <input bind:value={portfolio_size} type="range" min="0" max="10000" step="100" style="width:50%;">
        <br>

        <button class="text-white bg-dark" style="margin:0 0 2rem 0 ;padding:0.5rem; font-size:1.25rem;" on:click={updateClipboard((my_kelly*portfolio_size).toFixed(2))}>copy and trade@RH</button>

        <br>

        <button class="button dark pull-right" on:click={goback}>Go Back</button>
    </div>
    {/if}
</div>
