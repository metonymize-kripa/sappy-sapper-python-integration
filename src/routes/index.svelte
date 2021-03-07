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
				.then(d => (api_output = JSON.parse(d)));
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
            <h2> ☝️ Symbol+skill+↵ </h2>
        {:else}
            <div style="padding:0 1rem;" class='bd-dark text-center'>
                <h2 class="{api_output.main_class}">{api_output.main_point}</h2>
                <p>{@html api_output.description}</p>
                <h3 class="supporting">{api_output.supporting_data}</h3>
            </div>
            <div style="padding:0 1rem; margin-top:1rem;" class='text-grey text-center'>
                <h4 style="margin:0.5rem 0 0 0; " class="{api_output.secondary_class}">{api_output.secondary_point}</h4>
                {#if api_output.meter_value > -1}
                    <meter value="{api_output.meter_value}" min ="0" max="100"></meter>
                {/if}
                <p>{api_output.secondary_description}</p>
            </div>
        {/if}
    </div>
    <div class="card col-4 bg-light" style="font-size:1.4rem;padding:0.1rem 0.5rem;">
      <header>
        <h4>Skills Sheet</h4>
      </header>
      <span class="text-white bg-primary bd-dark">IBM</span> - 7 day price range<br>
      <span class="text-white bg-primary bd-dark">ibm doom</span> - Prb of stock crash<br>
      <span class="text-white bg-primary bd-dark">ibm volume</span> - Relative(10d) vol<br>
      <span class="text-white bg-primary bd-dark">ibm div</span> - Last div <br>
      <span class="text-white bg-primary bd-dark">ibm dive</span> - Upcoming (Est) div<br>
      <span class="text-white bg-primary bd-dark">ibm kelly</span> - optimal allocation<br>
      <span class="text-white bg-primary bd-dark">ibm call</span> - optimal calls<br>
      <span class="text-white bg-primary bd-dark">ibm twitter</span> - optimal calls<br>
    </div>
</div>
<footer>
<p><strong>📯 Sign up for the <a href='https://oracled.mailchimpsites.com/'>DailySpread</a></strong></p>
<p>Check us at <a href='https://bearfox.live/'>Bearfox.live</a>, See us in action at <a href='https://oracled.com/'>Oracled.com</a></p>
</footer>
