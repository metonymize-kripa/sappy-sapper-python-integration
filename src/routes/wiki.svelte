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
    let fat_kelly = "Fetching..";
    let friend_kelly = "Fetching..";
    let api_output = {};
    let post_url = encodeURIComponent("https://social.oracled.com/?symbol=");
    let post_title =  encodeURIComponent("Check it out: I just FOMO optimized ");
    let gain_chance= "NA";
    let gain_class = "dark";
    let range = "Fetching.."; 
    let price = 0;
    let desc = "NA"
    let count = 9;
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
                        my_kelly = +(api_output.kelly_k*100).toFixed(2);
                        fat_kelly = +(api_output.kelly_k*100).toFixed(2);
                        friend_kelly = +(api_output.kelly_k*100).toFixed(2)-2.3;
                        gain_chance = +(api_output.prob_up*100).toFixed(2);
                       
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
        <div class="tile is-child is-vertical is-11" >
            <iframe width="100%" height="420" src="https://public.com/stocks/{ticker}/embed" frameborder="0" allow="encrypted-media" allowfullscreen allowtransparency></iframe>
      </div>
    </div>
</div>
<div class="tile is-ancestor">
    <div class="tile is-parent is-12  ">
        <div class="tile is-child is-12 is-success notification ">
            <h2 style="margin:0;font-weight:700;font-size:2rem;color:blue;">My Rating:</h2>
            <h2 style="color:#480548;margin:0;font-weight:700;font-size:2.5rem;">{my_kelly}</h2>
            <input bind:value={my_kelly} type="range" min="-10" max="10" step="1" style="width:60%;margin:0 auto;font-size:2rem;">
            <p class="has-text-right">Chance:{Math.round((((3*my_kelly+varx)/(1+varx)))*100)}%</p>
        </div>
    </div>
</div>
<div class="tile is-ancestor">
    <div class="tile is-parent is-12  ">
        <div class="tile is-child is-6 is-danger notification ">
            <h2 style="margin:0;font-weight:700;font-size:2rem;">FatTony Says:</h2>
            <h2 style="color:#480548;margin:0;font-weight:700;font-size:2.5rem;">{fat_kelly}</h2>
            <input bind:value={fat_kelly} type="range" min="-10" max="10" step="1" style="width:60%;margin:0 auto;font-size:2rem;">
            <p class="has-text-right">Chance:{Math.round(gain_chance)}%</p>
        </div>
        <div class="tile is-child is-6 is-info  notification">
            <h2 style="margin:0;font-weight:700;font-size:2rem;">Friends Say:</h2> 
            <h2 style="color:#6d114c;margin:0;font-weight:700;font-size:2.5rem;">{friend_kelly}%</h2>
            <input bind:value={friend_kelly} type="range" min="-10" max="10" step="1" style="width:60%;margin:0 auto;font-size:2rem;">
            <p class="has-text-right">Chance:{Math.round(gain_chance-3)}%</p>
        </div>  
     </div>
</div>
<div class="tile is-ancestor">
  <div class="tile is-parent is-12" >
        <div class="tile is-child is-1"><a href="https://reddit.com/submit?url={post_url}{ticker}&title={post_title}{ticker}" class="fa fa-reddit pull-left"></a></div>
        <div class="tile is-child is-1"><a href="https://twitter.com/share?url={post_url}{ticker}&text={post_title}{ticker}&hashtags=fomo,oracled.com" class="fa fa-twitter pull-left"></a></div>
        <div class="tile is-child is-1"><a href="https://api.whatsapp.com/send?text={post_title}{ticker} {post_url}{ticker}" class="fa fa-whatsapp pull-left"></a></div>
        <div class="tile is-child is-1"><a href="" on:click={copyurl("https://social.oracled.com/?symbol="+ticker)} class="fa fa-copy pull-left"></a></div>
        <div class="tile is-child has-text-right"><a class="button is-danger text-left" on:click={updateClipboard((my_kelly*100).toFixed(2))}>Trade</a></div>
    </div>

</div>


</main>

