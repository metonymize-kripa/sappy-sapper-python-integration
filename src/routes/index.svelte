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
		margin: 10 auto;
		width:30%;
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
		max-width: 100px;
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
	.bear{
		color:red;
	}
	.bull{
		color:green;
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
    div.autocomplete{
        width:60% !important;
    }
    .autocomplete{
        width:60% !important;
    }
    autocomplete{
        width:60% !important;
    }

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

	const tickers = ["AAL","AAL DOOM","AAL KELLY","AAL WSB","AAL VOLUME","AAL NEW2","AAPL","AAPL DOOM","AAPL KELLY","AAPL WSB","AAPL VOLUME","AAPL NEW2","ALXN","ALXN DOOM","ALXN KELLY","ALXN WSB","ALXN VOLUME","ALXN NEW2","AMC","AMC DOOM","AMC KELLY","AMC WSB","AMC VOLUME","AMC NEW2","AMD","AMD DOOM","AMD KELLY","AMD WSB","AMD VOLUME","AMD NEW2","AMZN","AMZN DOOM","AMZN KELLY","AMZN WSB","AMZN VOLUME","AMZN NEW2","APHA","APHA DOOM","APHA KELLY","APHA WSB","APHA VOLUME","APHA NEW2","ARKF","ARKF DOOM","ARKF KELLY","ARKF WSB","ARKF VOLUME","ARKF NEW2","ARKK","ARKK DOOM","ARKK KELLY","ARKK WSB","ARKK VOLUME","ARKK NEW2","BABA","BABA DOOM","BABA KELLY","BABA WSB","BABA VOLUME","BABA NEW2","BAC","BAC DOOM","BAC KELLY","BAC WSB","BAC VOLUME","BAC NEW2","BB","BB DOOM","BB KELLY","BB WSB","BB VOLUME","BB NEW2","BKNG","BKNG DOOM","BKNG KELLY","BKNG WSB","BKNG VOLUME","BKNG NEW2","BRK/B","BRK/B DOOM","BRK/B KELLY","BRK/B WSB","BRK/B VOLUME","BRK/B NEW2","C","C DOOM","C KELLY","C WSB","C VOLUME","C NEW2","CCIV","CCIV DOOM","CCIV KELLY","CCIV WSB","CCIV VOLUME","CCIV NEW2","CCL","CCL DOOM","CCL KELLY","CCL WSB","CCL VOLUME","CCL NEW2","CFO","CFO DOOM","CFO KELLY","CFO WSB","CFO VOLUME","CFO NEW2","CHNG","CHNG DOOM","CHNG KELLY","CHNG WSB","CHNG VOLUME","CHNG NEW2","CHTR","CHTR DOOM","CHTR KELLY","CHTR WSB","CHTR VOLUME","CHTR NEW2","CRM","CRM DOOM","CRM KELLY","CRM WSB","CRM VOLUME","CRM NEW2","CRSR","CRSR DOOM","CRSR KELLY","CRSR WSB","CRSR VOLUME","CRSR NEW2","CVNA","CVNA DOOM","CVNA KELLY","CVNA WSB","CVNA VOLUME","CVNA NEW2","CZR","CZR DOOM","CZR KELLY","CZR WSB","CZR VOLUME","CZR NEW2","DIS","DIS DOOM","DIS KELLY","DIS WSB","DIS VOLUME","DIS NEW2","DKNG","DKNG DOOM","DKNG KELLY","DKNG WSB","DKNG VOLUME","DKNG NEW2","E","E DOOM","E KELLY","E WSB","E VOLUME","E NEW2","EOD","EOD DOOM","EOD KELLY","EOD WSB","EOD VOLUME","EOD NEW2","EV","EV DOOM","EV KELLY","EV WSB","EV VOLUME","EV NEW2","EXPE","EXPE DOOM","EXPE KELLY","EXPE WSB","EXPE VOLUME","EXPE NEW2","FB","FB DOOM","FB KELLY","FB WSB","FB VOLUME","FB NEW2","FDX","FDX DOOM","FDX KELLY","FDX WSB","FDX VOLUME","FDX NEW2","FE","FE DOOM","FE KELLY","FE WSB","FE VOLUME","FE NEW2","FIS","FIS DOOM","FIS KELLY","FIS WSB","FIS VOLUME","FIS NEW2","FISV","FISV DOOM","FISV KELLY","FISV WSB","FISV VOLUME","FISV NEW2","GDDY","GDDY DOOM","GDDY KELLY","GDDY WSB","GDDY VOLUME","GDDY NEW2","GE","GE DOOM","GE KELLY","GE WSB","GE VOLUME","GE NEW2","GME","GME DOOM","GME KELLY","GME WSB","GME VOLUME","GME NEW2","GOOGL","GOOGL DOOM","GOOGL KELLY","GOOGL WSB","GOOGL VOLUME","GOOGL NEW2","GPN","GPN DOOM","GPN KELLY","GPN WSB","GPN VOLUME","GPN NEW2","HCA","HCA DOOM","HCA KELLY","HCA WSB","HCA VOLUME","HCA NEW2","IAC","IAC DOOM","IAC KELLY","IAC WSB","IAC VOLUME","IAC NEW2","ICLN","ICLN DOOM","ICLN KELLY","ICLN WSB","ICLN VOLUME","ICLN NEW2","IMO","IMO DOOM","IMO KELLY","IMO WSB","IMO VOLUME","IMO NEW2","IPO","IPO DOOM","IPO KELLY","IPO WSB","IPO VOLUME","IPO NEW2","JD","JD DOOM","JD KELLY","JD WSB","JD VOLUME","JD NEW2","JPM","JPM DOOM","JPM KELLY","JPM WSB","JPM VOLUME","JPM NEW2","LBRDK","LBRDK DOOM","LBRDK KELLY","LBRDK WSB","LBRDK VOLUME","LBRDK NEW2","LSXMK","LSXMK DOOM","LSXMK KELLY","LSXMK WSB","LSXMK VOLUME","LSXMK NEW2","MA","MA DOOM","MA KELLY","MA WSB","MA VOLUME","MA NEW2","MELI","MELI DOOM","MELI KELLY","MELI WSB","MELI VOLUME","MELI NEW2","MRO","MRO DOOM","MRO KELLY","MRO WSB","MRO VOLUME","MRO NEW2","MSFT","MSFT DOOM","MSFT KELLY","MSFT WSB","MSFT VOLUME","MSFT NEW2","MU","MU DOOM","MU KELLY","MU WSB","MU VOLUME","MU NEW2","NFLX","NFLX DOOM","NFLX KELLY","NFLX WSB","NFLX VOLUME","NFLX NEW2","NIO","NIO DOOM","NIO KELLY","NIO WSB","NIO VOLUME","NIO NEW2","NOK","NOK DOOM","NOK KELLY","NOK WSB","NOK VOLUME","NOK NEW2","NOW","NOW DOOM","NOW KELLY","NOW WSB","NOW VOLUME","NOW NEW2","NVDA","NVDA DOOM","NVDA KELLY","NVDA WSB","NVDA VOLUME","NVDA NEW2","NYC","NYC DOOM","NYC KELLY","NYC WSB","NYC VOLUME","NYC NEW2","OSK","OSK DOOM","OSK KELLY","OSK WSB","OSK VOLUME","OSK NEW2","PINS","PINS DOOM","PINS KELLY","PINS WSB","PINS VOLUME","PINS NEW2","PLTR","PLTR DOOM","PLTR KELLY","PLTR WSB","PLTR VOLUME","PLTR NEW2","PLUG","PLUG DOOM","PLUG KELLY","PLUG WSB","PLUG VOLUME","PLUG NEW2","PT","PT DOOM","PT KELLY","PT WSB","PT VOLUME","PT NEW2","PTON","PTON DOOM","PTON KELLY","PTON WSB","PTON VOLUME","PTON NEW2","PYPL","PYPL DOOM","PYPL KELLY","PYPL WSB","PYPL VOLUME","PYPL NEW2","QCOM","QCOM DOOM","QCOM KELLY","QCOM WSB","QCOM VOLUME","QCOM NEW2","QQQ","QQQ DOOM","QQQ KELLY","QQQ WSB","QQQ VOLUME","QQQ NEW2","R","R DOOM","R KELLY","R WSB","R VOLUME","R NEW2","RIOT","RIOT DOOM","RIOT KELLY","RIOT WSB","RIOT VOLUME","RIOT NEW2","RKT","RKT DOOM","RKT KELLY","RKT WSB","RKT VOLUME","RKT NEW2","SE","SE DOOM","SE KELLY","SE WSB","SE VOLUME","SE NEW2","SNAP","SNAP DOOM","SNAP KELLY","SNAP WSB","SNAP VOLUME","SNAP NEW2","SNDL","SNDL DOOM","SNDL KELLY","SNDL WSB","SNDL VOLUME","SNDL NEW2","SPY","SPY DOOM","SPY KELLY","SPY WSB","SPY VOLUME","SPY NEW2","SQ","SQ DOOM","SQ KELLY","SQ WSB","SQ VOLUME","SQ NEW2","TDG","TDG DOOM","TDG KELLY","TDG WSB","TDG VOLUME","TDG NEW2","THCB","THCB DOOM","THCB KELLY","THCB WSB","THCB VOLUME","THCB NEW2","TLRY","TLRY DOOM","TLRY KELLY","TLRY WSB","TLRY VOLUME","TLRY NEW2","TMUS","TMUS DOOM","TMUS KELLY","TMUS WSB","TMUS VOLUME","TMUS NEW2","TSLA","TSLA DOOM","TSLA KELLY","TSLA WSB","TSLA VOLUME","TSLA NEW2","TWTR","TWTR DOOM","TWTR KELLY","TWTR WSB","TWTR VOLUME","TWTR NEW2","UBER","UBER DOOM","UBER KELLY","UBER WSB","UBER VOLUME","UBER NEW2","UPWK","UPWK DOOM","UPWK KELLY","UPWK WSB","UPWK VOLUME","UPWK NEW2","UVXY","UVXY DOOM","UVXY KELLY","UVXY WSB","UVXY VOLUME","UVXY NEW2","V","V DOOM","V KELLY","V WSB","V VOLUME","V NEW2","VAR","VAR DOOM","VAR KELLY","VAR WSB","VAR VOLUME","VAR NEW2","WFC","WFC DOOM","WFC KELLY","WFC WSB","WFC VOLUME","WFC NEW2","WKHS","WKHS DOOM","WKHS KELLY","WKHS WSB","WKHS VOLUME","WKHS NEW2"];

	let selectedTicker = "AAL";

	const progress = tweened(0, {
		duration: 400,
		easing: cubicOut
	});

	let ticker = "SPY";

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

<div>
	<AutoComplete items={tickers} bind:selectedItem={ticker} on:keydown={handleKeydown} maxItemsToShowInList=5/>
	<button on:click={runAPI}>
		GO
	</button>
</div>

{#if api_output.symbol == "waiting"}
    <p>Getting results.....</p>
{:else if api_output.symbol == "welcome"}
    <p>Type in something</p>
{:else}
    <br>
    <h2 style="class:{api_output.main_class};">{api_output.main_point}</h2>
    <p>{@html api_output.description}</p>
    <h3>{api_output.supporting_data}</h3>
    <h4 style="class:{api_output.secondary_class};">{api_output.secondary_point}</h4>
    <p>{api_output.secondary_description}</p>
{/if}

<figure>
	<img alt='Fat Tony' src='FatTony.png'>
	<figcaption>Fat Tony: I don't get mad. I get stabby.</figcaption>
</figure>

<p><strong> Sign up for the <a href='https://oracled.mailchimpsites.com/'> DailySpread</a></strong></p>
