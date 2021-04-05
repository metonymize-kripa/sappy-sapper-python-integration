<svelte:head>
	<title>Use Cases</title>
</svelte:head>

<h1>Some of our use cases</h1>

<p>Options are just one of the many sources of insights that we make available for traders.
Here are a few use cases to inspire your exploration with our tools. Be bold. Hope you have fun!</p>

<h1>Wall of Fame</h1>

<script>
	import { onMount } from 'svelte';
</script>

<style>
	.photos {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		grid-gap: 8px;
	}

	figure, img {
		width: 100%;
		margin: 0;
	}
</style> 
<div class="row">
    <div class="card col-6 bg-light" >
      <header>
        <h4>Generating 20% yield from MSFT</h4>
      </header>
        You heard it right. Using fatneo, one of our users has been writing weekly covered calls on MSFT. He looks at the potential <a  href="/?symbol=msft&cmd=">one week range of MSFT</a> and writes weekly call outside that range.  He has made about $400 in a month (20% yield). If he keeps doing it for a year, he could make over $5,000.
    </div>
    <div class="card col-6 bg-light" >
      <header>
        <h4>Making money on TSLA meltdown</h4>
      </header>
        TSLA has had a bad run during Feb. It fell over 30%. One of our users believed that the stock had hit the bottom. Using <a  href="/?symbol=tsla&cmd=kelly">fatneo's Kelly skill</a> he knew the probability of upside is more than 50%. The volatility was high and so he sold a weekly $520 put and made over $1,000.
    </div>
</div>
