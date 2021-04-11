<svelte:head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://unpkg.com/chota@latest">
</svelte:head>
<!--
<script context="module">
	// the (optional) preload function takes a
	// `{ path, params, query }` object and turns it into
	// the data we need to render the page
	export async function preload(page, session) {
        const { ticker } = page.params;
        return {ticker};
	}

</script>
    -->
<script>
    //import { onMount } from 'svelte';
    import { stores } from '@sapper/app';
    const { preloading, page, session } = stores();
    const { host, path, params, query } = $page;
	let ticker = 'SPY';
    ticker = ticker.toUpperCase();
    let my_kelly = "no";
    let api_output = {};
    let ticker_array_wsb = ['GME ','AMC ','SPY ','PLTR', 'UPST']
    let ticker_array_gvip = ['MELI','TWTR','IAC ','TSLA', 'SE']
    let post_url = encodeURIComponent("https://social.oracled.com/?symbol=");
    let post_title =  encodeURIComponent("Check it out: I just FOMO optimized ");
    let gain_chance= "NA";
    let gain_class = "dark";
    let varx = 0;
    function calculateKelly() {
            my_kelly = "no";
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
                        my_kelly = api_output.kelly_k;
                        let edge = api_output.prob_up - 0.5;
                        gain_chance = +(api_output.prob_up*100).toFixed(2);
                        console.log(gain_chance);
                        if (gain_chance > 52)
                            gain_class = "success";
                        else if (gain_chance < 49)
                            gain_class = "error";
                        varx = api_output.prob_down_n/api_output.prob_up_n;

                    }

                });
    }

    function currencyFormat(num,decimals) {
      return num.toFixed(decimals).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
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
    if ('symbol' in  query){
        console.log("here");
        ticker = query['symbol'];
        if (process.browser)
            calculateKelly();
    }
    else{
    ticker = 'SPY';
    if (process.browser)
        calculateKelly();
    }


</script>
<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 400px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
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
    .card{
        border-radius:2rem;
        border: 1px solid #eaeaea;
        box-shadow:none;

    }
</style>
<main>
<div class="row">
    <div class="col-10 " >
        {#if my_kelly == 'no' }
        <header>
          <h4>Oracle is thinking .....</h4>
        </header>
        {:else if my_kelly =="error"}
        <header>
          <h4>The 💎Oracle thought deep, but couldn't for shame my promise keep</h4>
        </header>
        {:else}
        <header>
          <h4>The 💎Oracle's FOMO optimized recommendation is:</h4>
        </header>
        {/if}
    </div>
    {#if my_kelly != 'no' && my_kelly != 'error' }
        <div class="col-10 card" >
            <h2 style="font-size:3rem;margin:0; ">{ticker}</h2>
            <h2 style="color:#00f;margin:0;font-weight:700;font-size:3rem;">{currencyFormat(api_output.kelly_k*100,2)}%</h2>
            <input bind:value={my_kelly} type="range" min="0" max="0.5" step="0.01" style="width:50%;margin:0 auto;">
            <span >My Allocation : {currencyFormat(my_kelly*100,2)}%</span>
        </div>
        <div class="col-10 card" >
        <table >
            <thead>
                <tr>
                    <th>1 Week Odds</th>
                    <th>Gain %</th>
                    <th>Loss %</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Option Implied</td>
                    <td><span class="tag is-large bg-success text-white">{Math.round(gain_chance)}</span></td>
                    <td><span class="tag is-large bg-error text-white">{Math.round(100-gain_chance)}</span></td>
                </tr>
                <tr>
                    <td>Override</td>
                    <td><span class="tag is-large bg-success text-white">{Math.round(((3*my_kelly)+varx)*100/(1+varx))}</span></td>
                    <td><span class="tag is-large bg-error text-white">{Math.round((1 - ((3*my_kelly+varx)/(1+varx)))*100)}</span></td>
                </tr>
            </tbody>
        </table>
        </div>
        <div class="col-10 " >
            <iframe width="100%" height="412"  src="https://public.com/stocks/{ticker}/embed" frameborder="0" allow="encrypted-media" allowfullscreen allowtransparency></iframe>
        </div>
        <div class="col-10 card" >
            <a href="https://reddit.com/submit?url={post_url}{ticker}&title={post_title}{ticker}" class="fa fa-reddit pull-left"></a>
            <a href="https://twitter.com/share?url={post_url}{ticker}&text={post_title}{ticker}&hashtags=fomo,oracled.com" class="fa fa-twitter pull-left"></a>
            <a href="https://api.whatsapp.com/send?text={post_title}{ticker} {post_url}{ticker}" class="fa fa-whatsapp pull-left"></a>
            <a href="" on:click={copyurl("https://social.oracled.com/?symbol="+ticker)} class="fa fa-copy pull-left"></a>
            <button class="text-white bg-dark pull-right" on:click={updateClipboard((my_kelly*100).toFixed(2))}>copy and trade@RH</button>
        </div>
    {/if}
</div>
</main>
