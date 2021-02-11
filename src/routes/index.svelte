<style>
	h1, h2, figure, p {
		text-align: center;
		margin: 0 auto;
	}
	h1, input, button {
		font-size: 2.8em;
		text-transform: uppercase;
		font-weight: 700;
		margin: 0 0 0.5em 0;
	}
	h2 {
		font-size: 5.8em;
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
		max-width: 400px;
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
	let api_output = ""
	
	async function handleKeydown(event) {
		if (event.key !== 'Tab') return;
		event.preventDefault();
		runAPI();
	}
		
	function runAPI() {
		fetch("./api/test?sym="+ticker)
			.then(d => d.text())
			.then(d => (api_output = d));
	}
</script>


<input bind:value={ticker} on:keydown={handleKeydown}>
<button on:click={runAPI}>
	Get quote
</button>

<h2><strong>{api_output}</strong></h2>

<figure>
	<img alt='Borat' src='great-success.png'>
	<figcaption>HIGH FIVE!</figcaption>
</figure>


