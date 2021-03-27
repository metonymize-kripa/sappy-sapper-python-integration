<svelte:head>
	<title>Crypto Range</title>
</svelte:head>
<h1>💎 Oracle, what's the price band for next week?</h1>

<script>
import { stores } from '@sapper/app';
const { preloading, page, session } = stores();
const { host, path, params, query } = $page;
let ticker ='';
let visible = true;
let amt_invest=0;
let api_output = {};
let low_range = 0;
let high_range = 0;
let show_entry_card = true;
let show_error = false;
let color_class= "neutral";
let ticker_array_wsb = ['BTC','ETH'];// ['USDT', 'DODGE', 'BAT', 'DAI']
function calculateRange() {
        show_entry_card=false;
        visible=true;
	low_range = 0;
        fetch("https://www.insuremystock.com/crypto/range/"+ticker)
            .then(d => d.text())
            .then(d => {
                            api_output = JSON.parse(d);
                            console.log(api_output);
                            low_range = currencyFormat(Math.round(api_output.low_range));
                            high_range = currencyFormat(Math.round(api_output.high_range));
                            if (api_output.symbol == 'Error')
                            {
                                show_error = true;
                            }


            });
}
function goback(){
    show_entry_card = true;
}
function currencyFormat(num) {
  return '$' + num.toFixed(0).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
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
    window.open("https://www.coinbase.com")
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

</style>

<div class="row">
    {#if show_entry_card}
    <div class="card col-8 bg-light" >
      <header>
        <h4>Picks from r/CryptoCurrency & Hedgeye</h4>
        {#each ticker_array_wsb as tx}
            <button class="secondary button"  style="font:1.5rem;padding:1rem 0.6rem" on:click={e => ticker=tx}>{tx}</button>
        {/each}
      </header>
      <div class="row">
          <div class="col-8"> Or enter symbol:</div>
      </div>
      <div class="row">
          <div class="col-8"> <input bind:value={ticker}/></div>
      </div>
        <button class="button primary" on:click={calculateRange}>Calculate</button>
    </div>
    {:else}
    <div class="card col-8 bg-light" >

      {#if low_range==0}
      <h2>Getting Data. Please wait..</h2>
      {:else if show_error}
        <h4>{ticker} not supported...yet </h4>
        <button class="button primary" on:click={goback}>Start Again</button>
      {:else}
      <header>
        <h4>Oracle says price will stay in this range:</h4>
      </header>
        <h2 style="margin-bottom:1rem;;" class="{color_class}">{low_range} - {high_range}</h2>
        {#if visible}
        <a class="button" style="margin:-1rem 0 2rem 0 ;padding:1rem; font-size:1.25rem; width:10rem;background: url(coinbase-logo-svg.svg) no-repeat;" href="https://www.coinbase.com"></a>
        <!--<a class="button" style="margin:-1rem 0 2rem 0 ;padding:1rem; font-size:1.25rem; width:10rem;" href="https://www.gemini.com">gemini</a> -->
        {/if}
        <br>
        <button class="button primary" on:click={goback}>Start Again</button>
    {/if}

    </div>
    {/if}
</div>
