<svelte:head>
	<title>Options to Sell</title>
</svelte:head>
<h1>💎 Oracle: What options should I sell?</h1>

<script>
import { fade } from 'svelte/transition';
let ticker ='';
let portfolio_size = 100;
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
        fetch("https://www.insuremystock.com/options/range/"+ticker)
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
        <button class="button primary" on:click={calculateRange}>Calculate</button>
    </div>
    {:else}
    <div class="card col-8 bg-light" >
      <header>
        <h4>Oracle says sell options outside this range:</h4>
      </header>
      {#if low_range==0}
      <h2>Getting Data. Please wait..</h2>
      {:else}
        <h2 class="{color_class}"><a class="text-white bg-primary bd-dark" style="margin:0 1rem; font-size:1.5rem;" href='https://fatneo.com/?cmd=put&symbol={ticker}'>sell put</a>${low_range} - ${high_range}<a class="text-white bg-primary bd-dark" style="margin:0 1rem; font-size:1.5rem;" href='https://fatneo.com/?cmd=call&symbol={ticker}'>sell call</a></h2>
        <button class="button primary" on:click={goback}>Start Again</button>
    {/if}

    </div>
    {/if}
</div>
