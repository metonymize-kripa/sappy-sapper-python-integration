<style>
	h1, h2, figure, p {
		text-align: center;
		margin: 0 auto;
	}
	h1, input, button {
		font-size: 2.8em;
		text-transform: uppercase;
		font-weight: 400;
		margin: 0 0 0.5em 0;
	}
	h2 {
		font-size: 2.8em;
		text-transform: uppercase;
		font-weight: 1400;
		margin: 0 0 0.5em 0;
		color: green;
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
	Tab or Clk
</button>

{#if api_output.symbol == "no_symbol"}
	<p>Please enter a symbol to see the range of price the stock can take in a week</p>
{:else if api_output.symbol == "invalid_symbol"}
	<h3>Your symbol was invalid. Please try again</h3>
{:else}
	<h1>{api_output.symbol} ($ {api_output.price})</h1>
	<h3>One week range (3:1 odds):</h3>
	<h2><span style="color:red;">${api_output.low}</span> - ${api_output.high}</h2>
{/if}
<figure>
	<img alt='Fat Tony' src='FatTony.png'>
	<figcaption>Fat Tony: I don't get mad. I get stabby.</figcaption>
</figure>

<p>Type + Tab = Quote</p>

<p><strong> Sign up for the <a href='https://oracled.mailchimpsites.com/'> DailySpread</a></strong></p>
