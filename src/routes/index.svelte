<svelte:head>
	<title>Show Kelly Engine</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</svelte:head>
<h1>💎 Oracle, How much should I buy? (Show me your work)</h1>

<script>
import { stores } from '@sapper/app';
const { preloading, page, session } = stores();
const { host, path, params, query } = $page;

let ticker ='TSLA';
let portfolio_size = 100;

let my_kelly = "no";
let api_output = {};
let show_entry_card = true;
let ticker_array_wsb = ['GME ','AMC ','SPY ','PLTR']
let ticker_array_gvip = ['MELI','TWTR','IAC ','TSLA']
let post_url = encodeURIComponent("https://social.oracled.com/?symbol=");
let post_title =  encodeURIComponent("Hey, I just Oracled "+ticker+" ... check it out");

function calculateKelly() {
        my_kelly = "no";
        show_entry_card=false;
        ticker = ticker.toUpperCase();
        fetch("https://www.insuremystock.com/options/kelly/"+ticker)
            .then(d => d.text())
            .then(d => {
                            api_output = JSON.parse(d);
                            console.log(api_output);
                            if ('error' in api_output)
                                my_kelly="error";
                            else
                                my_kelly = api_output.kelly2;
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

function copyurl(my_url) {
  navigator.clipboard.writeText(my_url).then(function() {

    /* clipboard success. Maybe toast it? */
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
    .tx-button{
        font:1.5rem;
        padding:1rem 0.8rem
    }
    .fa {
      padding: 1rem;
      font-size: 1.5rem;
      width: 4rem;
      text-align: center;
    }

    .fa:hover {
        opacity: 0.7;
    }

    .fa-twitter {
      background: #55ACEE;
      color: white;
    }

    .fa-google {
      background: #dd4b39;
      color: white;
    }

    .fa-linkedin {
      background: #007bb5;
      color: white;
    }

    .fa-reddit {
      background: #ff5700;
      color: white;
    }

    .fa-whatsapp {
      background: #43d854;
      color: white;
    }

    .fa-envelope {
      background: #3f4144;
      color: white;
    }
    .fa-copy {
      background: #3f4144;
      color: white;
    }

</style>

<div class="row">
    {#if show_entry_card}
    <div class="card col-8 bg-light" >
      <header>
        <h4>Select from popular stock</h4>
        {#each ticker_array_wsb as tx}
            <button class="secondary button tx-button"  on:click={e => ticker=tx}>{tx}</button>
        {/each}
        <br>
        {#each ticker_array_gvip as tx}
            <button class="secondary button tx-button"  on:click={e => ticker=tx}>{tx}</button>
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
    <div class="card col-10 bg-light" >
        {#if my_kelly == 'no' }
        <header>
          <h4>Oracle is thinking .....</h4>
        </header>
        {:else if my_kelly =="error"}
        <header>
          <h4>Oracle though hard and long but could not find enough option data to come up with an answer</h4>
        </header>
        <button class="button dark pull-right" on:click={goback}>Go Back</button>
        {:else}
      <header>
        <h4>Oracle says do not invest more than:</h4>
      </header>
        <h2 style="margin-bottom:0;">{currencyFormat(api_output.kelly2*100,2)}% in {ticker}</h2>
        <div class="row">
            <div class="col-8" >
                I want to make my own decision (${currencyFormat(my_kelly*100,2)}):
                <input bind:value={my_kelly} type="range" min="0" max="1" step="0.01" style="width:50%;">
                <br>

                <button class="text-white bg-dark" style="margin:0 0 2rem 0 ;padding:0.5rem; font-size:1.25rem;" on:click={updateClipboard((my_kelly*portfolio_size).toFixed(2))}>copy and trade@RH</button>

                <br>

            </div>
            <div class="col-3" >
                Risk: <button class="button error pull-right" style="width:7rem; padding:0.4rem 0.5rem">{(Math.pow( ((1-api_output.kelly2)/(1+api_output.kelly2)), (1/my_kelly) )*100).toFixed(2)}%</button>
                <br>
                <br>
                Return: <button class="button success pull-right" style="width:7rem; padding:0.4rem 0.5rem">${(100*my_kelly*my_kelly).toFixed(2)}</button>


            </div>
        </div>
        <a href="https://reddit.com/submit?url={post_url}{ticker}&title={post_title}" class="fa fa-reddit"></a>
        <a href="https://twitter.com/share?url={post_url}{ticker}&text={post_title}&hashtags=kelly,fatneo" class="fa fa-twitter"></a>
        <a href="https://api.whatsapp.com/send?text={post_title} {post_url}{ticker}" class="fa fa-whatsapp"></a>
        <a href="" on:click={copyurl("https://social.oracled.com/?symbol="+ticker)} class="fa fa-copy"></a>
        <!-- <a href="https://mail.google.com/mail/u/1/?fs=1&su={post_title}{ticker}&tf={post_url}?symbol={ticker}" class="fa fa-envelope"></a> -->
        <button class="button dark pull-right" on:click={goback}>Go Back</button>
        {/if}
    </div>
    {/if}
</div>
