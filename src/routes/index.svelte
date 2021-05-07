<svelte:head>
	<title>Set 1:5 Limit Order</title>
</svelte:head>
<h1>💎Oracle: What limit orders have a 1:5 chance of fill?</h1>

<script>
import { stores } from '@sapper/app';
const {  page, session } = stores();
const { host, path, params, query } = $page;
import { fade } from 'svelte/transition';
let visible = true;
let ticker ='';
let amt_invest=0;
let api_output = {};
let low_range = 0;
let high_range = 0;
let show_entry_card = true;
let color_class= "neutral";
let ticker_array_wsb = ['GME','AMC','PLTR','TSLA']
let ticker_array_gvip = ['MELI','TWTR','IAC','SE']
function calculateRange() {
    show_entry_card=false;
    visible=true;
    console.log(ticker);
    ticker = ticker.toUpperCase();
    fetch("https://www.insuremystock.com/options/range/"+ticker+"/?days=7&sigma=0.85")
        .then(d => d.text())
        .then(d => {
                        api_output = JSON.parse(d);
                        console.log(api_output);
                        low_range = Math.round(api_output.low_range);
                        high_range = Math.round(api_output.high_range);
                        if (api_output.prob_up>0.5)
                            color_class = "bullish";
                        else if (api_output.prob_up < 0.45)
                            color_class = "bearish";

        });
}
function goback(){
    show_entry_card = true;
}
function currencyFormat(num) {
  return '$' + num.toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}

if ('symbol' in  query){
    console.log("here");
    ticker = query['symbol'];
    if (process.browser)
        calculateRange();
}

function updateClipboard(newClip) {
  navigator.clipboard.writeText(newClip).then(function() {
    visible=false;
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
    .neutral{
        color:black;
	}
	.bearish{
		color:red;
	}
	.bullish{
		color:green;
	}
	h2{
		color:#dc00b6;
	}
	h1{
		color:#00f;
	}

</style>

<div class="row">
    {#if show_entry_card}
		<div class="col-2 " ></div>
    <div class="card col-8" >
      <header>
        <h2>Select from popular stock</h2>
        {#each ticker_array_wsb as tx}
            <button class="secondary button"  style="font-size: 2rem; padding: 0.6rem; margin: 0.2rem 0.2rem 1rem; background: rgb(53, 30, 181); color: white; border-radius: 1rem;" on:click={e => ticker=tx}>{tx}</button>
        {/each}
        <br>
        {#each ticker_array_gvip as tx}
            <button class="secondary button"  style="font-size: 2rem; padding: 0.6rem; margin: 0.2rem 0.2rem 1rem; background: rgb(53, 30, 181); color: white; border-radius: 1rem;" on:click={e => ticker=tx}>{tx}</button>
        {/each}
      </header>
      <div class="row">
          <div class="col-8"> Or enter symbol:</div>
      </div>
      <div class="row">
          <div class="col-8"> <input bind:value={ticker}/></div>
      </div>
        <button class="button primary is-center" style="width: 50%; margin:0 auto; color: white; background: rgb(193, 10, 169); font-size: 3rem; font-weight: 700; padding: 1rem; border-radius: 20rem;" on:click={calculateRange}>Calculate</button>
    </div>
    {:else}
		<div class="col-1"></div>
    <div class="card col-10 text-center" >

      {#if low_range==0}
      <h2>Getting Data. Please wait..</h2>
      {:else}
      <header>
        <h2>Oracle says,  sell {ticker} options outside this range:</h2>
      </header>
        <h2 class="{color_class}"><span class="text-white bg-primary bd-dark" style="margin:0 1rem; font-size:1.5rem;" on:click={()=> updateClipboard(low_range)}>
					Buy</span>${low_range} - ${high_range}
					<span class="text-white bg-primary bd-dark" style="margin:0 1rem; font-size:1.5rem;" on:click={()=> updateClipboard(high_range)}>
						Sell
					</span>
				</h2>
				<!--
        {#if visible}
        <img class ="pull-left" src="robinhood.png" style="width:20%;cursor:pointer;" on:click={()=> updateClipboard(low_range)}>
        {/if}
				-->
    {/if}

    </div>
			<div class="col-1"></div>	<div class="col-1"></div>
		<div class="col-10 " >
            <iframe width="100%" height="412"  src="https://public.com/stocks/{ticker}/embed" frameborder="0" allow="encrypted-media" allowfullscreen allowtransparency></iframe>
    </div>
		<button class="button is-center" style="width: 50%; margin:0 auto; color: white; background: rgb(193, 10, 169); font-size: 3rem; font-weight: 700; padding: 1rem; border-radius: 20rem;" on:click={goback}>Go Back</button>
    {/if}
</div>
