<style>
	h1, h2, h3, figure, p {
		text-align: center;
		margin: 0 auto;
	}
	h1, input, button {
		font-size: 1.8em;
		text-transform: uppercase;
		font-weight: 400;
		margin: 0 0 0.5em 0;
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
		text-transform: uppercase;
		font-weight: 1400;
		margin: 0 0 0.5em 0;
		color: purple;
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
	let py_ret = "None";
	
	async function handleKeydown(event) {
		if (event.key !== 'Tab') return;
		event.preventDefault();
		runAPI();
	}
		
	function runAPI() {
		fetch("./api/test?sym="+ticker)
			.then(d => d.text())
			.then(d => (api_output = JSON.parse(d)));
	}
</script>

<input bind:value={ticker} on:keydown={handleKeydown}>
<button on:click={runAPI}>
	Tab/Clk
</button>

{#if api_output.symbol == "no_symbol"}
	<p>Please enter a stock symbol.</p>
{:else if api_output.symbol == "invalid_symbol"}
	<p>Your symbol was invalid. Please try again</p>
{:else}
	<p>Price Outlook (1 Wk): Options implied (75% Prob.)</p>
	<h2><span style="color:red;">${api_output.low}</span> - ${api_output.high}</h2>
	<h3>Current price: ${api_output.price}</h3>
{/if}
<figure>
	<img alt='Fat Tony' src='FatTony.png'>
	<figcaption>Fat Tony: I don't get mad. I get stabby.</figcaption>
</figure>

<p>Type + Tab = Quote</p>

<p><strong> Sign up for the <a href='https://oracled.mailchimpsites.com/'> DailySpread</a></strong></p>
