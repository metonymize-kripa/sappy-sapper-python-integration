<svelte:head>
	<title>Social Wiki Trader</title>
</svelte:head>
<h1>Dear 💎Oracle, How much should I buy?</h1>

<script>
import { stores } from '@sapper/app';
const { preloading, page, session } = stores();
const { host, path, params, query } = $page;

let visible = true;
let ticker ='TSLA';
let portfolio_size = 100;
let amt_invest=0;
let api_output = {};
let show_entry_card = true;
let ticker_array_wsb = ['GME ','AMC ','SPY ','PLTR']
let ticker_array_gvip = ['MELI','TWTR','IAC ','TSLA']


</script>

<style>

	figure, img {
		width: 100%;
		margin: 0;
	}
</style>

<div class="row">

    <div class="card col-11 bg-light" >
      <header>
        <h4>Select from popular stock</h4>
        {#each ticker_array_wsb as tx}
            <a class="secondary button"  style="font:1.5rem;padding:1rem 0.8rem" href="/wiki/?symbol={tx}">{tx}</a>
        {/each}
        
        {#each ticker_array_gvip as tx}
            <a class="secondary button"  style="font:1.5rem;padding:1rem 0.8rem" href="/wiki/?symbol={tx}">{tx}</a>
        {/each}
      </header>
      <div class="row">
          <div class="col-6"> Or enter symbol:</div>
      </div>
       <div class="row">
          <div class="col-6"> <input bind:value={ticker}/></div>
      </div>
      
        <a class="button primary" href="/wiki/?symbol={ticker}">Go</a>
    </div>
</div>
