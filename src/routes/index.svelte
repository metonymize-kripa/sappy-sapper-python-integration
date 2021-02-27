<style>
	h1, h2, h3,h4, figure, p {
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
		width:60%;
	}
	button {
		text-transform: uppercase;
		margin: 0 auto;
		width:20%;
		font-size: 1.6em;
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
    h4 {
		font-size: 1.2em;
		font-weight: 600;
		margin: 0 0 0.5em 0;
	}
	figure {
		margin: 0 0 1em 0;
	}
	img {
		width: 100%;
		margin: 0 0 1em 0;
	}
	p {
		margin: 1em auto;
	}

	progress {
		display: block;
		width: 200px;
		height:40px;
		margin: 0 auto;
	}
   .neutral {
        color:black;
	}
	.bearish{
		color:red;
	}
	.bullish{
		color:green;
	}
    :global(.autocomplete-list-item){
        text-align:left!important;
    }

	/*.progress-div {
	    width: 200px;
	    height: 40px;
	    align-items: center;
	    text-align: center;
	    margin: 0 auto;
	}
	.progress-label{
	    position: absolute;
	    display: block;
	    margin: -32px 90px;
	}

	progress:before {
	  content: attr(data-label);
	  font-size: 1em;
	  text-align: center;
	  margin: 8px 75px;
	  position: absolute;
	  font-weight: 800;
	}
	*/

	@media (min-width: 480px) {
		h1 {
			font-size: 4em;
		}
	}
</style>

<script>
	import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';
	import AutoComplete from "simple-svelte-autocomplete";
	const dsrandom = require('random-gif');

	const tickers = ["AAL","AAL DOOM","AAL KELLY","AAL WSB","AAL VOLUME","AAL CALL","AAPL","AAPL DOOM","AAPL KELLY","AAPL WSB","AAPL VOLUME","AAPL CALL","ALXN","ALXN DOOM","ALXN KELLY","ALXN WSB","ALXN VOLUME","ALXN CALL","AMC","AMC DOOM","AMC KELLY","AMC WSB","AMC VOLUME","AMC CALL","AMD","AMD DOOM","AMD KELLY","AMD WSB","AMD VOLUME","AMD CALL","AMZN","AMZN DOOM","AMZN KELLY","AMZN WSB","AMZN VOLUME","AMZN CALL","APHA","APHA DOOM","APHA KELLY","APHA WSB","APHA VOLUME","APHA CALL","ARKF","ARKF DOOM","ARKF KELLY","ARKF WSB","ARKF VOLUME","ARKF CALL","ARKK","ARKK DOOM","ARKK KELLY","ARKK WSB","ARKK VOLUME","ARKK CALL","BABA","BABA DOOM","BABA KELLY","BABA WSB","BABA VOLUME","BABA CALL","BAC","BAC DOOM","BAC KELLY","BAC WSB","BAC VOLUME","BAC CALL","BB","BB DOOM","BB KELLY","BB WSB","BB VOLUME","BB CALL","BKNG","BKNG DOOM","BKNG KELLY","BKNG WSB","BKNG VOLUME","BKNG CALL","BRK/B","BRK/B DOOM","BRK/B KELLY","BRK/B WSB","BRK/B VOLUME","BRK/B CALL","C","C DOOM","C KELLY","C WSB","C VOLUME","C CALL","CCIV","CCIV DOOM","CCIV KELLY","CCIV WSB","CCIV VOLUME","CCIV CALL","CCL","CCL DOOM","CCL KELLY","CCL WSB","CCL VOLUME","CCL CALL","CFO","CFO DOOM","CFO KELLY","CFO WSB","CFO VOLUME","CFO CALL","CHNG","CHNG DOOM","CHNG KELLY","CHNG WSB","CHNG VOLUME","CHNG CALL","CHTR","CHTR DOOM","CHTR KELLY","CHTR WSB","CHTR VOLUME","CHTR CALL","CRM","CRM DOOM","CRM KELLY","CRM WSB","CRM VOLUME","CRM CALL","CRSR","CRSR DOOM","CRSR KELLY","CRSR WSB","CRSR VOLUME","CRSR CALL","CVNA","CVNA DOOM","CVNA KELLY","CVNA WSB","CVNA VOLUME","CVNA CALL","CZR","CZR DOOM","CZR KELLY","CZR WSB","CZR VOLUME","CZR CALL","DIS","DIS DOOM","DIS KELLY","DIS WSB","DIS VOLUME","DIS CALL","DKNG","DKNG DOOM","DKNG KELLY","DKNG WSB","DKNG VOLUME","DKNG CALL","E","E DOOM","E KELLY","E WSB","E VOLUME","E CALL","EOD","EOD DOOM","EOD KELLY","EOD WSB","EOD VOLUME","EOD CALL","EV","EV DOOM","EV KELLY","EV WSB","EV VOLUME","EV CALL","EXPE","EXPE DOOM","EXPE KELLY","EXPE WSB","EXPE VOLUME","EXPE CALL","FB","FB DOOM","FB KELLY","FB WSB","FB VOLUME","FB CALL","FDX","FDX DOOM","FDX KELLY","FDX WSB","FDX VOLUME","FDX CALL","FE","FE DOOM","FE KELLY","FE WSB","FE VOLUME","FE CALL","FIS","FIS DOOM","FIS KELLY","FIS WSB","FIS VOLUME","FIS CALL","FISV","FISV DOOM","FISV KELLY","FISV WSB","FISV VOLUME","FISV CALL","GDDY","GDDY DOOM","GDDY KELLY","GDDY WSB","GDDY VOLUME","GDDY CALL","GE","GE DOOM","GE KELLY","GE WSB","GE VOLUME","GE CALL","GME","GME DOOM","GME KELLY","GME WSB","GME VOLUME","GME CALL","GOOGL","GOOGL DOOM","GOOGL KELLY","GOOGL WSB","GOOGL VOLUME","GOOGL CALL","GPN","GPN DOOM","GPN KELLY","GPN WSB","GPN VOLUME","GPN CALL","HCA","HCA DOOM","HCA KELLY","HCA WSB","HCA VOLUME","HCA CALL","IAC","IAC DOOM","IAC KELLY","IAC WSB","IAC VOLUME","IAC CALL","ICLN","ICLN DOOM","ICLN KELLY","ICLN WSB","ICLN VOLUME","ICLN CALL","IMO","IMO DOOM","IMO KELLY","IMO WSB","IMO VOLUME","IMO CALL","IPO","IPO DOOM","IPO KELLY","IPO WSB","IPO VOLUME","IPO CALL","JD","JD DOOM","JD KELLY","JD WSB","JD VOLUME","JD CALL","JPM","JPM DOOM","JPM KELLY","JPM WSB","JPM VOLUME","JPM CALL","LBRDK","LBRDK DOOM","LBRDK KELLY","LBRDK WSB","LBRDK VOLUME","LBRDK CALL","LSXMK","LSXMK DOOM","LSXMK KELLY","LSXMK WSB","LSXMK VOLUME","LSXMK CALL","MA","MA DOOM","MA KELLY","MA WSB","MA VOLUME","MA CALL","MELI","MELI DOOM","MELI KELLY","MELI WSB","MELI VOLUME","MELI CALL","MRO","MRO DOOM","MRO KELLY","MRO WSB","MRO VOLUME","MRO CALL","MSFT","MSFT DOOM","MSFT KELLY","MSFT WSB","MSFT VOLUME","MSFT CALL","MU","MU DOOM","MU KELLY","MU WSB","MU VOLUME","MU CALL","NFLX","NFLX DOOM","NFLX KELLY","NFLX WSB","NFLX VOLUME","NFLX CALL","NIO","NIO DOOM","NIO KELLY","NIO WSB","NIO VOLUME","NIO CALL","NOK","NOK DOOM","NOK KELLY","NOK WSB","NOK VOLUME","NOK CALL","NOW","NOW DOOM","NOW KELLY","NOW WSB","NOW VOLUME","NOW CALL","NVDA","NVDA DOOM","NVDA KELLY","NVDA WSB","NVDA VOLUME","NVDA CALL","NYC","NYC DOOM","NYC KELLY","NYC WSB","NYC VOLUME","NYC CALL","OSK","OSK DOOM","OSK KELLY","OSK WSB","OSK VOLUME","OSK CALL","PINS","PINS DOOM","PINS KELLY","PINS WSB","PINS VOLUME","PINS CALL","PLTR","PLTR DOOM","PLTR KELLY","PLTR WSB","PLTR VOLUME","PLTR CALL","PLUG","PLUG DOOM","PLUG KELLY","PLUG WSB","PLUG VOLUME","PLUG CALL","PT","PT DOOM","PT KELLY","PT WSB","PT VOLUME","PT CALL","PTON","PTON DOOM","PTON KELLY","PTON WSB","PTON VOLUME","PTON CALL","PYPL","PYPL DOOM","PYPL KELLY","PYPL WSB","PYPL VOLUME","PYPL CALL","QCOM","QCOM DOOM","QCOM KELLY","QCOM WSB","QCOM VOLUME","QCOM CALL","QQQ","QQQ DOOM","QQQ KELLY","QQQ WSB","QQQ VOLUME","QQQ CALL","R","R DOOM","R KELLY","R WSB","R VOLUME","R CALL","RIOT","RIOT DOOM","RIOT KELLY","RIOT WSB","RIOT VOLUME","RIOT CALL","RKT","RKT DOOM","RKT KELLY","RKT WSB","RKT VOLUME","RKT CALL","SE","SE DOOM","SE KELLY","SE WSB","SE VOLUME","SE CALL","SNAP","SNAP DOOM","SNAP KELLY","SNAP WSB","SNAP VOLUME","SNAP CALL","SNDL","SNDL DOOM","SNDL KELLY","SNDL WSB","SNDL VOLUME","SNDL CALL","SPY","SPY DOOM","SPY KELLY","SPY WSB","SPY VOLUME","SPY CALL","SQ","SQ DOOM","SQ KELLY","SQ WSB","SQ VOLUME","SQ CALL","TDG","TDG DOOM","TDG KELLY","TDG WSB","TDG VOLUME","TDG CALL","THCB","THCB DOOM","THCB KELLY","THCB WSB","THCB VOLUME","THCB CALL","TLRY","TLRY DOOM","TLRY KELLY","TLRY WSB","TLRY VOLUME","TLRY CALL","TMUS","TMUS DOOM","TMUS KELLY","TMUS WSB","TMUS VOLUME","TMUS CALL","TSLA","TSLA DOOM","TSLA KELLY","TSLA WSB","TSLA VOLUME","TSLA CALL","TWTR","TWTR DOOM","TWTR KELLY","TWTR WSB","TWTR VOLUME","TWTR CALL","UBER","UBER DOOM","UBER KELLY","UBER WSB","UBER VOLUME","UBER CALL","UPWK","UPWK DOOM","UPWK KELLY","UPWK WSB","UPWK VOLUME","UPWK CALL","UVXY","UVXY DOOM","UVXY KELLY","UVXY WSB","UVXY VOLUME","UVXY CALL","V","V DOOM","V KELLY","V WSB","V VOLUME","V CALL","VAR","VAR DOOM","VAR KELLY","VAR WSB","VAR VOLUME","VAR CALL","WFC","WFC DOOM","WFC KELLY","WFC WSB","WFC VOLUME","WFC CALL","WKHS","WKHS DOOM","WKHS KELLY","WKHS WSB","WKHS VOLUME","WKHS CALL"];
	let ticker = "AAL";

	const progress = tweened(0, {
		duration: 400,
		easing: cubicOut
	});


	let api_output = {"symbol":"welcome"};

	async function handleKeydown(event) {
		if (event.key === 'Enter') {
			//event.preventDefault();
			runAPI();
		}
		else {
			 return;
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


<div style='text-align: center; max-width:600px; margin: 0 auto;'>

        <AutoComplete  class="my-ac" items={tickers} bind:selectedItem={ticker}
		      on:keydown={handleKeydown}
		      maxItemsToShowInList=7 hideArrow=true placeholder="AAL" showClear=true />

        <button on:click={runAPI}>
		GO
	</button>

</div>
    <br>

{#if api_output.symbol == "waiting"}
    <h3> Options data 🏋️ getting results ...</h3>
	<figure style='width:10%;margin:0 auto'>
	<img alt='Loading' src='loadcat.gif'>
</figure>
{:else if api_output.symbol == "welcome"}
    <h2>Type'n pick ☝️ </h2>
    <br>
    <p>How to?</p>
    <h2>👇</h2>

<figure style='width:80%;margin:0 auto'>
	<img alt='Fat Tony' src='FatNeoSPYHowTo.gif'>
	<figcaption>Fat Tony: I don't normally teach, but when I do, I do. 🎷</figcaption>
</figure>
{:else}
    <br>
    <h2 class="{api_output.main_class}">{api_output.main_point}</h2>
    <p>{@html api_output.description}</p>
    <h3>{api_output.supporting_data}</h3>
    <h4 class="{api_output.secondary_class}">{api_output.secondary_point}</h4>
    <p>{api_output.secondary_description}</p>
{/if}

 <!--
<figure>
	<img alt='Fat Tony' src='{dsrandom.randomGifHacker()}'>
	<figcaption>Fat Tony: I don't get testy. I get stabby.</figcaption>
</figure>
-->
<br>
<p><strong> Sign up for the <a href='https://oracled.mailchimpsites.com/'> 📯 DailySpread 📯</a></strong></p>
