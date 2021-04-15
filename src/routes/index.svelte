<style>
   	.neutral{
        color:black;
	}
	.bearish{
		color:red;
	}
	.bullish{
		color:green;
	}
    .supporting{
        color:navy;
    }
    .explain{
    font-size:1.2rem;
    color:grey;
    }
    a.card-button:hover{
        background:red;
    }

    :global(body) {
    max-width:80rem;
    margin:0 auto;
    }
    :global(meter){
    width:12rem;
    height:3rem;
    }

	:global(.autocomplete-list-item){
        text-align:left!important;
	}
</style>

<script>
	import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';
	import {Button} from 'svelte-chota';
	let button_text = 'Go';
	let batch_commands = ["call", "wise"];
    let ticker = "";
    let card_ticker = 'SPY';
    let tag1 = "";
    let tag2 = "";
    let tag3 = "";

    import { stores } from '@sapper/app';
    const { preloading, page, session } = stores();
    const { host, path, params, query } = $page;


    async function handleKeydown(event) {
		if (event.key === 'Tab' || event.key === 'Enter' ) {
			event.preventDefault();
			runAPI();
		}
		else {
			 return;
		}
	}
	const progress = tweened(0, {
		duration: 400,
		easing: cubicOut
	});

	let api_output = {"symbol":"welcome"};

	function skillType(query, batch_commands) {
		if ( query.toLowerCase().includes("call") ||  query.toLowerCase().includes("wise") ) {
			return "Slow skill: "
		}
		else {
			return ""
		}
	}

	function runAPI() {
		api_output = {"symbol":"waiting"};
		progress.set(0);
		fetch("./api/test?input_cmd="+ticker)
			.then(d => d.text())
			.then(d => {
                            api_output = JSON.parse(d);
                            card_ticker = api_output.symbol;
                            console.log(api_output);
                            tag1 = api_output.tag1;
                            tag2 = api_output.tag2;
                            tag3 = api_output.tag3;
                        });
	    }
    function getAPIData(cmd,symbol){
            ticker = symbol+" "+cmd;
            runAPI();
        }

    let cmd_to_run_from_get="";
    let symbol_to_run_from_get='spy';
    if ('cmd' in  query){
        cmd_to_run_from_get = query['cmd'];
        if ('symbol' in  query){
            symbol_to_run_from_get = query['symbol'];
        }
        ticker = symbol_to_run_from_get+" "+cmd_to_run_from_get;
        runAPI();

    }

</script>

<h1>₿ Welcome Peter!</h1>

<div class="row">
<div class="grouped col-12">
 <div class="col-8"> <input bind:value={ticker} on:keydown={handleKeydown} autofocus/></div>
  <div class="col-4"><button class="button primary" on:click={runAPI}> GO </button></div>
</div>
</div>


<div class="row">
    <div class="col-8">
        {#if api_output.symbol == "waiting"}
            <h1>Running quantum computing ...</h1>
        	<figure style='width:10%'>
        		<img alt='Loading' src='loadcat.gif'>
        	</figure>
        {:else if api_output.symbol == "welcome"}
            <h2> ☝️ Symbol ⎵ skill ↵ </h2>
        <!--    <figure>
            	<img alt='Fat Tony' src='FatTony.png'>
            	<figcaption>Fat Tony: I don't get mad. I get stabby.</figcaption>
            </figure> -->
        {:else}
            <div style="padding:0 1rem;" class='bd-dark text-center'>
                <h2 style ="margin:1rem 0px -0.5rem 0px;" class="{api_output.main_class}">{@html api_output.main_point}</h2>
                {#if tag1 != ""}
                    <a class="text-white bg-primary bd-dark" style="margin:0 2rem; font-size:1.5rem;" href='' on:click={getAPIData("put",api_output.symbol)}>{tag1}</a><a class="text-white bg-primary bd-dark" style='margin:0 2rem; font-size:1.5rem;' href='' on:click={getAPIData("call",api_output.symbol)}>{tag2}</a>
                {/if}
                <p>{@html api_output.description}</p>
                {#if tag3 != ""}
                    <a class="text-white bg-primary bd-dark" style="margin:1rem; font-size:1.5rem;" href='' on:click={getAPIData("insure",api_output.symbol)}>{tag3}</a>
                {/if}
                <h3 class="supporting">{api_output.supporting_data}</h3>
            </div>
            <div style="padding:0 1rem; margin-top:1rem;" class='text-grey text-center'>
                <h4 style="margin:0.5rem 0 0 0; " class="{api_output.secondary_class}">{api_output.secondary_point}</h4>
               <!--
                {#if api_output.meter_value > -1}
                    <meter value="{api_output.meter_value}" min ="0" max="100"></meter>
                {/if}
                -->
                <p>{api_output.secondary_description}</p>
            </div>
            <p class="explain">{@html api_output.explain}</p>
        {/if}
    </div>
    <div class="card col-4 bg-light" style="font-size:1.4rem;padding:0.1rem 0.5rem;">
      <header>
        <h4>Skills Sheet</h4>
      </header>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("range",card_ticker)}  href="">{card_ticker} range </a> - 7 day price range<br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("call",card_ticker)} href="">{card_ticker} call</a> - Optimal calls<br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("put",card_ticker)} href="">{card_ticker} put</a> - Optimal puts<br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("doom",card_ticker)} href="">{card_ticker} doom</a> - Prb of stock crash<br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("wsb",card_ticker)} href="">{card_ticker} wsb</a> - r/wallstreetbets mentions<br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("kelly",card_ticker)} href="">{card_ticker} kelly</a> - Optimal allocation<br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("volume",card_ticker)} href="">{card_ticker} volume</a> - Relative(10d) vol<br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("div",card_ticker)} href="">{card_ticker} div</a> - Last div <br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("dive",card_ticker)} href="">{card_ticker} dive</a> - Upcoming (Est) div<br>
      <a class="text-white bg-primary bd-dark" on:click={getAPIData("twitter",card_ticker)} href="">{card_ticker} twitter</a> - Twitter sentiment<br>
      <!-- <a class="text-white bg-primary bd-dark" href="/?symbol=BTC&cmd=crypto">BTC crypto</a> - crypto 7 day range <br> -->
    </div>
</div>
<footer>
<p><strong>📯 Try the <a href='https://oracled.mailchimpsites.com/'>DailySpread</a></strong></p>
<p>Check us at <a href='https://bearfox.live/'>Bearfox.live</a>, See us in action at <a href='https://oracled.com/'>Oracled.com</a></p>
</footer>
