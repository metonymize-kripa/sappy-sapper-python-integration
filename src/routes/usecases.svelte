<svelte:head>
	<title>Use Cases</title>
</svelte:head>

<h1>Some of our use cases</h1>

<p>Options are just one of the many sources of insights that we make available for traders.
Here are a few use cases to inspire your exploration with our tools. Be bold. Hope you have fun!</p>

<h2><strong>Avoiding melt down</strong></h2>
<p>Using TICKER DOOM allows us to estimate the options implied probability of a sharp near term drop.</p>

<h1>✨ Fat Neo's Wall of Fame [Placeholder in works]</h1>

<script>
	import { onMount } from 'svelte';
	const dsrandom = require('random-gif');

	let photos = [];

	onMount(async () => {
		const res = await fetch(`https://jsonplaceholder.typicode.com/photos?_limit=4`);
		photos = await res.json();
	});
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

<div class="photos">
	{#each photos as photo}
		<figure>
			<img src='{dsrandom.randomGifDrift()}' alt={photo.title}>
		</figure>
	{:else}
		<!-- this block renders when photos.length === 0 -->
		<p>loading...</p>
	{/each}
</div>
