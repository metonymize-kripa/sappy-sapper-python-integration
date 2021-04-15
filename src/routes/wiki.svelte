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
    let post_url = encodeURIComponent("https://social.oracled.com/?symbol=");
    let post_title =  encodeURIComponent("Check it out: I just FOMO optimized ");
    let gain_chance= "NA";
    let gain_class = "dark";
    let range = "no"; 
    let price = 0;
    let desc = "NA"
    let count = 0;
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
                        gain_chance = +(api_output.prob_up*100).toFixed(2);
                       
                        if (gain_chance > 52)
                            gain_class = "success";
                        else if (gain_chance < 49)
                            gain_class = "error";
                       
                    }
                });
                fetch("https://www.insuremystock.com/options/range/"+ticker)
                .then(d => d.text())
                .then(d =>
                {
                    api_output = JSON.parse(d);
                    console.log(api_output);
                    if ('error' in api_output)
                        range="error";
                    else
                    {
                        range = "$"+currencyFormat(api_output.low_range,0)+" - $"+currencyFormat(api_output.high_range,0);
                        price = +(api_output.price).toFixed(2);
                        desc = api_output.desc;

                       
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

	
	function handleUpVote() {
		count += 1;
	}
	function handleDownVote() {
		count -= 1;
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
    <div class="col-12 " >
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
          <h4>The 💎Oracle's Says:</h4>
        </header>
        {/if}
    </div>
    {#if my_kelly != 'no' && my_kelly != 'error' }
        <div class="col-12 card" >
            <h2 style="font-size:3rem;margin:0; ">{ticker} (${price})</h2>
             Oracle says limit your allocation in {desc} to:
            <h2 style="color:#00f;margin:0;font-weight:700;font-size:3rem;">{currencyFormat(my_kelly*100,2)}%</h2>
        </div>
        <div class="col-12 card" >
        Oracle looked at the option markets and thinks that stock will stay within this range in the next week. 
        <h2 style="color:#00f;margin:0;font-weight:700;font-size:3rem;">{range}</h2>
        </div>
        <div class="col-9 card" >
            <p style="font-weight:300" class="text-left">Oracle looked at the option markets and thinks that <span style="color:#00f;font-weight:500">{desc}</span> stock, currently at <span style="color:green;font-weight:500">${price}</span> will stay within <span style="color:purple;font-weight:500">{range}</span> range in the coming week. If you really are thinking about buying this stock, oracle would urge not to put in more than {currencyFormat(my_kelly*100,2)}% of your money into it. The best call to sell would be blah blah and if you are thinking of selling put might the oracle suggest blah blah.</p>
        </div>
        <div class="col-3 card" >
        <button style="margin:0.1rem; padding:0.2rem;background:white;" on:click={handleUpVote}>👍🏼</button>
        {count}
        <button style="margin:0.1rem; padding:0.2rem; background:white" on:click={handleDownVote}>👎🏼</button>
        </div>
        <div class="col-12 card" >
            <p style="font-weight:300;" class="text-left">Oracle looked at the option markets and thinks that <span style="color:#00f;font-weight:500">{desc}</span> stock, currently at <span style="color:green;font-weight:500">${price}</span> will stay within <span style="color:purple;font-weight:500">{range}</span> range in the coming week. If you really are thinking about buying this stock, oracle would urge not to put in more than {currencyFormat(my_kelly*100,2)}% of your money into it. The best call to sell would be blah blah and if you are thinking of selling put might the oracle suggest blah blah.</p>
             <button style="margin:0.1rem; padding:0.2rem;" on:click={handleUpVote}>👍🏼</button>
        {count}
        <button style="margin:0.1rem; padding:0.2rem;" on:click={handleDownVote}>👎🏼</button>
        </div>
        <div class="col-12 " >
            <iframe width="100%" height="412"  src="https://public.com/stocks/{ticker}/embed" frameborder="0" allow="encrypted-media" allowfullscreen allowtransparency></iframe>
        </div>
        <div class="col-12 card" >
            <a href="https://reddit.com/submit?url={post_url}{ticker}&title={post_title}{ticker}" class="fa fa-reddit pull-left"></a>
            <a href="https://twitter.com/share?url={post_url}{ticker}&text={post_title}{ticker}&hashtags=fomo,oracled.com" class="fa fa-twitter pull-left"></a>
            <a href="https://api.whatsapp.com/send?text={post_title}{ticker} {post_url}{ticker}" class="fa fa-whatsapp pull-left"></a>
            <a href="" on:click={copyurl("https://social.oracled.com/?symbol="+ticker)} class="fa fa-copy pull-left"></a>
            <br>
            <button class="text-white bg-dark pull-right" on:click={updateClipboard((my_kelly*100).toFixed(2))}>copy and trade@RH</button>
        </div>
    {/if}
</div>
</main>

