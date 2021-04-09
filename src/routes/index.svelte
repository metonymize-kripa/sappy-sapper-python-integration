<svelte:head>
	<title>Show Kelly Engine</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</svelte:head>
<h1>💎Oracle, FOMO optimize this buy for me ... </h1>

<script>
import { stores } from '@sapper/app';
const { preloading, page, session } = stores();
const { host, path, params, query } = $page;

let ticker ='TSLA';
let portfolio_size = 100;


let my_kelly = "no";
let api_output = {};
let show_entry_card = true;
let ticker_array_wsb = ['GME ','AMC ','SPY ','PLTR', 'UPST']
let ticker_array_gvip = ['MELI','TWTR','IAC ','TSLA', 'SE']
let post_url = encodeURIComponent("https://social.oracled.com/?symbol=");
let post_title =  encodeURIComponent("Check it out: I just FOMO optimized ");
let gain_chance= "NA";
let gain_class = "dark";
let risk_ruin=0;
let widget_html = "";
let widget_script = "";
let chance_up=0;
let chance_down=1;

function get_widget(){
    ticker = ticker.toUpperCase();
    window.open("/stock/?symbol="+ticker);

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
    <div class="card col-8 bg-light" >
      <header>
        <h4>Top picks from r/wsb and Hedge Fund 13Fs</h4>
        {#each ticker_array_wsb as tx}
            <a class="secondary button tx-button"  href="/stock/?symbol={tx}">{tx}</a>
        {/each}
        {#each ticker_array_gvip as tx}
            <a class="secondary button tx-button"  href="/stock/?symbol={tx}">{tx}</a>
        {/each}
      </header>
      <div class="row">
          <div class="col-6"> Symbol:</div>
      </div>
      <div class="row">
          <div class="col-6"> <input bind:value={ticker}/></div>
      </div>
        <button class="button primary" on:click={get_widget}>Estimate now</button>
    </div>
</div>
