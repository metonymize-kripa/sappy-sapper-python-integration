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
    :global(body) {
    max-width:80rem;
    margin:0 auto;
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
</script>


<div class="row">
  <input style="width:60%;" bind:value={ticker} on:keydown={handleKeydown} autofocus/>
   <button style="width:30%;margin-left:2%;" class="button primary" on:click={runAPI}> GO </button>
</div>

<br>

{#if api_output.symbol == "waiting"}
    <h1>Running quantum computing ...</h1>
	<figure style='width:10%'>
		<img alt='Loading' src='loadcat.gif'>
	</figure>
{:else if api_output.symbol == "welcome"}
    <h2> ☝️ Type, pick, go  </h2>
{:else}
    <br>
    <h2 class="{api_output.main_class}">{api_output.main_point}</h2>
    <p>{@html api_output.description}</p>
    <h3>{api_output.supporting_data}</h3>
    <h4 class="{api_output.secondary_class}">{api_output.secondary_point}</h4>
    <p>{api_output.secondary_description}</p>
{/if}

<p><strong>📯 Sign up for the <a href='https://oracled.mailchimpsites.com/'>DailySpread</a></strong></p>
<p>Check us at <a href='https://bearfox.live/'>Bearfox.live</a>, See us in action at <a href='https://oracled.com/'>Oracled.com</a></p>
