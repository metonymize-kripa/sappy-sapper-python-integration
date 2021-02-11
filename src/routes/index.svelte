<style>
	h1, h2, textarea, figure, p {
		text-align: center;
		margin: 0 auto;
	}

	h1 {
		font-size: 2.8em;
		text-transform: uppercase;
		font-weight: 700;
		margin: 0 0 0.5em 0;
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
	let api_output = "";
	
	async function handleKeydown(event) {
		if (event.key !== 'Tab') return;	
		event.preventDefault();
		fetch("./api/test?sym="+ticker)
			.then(d => d.text())
			.then(d => (api_output = d));
	}
</script>


<svelte:head>
	<title>Sapper project template</title>
</svelte:head>

<h2>Enter ticker</h2>
<textarea value={ticker} on:keydown={handleKeydown}></textarea>

<h1>{api_output}</h1>

<figure>
	<img alt='Borat' src='great-success.png'>
	<figcaption>HIGH FIVE!</figcaption>
</figure>
