<svelte:head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
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
    let my_kelly = "Fetching..";
    let api_output = {};
    let post_url = encodeURIComponent("https://social.oracled.com/?symbol=");
    let post_title =  encodeURIComponent("Check it out: I just FOMO optimized ");
    let gain_chance= "NA";
    let gain_class = "dark";
    let range = "Fetching.."; 
    let price = 0;
    let desc = "NA"
    let count = 9;
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
                        my_kelly = (api_output.kelly_k*100).toFixed(2);
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
		max-width: 800px;
		margin: 0 auto;
	}


	@media (min-width: 800px) {
		main {
			max-width: none;
		}
	}

    .fa {
      padding: 0.5rem;
      font-size: 1.5rem;
      width: 3rem;
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
    .t-card{
        border-radius:2rem;
        border: 1px solid #eaeaea;
        box-shadow:none;

    }
</style>
<main>

{#if my_kelly == 'Fetching..' }

<header>
  <h4 class="title is-4">Oracle is thinking .....</h4>
</header>
{:else if my_kelly =="error"}
<header>
  <h4 class="title is-4">The 💎Oracle thought deep, but couldn't for shame my promise keep</h4>
</header>
{:else}
<header>
  <h4 class="title is-4">The 💎Oracle Says:</h4>
</header>
{/if}
<br>
<div class="tile is-ancestor">    
    <div class="tile is-parent is-12" >
        <div class="tile is-child notification is-warning is-8" >
            <h2 style="font-size:3rem;margin:0; color:#00f;font-weight:700">{ticker} (${price})</h2>
            {desc}
        </div>
        <div class="tile is-child notification is-link  is-4" >
             <button style="border:none;background:none;color:#eae5a3;"on:click={handleUpVote}><i style="font-size: 2rem;" class="fa fa-thumbs-up" aria-hidden="true"></i></button>
            {count}
            <button style="border:none;background:none;color:#eae5a3;" on:click={handleDownVote}><i style="font-size: 2rem;" class="fa fa-thumbs-down" aria-hidden="true"></button>
            <br>

            {#if count > -1}
                <span class="col-3 is-vertical-align is-center fa fa-heart" style="font-size:{1.5+Math.min(count,15)/15}rem;color:hsla(360, 100%, 50%, {0.1+count/20})" ></span>
            {:else}
                <span class="col-3 is-vertical-align is-center fa fa-angle-double-down" style="font-size:{1.5+Math.min(-count,15)/15}rem;color:hsla(360, 100%, 50%, {0.1-count/20})" ></span>
            {/if}
        </div>
    </div>
</div>
<div class="tile is-ancestor">
    <div class="tile is-parent is-4 is-vertical ">
        <div class="tile is-child is-danger notification ">
            <h2 style="margin:0;font-weight:700;font-size:2rem;">1Wk Range:</h2><h2 style="color:purple;margin:0;font-weight:700;font-size:2.5rem;">{range}</h2>
        </div>
        <div class="tile is-child is-info is-light notification">
            <h2 style="margin:0;font-weight:700;font-size:2rem;">Optimal Allocation:</h2> <h2 style="color:#fb6ea8;margin:0;font-weight:700;font-size:2.5rem;">{my_kelly}%</h2>
        </div>  
     </div>
    <div class="tile is-parent is-vertical ">
        <iframe width="100%" height="420"  src="https://public.com/stocks/{ticker}/embed" frameborder="0" allow="encrypted-media" allowfullscreen allowtransparency></iframe>
    </div>
</div>
<div class="tile is-ancestor">
  <div class="tile is-parent is-12" >
        <div class="tile is-child is-1"><a href="https://reddit.com/submit?url={post_url}{ticker}&title={post_title}{ticker}" class="fa fa-reddit pull-left"></a></div>
        <div class="tile is-child is-1"><a href="https://twitter.com/share?url={post_url}{ticker}&text={post_title}{ticker}&hashtags=fomo,oracled.com" class="fa fa-twitter pull-left"></a></div>
        <div class="tile is-child is-1"><a href="https://api.whatsapp.com/send?text={post_title}{ticker} {post_url}{ticker}" class="fa fa-whatsapp pull-left"></a></div>
        <div class="tile is-child is-1"><a href="" on:click={copyurl("https://social.oracled.com/?symbol="+ticker)} class="fa fa-copy pull-left"></a></div>
        <div class="tile is-child "><a class="button is-danger" on:click={updateClipboard((my_kelly*100).toFixed(2))}>Trade@Robinhood</a></div>
    </div>

</div>


</main>

