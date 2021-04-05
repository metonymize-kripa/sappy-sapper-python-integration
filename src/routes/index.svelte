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

function calculateKelly() {
        my_kelly = "no";
        show_entry_card=false;
        ticker = ticker.toUpperCase();
        fetch("https://www.insuremystock.com/options/kelly/"+ticker)
            .then(d => d.text())
            .then(d =>
            {
                api_output = JSON.parse(d);
                console.log(api_output);
                if ('error' in api_output)
                    my_kelly="error";
                else
                {
                    my_kelly = api_output.kelly2;
                    let edge = api_output.prob_up - 0.5;
                    risk_ruin = Math.pow( ((1-edge)/(1+edge)), (1/api_output.kelly2) );
                    console.log(risk_ruin);
                    gain_chance = +(api_output.prob_up*100).toFixed(2);
                    if (gain_chance > 52)
                        gain_class = "success";
                    else if (gain_chance < 49)
                        gain_class = "error";
                    chance_up = api_output.prob_up-0.5;
                    chance_down = api_output.prob_down;
                }

                widget_html = '<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/';
                widget_html +=ticker;
                widget_html +='/" rel="noopener" target="_blank"><span class="blue-text">';
                widget_html +=ticker;
                widget_html +=' Quotes</span></a> by TradingView</div><script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol": "';
                widget_html +=ticker;
                widget_html +='","width": "100%",height": "220","locale": "en", "dateRange": "12M", "colorTheme":"light", "trendLineColor": "rgba(69, 129, 142, 1)", "underLineColor": "rgba(217, 234, 211, 1)","isTransparent":true,"autosize":false,"largeChartUrl":"" }<\/script><\/div>';

                widget_script = '<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol": "';
                widget_script +=ticker;
                widget_script +='","width": "100%","height": "220","locale": "en", "dateRange": "12M", "colorTheme":"light", "trendLineColor": "rgba(69, 129, 142, 1)", "underLineColor": "rgba(217, 234, 211, 1)","isTransparent":true,"autosize":false,"largeChartUrl":"" }<\/script>'
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
        <h4>Top picks from r/wsb and Hedge Fund 13Fs</h4>
        {#each ticker_array_wsb as tx}
            <button class="secondary button tx-button"  on:click={e => ticker=tx}>{tx}</button>
        {/each}
        <br>
        {#each ticker_array_gvip as tx}
            <button class="secondary button tx-button"  on:click={e => ticker=tx}>{tx}</button>
        {/each}
      </header>
      <div class="row">
          <div class="col-6"> Symbol:</div>
         <!-- <div class="col-6"> Your portfolio size:</div> -->
      </div>
      <div class="row">
          <div class="col-6"> <input bind:value={ticker}/></div>
         <!--  <div class="col-6"> <input bind:value={portfolio_size}/></div> -->
      </div>
        <button class="button primary" on:click={calculateKelly}>Estimate now</button>
    </div>
    {:else}
    <div class="card col-10 bg-light" >
        {#if my_kelly == 'no' }
        <header>
          <h4>Oracle is thinking .....</h4>
        </header>
        {:else if my_kelly =="error"}
        <header>
          <h4>The 💎Oracle thought deep, but couldn't for shame my promise keep</h4>
        </header>
        <button class="button dark pull-right" on:click={goback}>Go Back</button>
        {:else}
      <header>
        <h4>The 💎Oracle's FOMO optimized recommendation is:</h4>
      </header>
        <h2 style="margin-bottom:0;">{currencyFormat(api_output.kelly2*100,2)}% in {ticker}</h2>
        <div class="row">
            <div class="col-8" >
                What if FOMO makes me pick (${currencyFormat(my_kelly*100,2)}) instead?
                <input bind:value={my_kelly} type="range" min="0" max="0.5" step="0.01" style="width:50%;">
                <br>

                <button class="text-white bg-dark" style="margin:0 0 2rem 0 ;padding:0.5rem; font-size:1.25rem;" on:click={updateClipboard((my_kelly*portfolio_size).toFixed(2))}>copy and trade@RH</button>

                <br>

            </div>
            <div class="col-4" >
                Gain chance: <button class="button {gain_class} pull-right" style="width:7rem; padding:0.4rem 0.5rem">{gain_chance}%</button>
                <br>
                <br>
                Implied Win Odds: <button class="button error pull-right" style="width:7rem; padding:0.4rem 0.5rem">{((0.5+my_kelly)/(0.5-my_kelly)).toFixed(2)}</button>

            </div>
            <!--
            <div class = "col-12">
            <embed
                src="https://public.com/stocks/{ticker}/embed"
                width = "100%"
                height="100%">
            </div>
            -->
            <!-- TradingView Widget BEGIN -->
            <!--{@html widget_html}
            {@html widget_script}
            -->

            <div class="tradingview-widget-container">
              <div class="tradingview-widget-container__widget"></div>
              <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{ticker}/" rel="noopener" target="_blank"><span class="blue-text">{ticker} Quotes</span></a> by TradingView</div>
              <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
              {
              "symbol": "TSLA",
              "width": "100%",
              "height": "220",
              "locale": "en",
              "dateRange": "12M",
              "colorTheme": "light",
              "trendLineColor": "rgba(69, 129, 142, 1)",
              "underLineColor": "rgba(217, 234, 211, 1)",
              "isTransparent": true,
              "autosize": false,
              "largeChartUrl": ""
            }
              </script>


            </div>

            <!-- TradingView Widget END -->
        </div>

        <a href="https://reddit.com/submit?url={post_url}{ticker}&title={post_title}{ticker}" class="fa fa-reddit"></a>
        <a href="https://twitter.com/share?url={post_url}{ticker}&text={post_title}{ticker}&hashtags=fomo,oracled.com" class="fa fa-twitter"></a>
        <a href="https://api.whatsapp.com/send?text={post_title}{ticker} {post_url}{ticker}" class="fa fa-whatsapp"></a>
        <a href="" on:click={copyurl("https://social.oracled.com/?symbol="+ticker)} class="fa fa-copy"></a>
        <!-- <a href="https://mail.google.com/mail/u/1/?fs=1&su={post_title}{ticker}&tf={post_url}?symbol={ticker}" class="fa fa-envelope"></a> -->
        <br>
        <br>
        <button class="button dark pull-right" on:click={goback}>Go Back</button>
        {/if}
    </div>
    {/if}
</div>
