<svelte:head>
	<title>Trade Options</title>
</svelte:head>
<!--
<h1>💎 Oracle: What options should I trade?</h1>
-->

<script>
import { stores } from '@sapper/app';
const {  page, session } = stores();
const { host, path, params, query } = $page;
import { fade } from 'svelte/transition';

let show_initial_tile = true;
let show_social_card = false;
let show_social_result_card = false;
let show_options_card = false;
let show_options_result_card = false;

let ticker ='';
let amt_invest = 0;
let low_range = 0;
let high_range = 0;
let show_entry_card = true;
let color_class= "neutral";
let portfolio_size = 100;
let oracle_speak ="";
let api_output = {};
let ticker_array_wsb = ['GME','AMC','PLTR','TSLA']
let ticker_array_gvip = ['MELI','TWTR','IAC','SE']
function calculateRange() {
    show_initial_tile = false;
    show_social_card = false;
    show_social_result_card = false;
    show_options_card = false;
    show_options_result_card = true;
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
function calculateKelly() {
    show_initial_tile = false;
    show_social_card = false;
    show_social_result_card = true;
    show_options_card = false;
    show_options_result_card = false;
    fetch("https://www.insuremystock.com/options/kelly/"+ticker)
        .then(d => d.text())
        .then(d => {
                        api_output = JSON.parse(d);
                        console.log(api_output);
                        amt_invest = currencyFormat(api_output.kelly2*portfolio_size);
                        show_entry_card=false;
        });
}
function goback_options(){
    show_initial_tile = false;
    show_social_card = false;
    show_social_result_card = false;
    show_options_card = true;
    show_options_result_card = false;
}
function goback_social(){
    show_initial_tile = false;
    show_social_card = true;
    show_social_result_card = false;
    show_options_card = false;
    show_options_result_card = false;
}

function currencyFormat(num) {
  return num.toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}

if ('symbol' in  query){
    console.log("here");
    ticker = query['symbol'];
    if (process.browser)
        calculateRange();
}

function update_clipboard_options(newClip) {
  navigator.clipboard.writeText(newClip).then(function() {
    window.open("https://www.robinhood.com/stocks/"+ticker);
  }, function() {
    /* clipboard write failed */
  });
}

function update_clipboard_social(newClip) {
  navigator.clipboard.writeText(newClip).then(function() {
    window.open("https://www.robinhood.com/stocks/"+ticker);
  }, function() {
    /* clipboard write failed */
  });
}

function select(oracle_speak) {
    if (oracle_speak=="options")
    {
     show_initial_tile = false;
     show_social_card = false;
     show_social_result_card = false;
     show_options_card = true;
     show_options_result_card = false;
    }
    if (oracle_speak=="social")
    {
     show_initial_tile = false;
     show_social_card = true;
     show_social_result_card = false;
     show_options_card = false;
     show_options_result_card = false;
    }
}

function goback_tiles(){
    show_initial_tile = true;
    show_social_card = false;
    show_social_result_card = false;
    show_options_card = false;
    show_options_result_card = false;
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
    .initial-tile{
    height:15rem;
    margin:6rem 1rem;
    }
    .initial-tile:hover{
        transform: scale(1.2);
        background-color: #999ca9 !important;
        cursor:pointer;
    }
    .tile-h4{
    padding:5rem 0;
    text-align:center;
    }

</style>

<div class="row">
    {#if show_initial_tile}
        <div class="card col-6 bg-light initial-tile" on:click={() =>select("options")} >
          <h4 class="tile-h4">Oracle, What options should I trade?</h4>
        </div>
        <div class="card col-6 bg-light initial-tile" on:click={() =>select("social")}>
          <h4 class="tile-h4">Oracle, How much should I buy?</h4>
        </div>
    {/if}
    {#if show_options_card}
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
              <div class="col-8"> Or enter symbol:</div>
          </div>
          <div class="row">
              <div class="col-8"> <input bind:value={ticker}/></div>
          </div>
            <button class="button primary" on:click={calculateRange}>Calculate</button>
            <button class="button dark pull-right" on:click={goback_tiles}>Go Back</button>
        </div>
    {/if}
    {#if show_options_result_card}
        <div class="card col-8 bg-light" >
          {#if low_range==0}
            <h2>Getting Data. Please wait..</h2>
          {:else}
              <header>
                <h4>Oracle says sell options outside this range:</h4>
              </header>
              <h2 class="{color_class}"><a class="text-white bg-primary bd-dark" style="margin:0 1rem; font-size:1.5rem;" href='https://fatneo.com/?cmd=put&symbol={ticker}'>sell put</a>${low_range} - ${high_range}<a class="text-white bg-primary bd-dark" style="margin:0 1rem; font-size:1.5rem;" href='https://fatneo.com/?cmd=call&symbol={ticker}'>sell call</a></h2>
                <img class ="pull-left" src="robinhood.png" style="width:20%;cursor:pointer;" on:click={()=> update_clipboard_options(high_range)}>
                <br>
                <button class="button dark pull-right" on:click={goback_options}>Go Back</button>
          {/if}

        </div>
    {/if}

    {#if show_social_card}
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
        <button class="button dark pull-right" on:click={goback_tiles}>Go Back</button>
    </div>
    {/if}
    {#if show_social_result_card}
    <div class="card col-8 bg-light" >
      <header>
        <h4>Oracle says do not invest more than:</h4>
      </header>
        <h2 style="margin-bottom:0;">${amt_invest} in {ticker}</h2>
        <!--<button class="text-white bg-dark" style="margin:0 0 2rem 0 ;padding:0.5rem; font-size:1.25rem;" on:click={update_clipboard_social(amt_invest)}>copy and trade@RH</button> -->
        <img class ="pull-left" src="robinhood.png" style="width:20%;cursor:pointer;" on:click={()=> update_clipboard_social(amt_invest)}>
        <br>
        <button class="button dark pull-right" on:click={goback_social}>Go Back</button>
    </div>
    {/if}
</div>
