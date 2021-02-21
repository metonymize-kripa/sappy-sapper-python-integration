<style>
	h1, h2, h3, figure, p {
		text-align: center;
		margin: 0 auto;
	}
	h1 {
		font-size: 1.8em;
		text-transform: uppercase;
		font-weight: 400;
		margin: 0 0 0.5em 0;
	}
	input {
		font-size: 1.8em;
		text-transform: uppercase;
		font-weight: 400;
		margin: 0 auto;
		width:50%;
		
	}
	button {
		font-size: 1.7em;
		text-transform: uppercase;
		font-weight: 400;
		margin: 0 auto;
		width:40%;
	}
	h2 {
		font-size: 1.8em;
		text-transform: uppercase;
		font-weight: 1400;
		margin: 0 0 0.5em 0;
		color: green;
	}
	h3 {
		font-size: 1.8em;
		font-weight: 1400;
		margin: 0 0 0.5em 0;
		color: blue;
	}
	figure {
		margin: 0 0 1em 0;
	}
	img {
		width: 100%;
		max-width: 100px;
		margin: 0 0 1em 0;
	}
	p {
		margin: 1em auto;
	}
	@media (min-width: 480px) {
		h1 {
			font-size: 4em;
		}
	}
</style>

<script>
	let ticker = "SPY";
	let api_output = {"symbol":"no_symbol"};
	let cmd_used = 'range';
	
	async function handleKeydown(event) {
		if (event.key === 'Tab' || event.key === 'Enter' ) {
			event.preventDefault();
			runAPI();
		}
		else {
			 return;
		}
	}
		
	function runAPI() {
		var tx_array = ticker.split(/\s+/);
		if (tx_array.length > 1)
		{
			if (tx_array[1].toLowerCase() == 'volume')
			{
				cmd_used = 'volume';
				fetch("https://www.insuremystock.com/stocks/volume/"+tx_array[0])
				.then(response => response.json())
				.then(data=>api_output=data);
			}
			else if (tx_array[1].toLowerCase() == 'doom')
			{
				cmd_used = 'doom';
				fetch("https://www.insuremystock.com/options/doom/?symbol="+tx_array[0])
				.then(response => response.json())
				.then(data=>api_output=data);
			}
			else
			{
				cmd_used == 'invalid';
			}
		}
		
		else{
			fetch("./api/test?sym="+ticker)
				.then(d => d.text())
				.then(d => (api_output = JSON.parse(d)));
		}
		
	}
</script>
<div style='text-align: center; max-width:600px; margin: 0 auto;'>
	<input bind:value={ticker} on:keydown={handleKeydown} autofocus/>
	<button on:click={runAPI}>
		GO
	</button>
</div>
<br>

{#if cmd_used == "range"}
	{#if api_output.symbol == "no_symbol"}
		<p>Type Ticker then Tab/Click.</p>
	{:else if api_output.symbol == "H🥚dl."}
		<p>H🥚dl.</p>
	{:else if api_output.symbol == "invalid_symbol"}
		<p>Bro does this ticker even options?</p>
	{:else}
		{#if api_output.prob_up > 0.499}
			<h2><span style="color:green;">${api_output.low} - ${api_output.high}</span></h2>
		{:else}
			<h2><span style="color:red;">${api_output.low} - ${api_output.high}</span></h2>
		{/if}
		<p>1Wk Price Band, Options implied @ 75% Prb.</p>
		<h3>Now@ {api_output.price}</h3>
	{/if}
{:else if cmd_used == "volume"}
	{#if api_output.percentile > 60}
		<h2><span style="color:green;">{api_output.percentile}</span></h2>
	{:else if api_output.percentile < 40}
		<h2><span style="color:red;">{api_output.percentile}</span></h2>
	{:else}
		<h2><span style="color:black;">{api_output.percentile}</span></h2>
	{/if}
	
	<h3>Now@ {api_output.price}</h3>

{:else if cmd_used == "doom"}
	{#if api_output.prob_down < 20}
		<h2><span style="color:green;">{api_output.prob_down}</span></h2>
	{:else }
		<h2><span style="color:red;">{api_output.prob_down}</span></h2>
	{/if}

{:else }
	
	<h2><span style="color:red;">INVALID COMMAND</span></h2>

{/if}

<figure>
	<img alt='Fat Tony' src='FatTony.png'>
	<figcaption>Fat Tony: I don't get mad. I get stabby.</figcaption>
</figure>

<p>Type + Tab = Quote</p>

<p><strong> Sign up for the <a href='https://oracled.mailchimpsites.com/'> DailySpread</a></strong></p>
