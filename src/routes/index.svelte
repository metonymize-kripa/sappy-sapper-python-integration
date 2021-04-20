<svelte:head>
	<title>Social Wiki Trader</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
</svelte:head>
<h1 class="title is-3">Dear 💎Oracle, How much should I buy?</h1>

<script>

let ticker ='TSLA';
let ticker_array_wsb = ['GME ','AMC ','SPY ','PLTR']
let ticker_array_gvip = ['MELI','TWTR','IAC ','TSLA']


</script>

<style>

	figure, img {
		width: 100%;
		margin: 0;
	}
    .button{
    margin:0.2rem;
    }
</style>

<div class="columns card">
    <div class="column is-full" >
      <header class="title is-4">
        <h4>Select from hot stock picks</h4>
        {#each ticker_array_wsb as tx}
            <a class="is-link button"  href="/wiki/?symbol={tx}">{tx}</a>
        {/each}
    <br>
        {#each ticker_array_gvip as tx}
            <a class="is-link button"   href="/wiki/?symbol={tx}">{tx}</a>
        {/each}
      </header>
      <div class="column is-half">
         Or enter symbol:
      </div>
       <div class="column is-half">
          <input class="input" bind:value={ticker}/>
      </div>
      
        <a class="button is-dark" href="/wiki/?symbol={ticker}">Go</a>
    </div>
</div>
