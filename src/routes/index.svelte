<style>
   	.neutral{
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
</style>

<script>
	import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';
	import AutoComplete from "simple-svelte-autocomplete";
	import {Button} from 'svelte-chota';
	let button_text = 'Search';

	const demo_tickers = ["SPY DIV", "T DIVE", "TSLA DOOM", "GME WSB", "PLTR KELLY"];
	//const tickers = ["AAL","AAL DOOM","AAL KELLY","AAL WSB","AAL CALL","AAL DIV","AAL VOLUME","AAPL","AAPL DOOM","AAPL KELLY","AAPL WSB","AAPL CALL","AAPL DIV","AAPL VOLUME","ABBV","ABBV DOOM","ABBV KELLY","ABBV WSB","ABBV CALL","ABBV DIV","ABBV VOLUME","ABT","ABT DOOM","ABT KELLY","ABT WSB","ABT CALL","ABT DIV","ABT VOLUME","ADM","ADM DOOM","ADM KELLY","ADM WSB","ADM CALL","ADM DIV","ADM VOLUME","ADP","ADP DOOM","ADP KELLY","ADP WSB","ADP CALL","ADP DIV","ADP VOLUME","AFL","AFL DOOM","AFL KELLY","AFL WSB","AFL CALL","AFL DIV","AFL VOLUME","ALB","ALB DOOM","ALB KELLY","ALB WSB","ALB CALL","ALB DIV","ALB VOLUME","ALXN","ALXN DOOM","ALXN KELLY","ALXN WSB","ALXN CALL","ALXN DIV","ALXN VOLUME","AMC","AMC DOOM","AMC KELLY","AMC WSB","AMC CALL","AMC DIV","AMC VOLUME","AMCR","AMCR DOOM","AMCR KELLY","AMCR WSB","AMCR CALL","AMCR DIV","AMCR VOLUME","AMD","AMD DOOM","AMD KELLY","AMD WSB","AMD CALL","AMD DIV","AMD VOLUME","AMZN","AMZN DOOM","AMZN KELLY","AMZN WSB","AMZN CALL","AMZN DIV","AMZN VOLUME","AOS","AOS DOOM","AOS KELLY","AOS WSB","AOS CALL","AOS DIV","AOS VOLUME","APD","APD DOOM","APD KELLY","APD WSB","APD CALL","APD DIV","APD VOLUME","APHA","APHA DOOM","APHA KELLY","APHA WSB","APHA CALL","APHA DIV","APHA VOLUME","ARKF","ARKF DOOM","ARKF KELLY","ARKF WSB","ARKF CALL","ARKF DIV","ARKF VOLUME","ARKK","ARKK DOOM","ARKK KELLY","ARKK WSB","ARKK CALL","ARKK DIV","ARKK VOLUME","ATO","ATO DOOM","ATO KELLY","ATO WSB","ATO CALL","ATO DIV","ATO VOLUME","BABA","BABA DOOM","BABA KELLY","BABA WSB","BABA CALL","BABA DIV","BABA VOLUME","BAC","BAC DOOM","BAC KELLY","BAC WSB","BAC CALL","BAC DIV","BAC VOLUME","BB","BB DOOM","BB KELLY","BB WSB","BB CALL","BB DIV","BB VOLUME","BDX","BDX DOOM","BDX KELLY","BDX WSB","BDX CALL","BDX DIV","BDX VOLUME","BEN","BEN DOOM","BEN KELLY","BEN WSB","BEN CALL","BEN DIV","BEN VOLUME","BF.B","BF.B DOOM","BF.B KELLY","BF.B WSB","BF.B CALL","BF.B DIV","BF.B VOLUME","BKNG","BKNG DOOM","BKNG KELLY","BKNG WSB","BKNG CALL","BKNG DIV","BKNG VOLUME","BRK/B","BRK/B DOOM","BRK/B KELLY","BRK/B WSB","BRK/B CALL","BRK/B DIV","BRK/B VOLUME","C","C DOOM","C KELLY","C WSB","C CALL","C DIV","C VOLUME","CAH","CAH DOOM","CAH KELLY","CAH WSB","CAH CALL","CAH DIV","CAH VOLUME","CARR","CARR DOOM","CARR KELLY","CARR WSB","CARR CALL","CARR DIV","CARR VOLUME","CAT","CAT DOOM","CAT KELLY","CAT WSB","CAT CALL","CAT DIV","CAT VOLUME","CB","CB DOOM","CB KELLY","CB WSB","CB CALL","CB DIV","CB VOLUME","CCIV","CCIV DOOM","CCIV KELLY","CCIV WSB","CCIV CALL","CCIV DIV","CCIV VOLUME","CCL","CCL DOOM","CCL KELLY","CCL WSB","CCL CALL","CCL DIV","CCL VOLUME","CFO","CFO DOOM","CFO KELLY","CFO WSB","CFO CALL","CFO DIV","CFO VOLUME","CHNG","CHNG DOOM","CHNG KELLY","CHNG WSB","CHNG CALL","CHNG DIV","CHNG VOLUME","CHTR","CHTR DOOM","CHTR KELLY","CHTR WSB","CHTR CALL","CHTR DIV","CHTR VOLUME","CINF","CINF DOOM","CINF KELLY","CINF WSB","CINF CALL","CINF DIV","CINF VOLUME","CL","CL DOOM","CL KELLY","CL WSB","CL CALL","CL DIV","CL VOLUME","CLX","CLX DOOM","CLX KELLY","CLX WSB","CLX CALL","CLX DIV","CLX VOLUME","CRM","CRM DOOM","CRM KELLY","CRM WSB","CRM CALL","CRM DIV","CRM VOLUME","CRSR","CRSR DOOM","CRSR KELLY","CRSR WSB","CRSR CALL","CRSR DIV","CRSR VOLUME","CTAS","CTAS DOOM","CTAS KELLY","CTAS WSB","CTAS CALL","CTAS DIV","CTAS VOLUME","CVNA","CVNA DOOM","CVNA KELLY","CVNA WSB","CVNA CALL","CVNA DIV","CVNA VOLUME","CVX","CVX DOOM","CVX KELLY","CVX WSB","CVX CALL","CVX DIV","CVX VOLUME","CZR","CZR DOOM","CZR KELLY","CZR WSB","CZR CALL","CZR DIV","CZR VOLUME","DIS","DIS DOOM","DIS KELLY","DIS WSB","DIS CALL","DIS DIV","DIS VOLUME","DKNG","DKNG DOOM","DKNG KELLY","DKNG WSB","DKNG CALL","DKNG DIV","DKNG VOLUME","DOV","DOV DOOM","DOV KELLY","DOV WSB","DOV CALL","DOV DIV","DOV VOLUME","E","E DOOM","E KELLY","E WSB","E CALL","E DIV","E VOLUME","ECL","ECL DOOM","ECL KELLY","ECL WSB","ECL CALL","ECL DIV","ECL VOLUME","ED","ED DOOM","ED KELLY","ED WSB","ED CALL","ED DIV","ED VOLUME","EMR","EMR DOOM","EMR KELLY","EMR WSB","EMR CALL","EMR DIV","EMR VOLUME","EOD","EOD DOOM","EOD KELLY","EOD WSB","EOD CALL","EOD DIV","EOD VOLUME","ESS","ESS DOOM","ESS KELLY","ESS WSB","ESS CALL","ESS DIV","ESS VOLUME","EV","EV DOOM","EV KELLY","EV WSB","EV CALL","EV DIV","EV VOLUME","EXPD","EXPD DOOM","EXPD KELLY","EXPD WSB","EXPD CALL","EXPD DIV","EXPD VOLUME","EXPE","EXPE DOOM","EXPE KELLY","EXPE WSB","EXPE CALL","EXPE DIV","EXPE VOLUME","FB","FB DOOM","FB KELLY","FB WSB","FB CALL","FB DIV","FB VOLUME","FDX","FDX DOOM","FDX KELLY","FDX WSB","FDX CALL","FDX DIV","FDX VOLUME","FE","FE DOOM","FE KELLY","FE WSB","FE CALL","FE DIV","FE VOLUME","FIS","FIS DOOM","FIS KELLY","FIS WSB","FIS CALL","FIS DIV","FIS VOLUME","FISV","FISV DOOM","FISV KELLY","FISV WSB","FISV CALL","FISV DIV","FISV VOLUME","FRT","FRT DOOM","FRT KELLY","FRT WSB","FRT CALL","FRT DIV","FRT VOLUME","GD","GD DOOM","GD KELLY","GD WSB","GD CALL","GD DIV","GD VOLUME","GDDY","GDDY DOOM","GDDY KELLY","GDDY WSB","GDDY CALL","GDDY DIV","GDDY VOLUME","GE","GE DOOM","GE KELLY","GE WSB","GE CALL","GE DIV","GE VOLUME","GME","GME DOOM","GME KELLY","GME WSB","GME CALL","GME DIV","GME VOLUME","GOOGL","GOOGL DOOM","GOOGL KELLY","GOOGL WSB","GOOGL CALL","GOOGL DIV","GOOGL VOLUME","GPC","GPC DOOM","GPC KELLY","GPC WSB","GPC CALL","GPC DIV","GPC VOLUME","GPN","GPN DOOM","GPN KELLY","GPN WSB","GPN CALL","GPN DIV","GPN VOLUME","GWW","GWW DOOM","GWW KELLY","GWW WSB","GWW CALL","GWW DIV","GWW VOLUME","HCA","HCA DOOM","HCA KELLY","HCA WSB","HCA CALL","HCA DIV","HCA VOLUME","HRL","HRL DOOM","HRL KELLY","HRL WSB","HRL CALL","HRL DIV","HRL VOLUME","IAC","IAC DOOM","IAC KELLY","IAC WSB","IAC CALL","IAC DIV","IAC VOLUME","ICLN","ICLN DOOM","ICLN KELLY","ICLN WSB","ICLN CALL","ICLN DIV","ICLN VOLUME","IMO","IMO DOOM","IMO KELLY","IMO WSB","IMO CALL","IMO DIV","IMO VOLUME","IPO","IPO DOOM","IPO KELLY","IPO WSB","IPO CALL","IPO DIV","IPO VOLUME","ITW","ITW DOOM","ITW KELLY","ITW WSB","ITW CALL","ITW DIV","ITW VOLUME","JD","JD DOOM","JD KELLY","JD WSB","JD CALL","JD DIV","JD VOLUME","JNJ","JNJ DOOM","JNJ KELLY","JNJ WSB","JNJ CALL","JNJ DIV","JNJ VOLUME","JPM","JPM DOOM","JPM KELLY","JPM WSB","JPM CALL","JPM DIV","JPM VOLUME","KMB","KMB DOOM","KMB KELLY","KMB WSB","KMB CALL","KMB DIV","KMB VOLUME","KO","KO DOOM","KO KELLY","KO WSB","KO CALL","KO DIV","KO VOLUME","LBRDK","LBRDK DOOM","LBRDK KELLY","LBRDK WSB","LBRDK CALL","LBRDK DIV","LBRDK VOLUME","LEG","LEG DOOM","LEG KELLY","LEG WSB","LEG CALL","LEG DIV","LEG VOLUME","LIN","LIN DOOM","LIN KELLY","LIN WSB","LIN CALL","LIN DIV","LIN VOLUME","LOW","LOW DOOM","LOW KELLY","LOW WSB","LOW CALL","LOW DIV","LOW VOLUME","LSXMK","LSXMK DOOM","LSXMK KELLY","LSXMK WSB","LSXMK CALL","LSXMK DIV","LSXMK VOLUME","MA","MA DOOM","MA KELLY","MA WSB","MA CALL","MA DIV","MA VOLUME","MCD","MCD DOOM","MCD KELLY","MCD WSB","MCD CALL","MCD DIV","MCD VOLUME","MDT","MDT DOOM","MDT KELLY","MDT WSB","MDT CALL","MDT DIV","MDT VOLUME","MELI","MELI DOOM","MELI KELLY","MELI WSB","MELI CALL","MELI DIV","MELI VOLUME","MKC","MKC DOOM","MKC KELLY","MKC WSB","MKC CALL","MKC DIV","MKC VOLUME","MMM","MMM DOOM","MMM KELLY","MMM WSB","MMM CALL","MMM DIV","MMM VOLUME","MRO","MRO DOOM","MRO KELLY","MRO WSB","MRO CALL","MRO DIV","MRO VOLUME","MSFT","MSFT DOOM","MSFT KELLY","MSFT WSB","MSFT CALL","MSFT DIV","MSFT VOLUME","MU","MU DOOM","MU KELLY","MU WSB","MU CALL","MU DIV","MU VOLUME","NFLX","NFLX DOOM","NFLX KELLY","NFLX WSB","NFLX CALL","NFLX DIV","NFLX VOLUME","NIO","NIO DOOM","NIO KELLY","NIO WSB","NIO CALL","NIO DIV","NIO VOLUME","NOK","NOK DOOM","NOK KELLY","NOK WSB","NOK CALL","NOK DIV","NOK VOLUME","NOW","NOW DOOM","NOW KELLY","NOW WSB","NOW CALL","NOW DIV","NOW VOLUME","NUE","NUE DOOM","NUE KELLY","NUE WSB","NUE CALL","NUE DIV","NUE VOLUME","NVDA","NVDA DOOM","NVDA KELLY","NVDA WSB","NVDA CALL","NVDA DIV","NVDA VOLUME","NYC","NYC DOOM","NYC KELLY","NYC WSB","NYC CALL","NYC DIV","NYC VOLUME","O","O DOOM","O KELLY","O WSB","O CALL","O DIV","O VOLUME","OSK","OSK DOOM","OSK KELLY","OSK WSB","OSK CALL","OSK DIV","OSK VOLUME","OTIS","OTIS DOOM","OTIS KELLY","OTIS WSB","OTIS CALL","OTIS DIV","OTIS VOLUME","PBCT","PBCT DOOM","PBCT KELLY","PBCT WSB","PBCT CALL","PBCT DIV","PBCT VOLUME","PEP","PEP DOOM","PEP KELLY","PEP WSB","PEP CALL","PEP DIV","PEP VOLUME","PG","PG DOOM","PG KELLY","PG WSB","PG CALL","PG DIV","PG VOLUME","PINS","PINS DOOM","PINS KELLY","PINS WSB","PINS CALL","PINS DIV","PINS VOLUME","PLTR","PLTR DOOM","PLTR KELLY","PLTR WSB","PLTR CALL","PLTR DIV","PLTR VOLUME","PLUG","PLUG DOOM","PLUG KELLY","PLUG WSB","PLUG CALL","PLUG DIV","PLUG VOLUME","PNR","PNR DOOM","PNR KELLY","PNR WSB","PNR CALL","PNR DIV","PNR VOLUME","PPG","PPG DOOM","PPG KELLY","PPG WSB","PPG CALL","PPG DIV","PPG VOLUME","PT","PT DOOM","PT KELLY","PT WSB","PT CALL","PT DIV","PT VOLUME","PTON","PTON DOOM","PTON KELLY","PTON WSB","PTON CALL","PTON DIV","PTON VOLUME","PYPL","PYPL DOOM","PYPL KELLY","PYPL WSB","PYPL CALL","PYPL DIV","PYPL VOLUME","QCOM","QCOM DOOM","QCOM KELLY","QCOM WSB","QCOM CALL","QCOM DIV","QCOM VOLUME","QQQ","QQQ DOOM","QQQ KELLY","QQQ WSB","QQQ CALL","QQQ DIV","QQQ VOLUME","R","R DOOM","R KELLY","R WSB","R CALL","R DIV","R VOLUME","RIOT","RIOT DOOM","RIOT KELLY","RIOT WSB","RIOT CALL","RIOT DIV","RIOT VOLUME","RKT","RKT DOOM","RKT KELLY","RKT WSB","RKT CALL","RKT DIV","RKT VOLUME","ROP","ROP DOOM","ROP KELLY","ROP WSB","ROP CALL","ROP DIV","ROP VOLUME","RTN","RTN DOOM","RTN KELLY","RTN WSB","RTN CALL","RTN DIV","RTN VOLUME","SE","SE DOOM","SE KELLY","SE WSB","SE CALL","SE DIV","SE VOLUME","SHW","SHW DOOM","SHW KELLY","SHW WSB","SHW CALL","SHW DIV","SHW VOLUME","SNAP","SNAP DOOM","SNAP KELLY","SNAP WSB","SNAP CALL","SNAP DIV","SNAP VOLUME","SNDL","SNDL DOOM","SNDL KELLY","SNDL WSB","SNDL CALL","SNDL DIV","SNDL VOLUME","SPGI","SPGI DOOM","SPGI KELLY","SPGI WSB","SPGI CALL","SPGI DIV","SPGI VOLUME","SPY","SPY DOOM","SPY KELLY","SPY WSB","SPY CALL","SPY DIV","SPY VOLUME","SQ","SQ DOOM","SQ KELLY","SQ WSB","SQ CALL","SQ DIV","SQ VOLUME","SWK","SWK DOOM","SWK KELLY","SWK WSB","SWK CALL","SWK DIV","SWK VOLUME","SYY","SYY DOOM","SYY KELLY","SYY WSB","SYY CALL","SYY DIV","SYY VOLUME","T","T DOOM","T KELLY","T WSB","T CALL","T DIV","T VOLUME","TDG","TDG DOOM","TDG KELLY","TDG WSB","TDG CALL","TDG DIV","TDG VOLUME","TGT","TGT DOOM","TGT KELLY","TGT WSB","TGT CALL","TGT DIV","TGT VOLUME","THCB","THCB DOOM","THCB KELLY","THCB WSB","THCB CALL","THCB DIV","THCB VOLUME","Ticker","Ticker DOOM","Ticker KELLY","Ticker WSB","Ticker CALL","Ticker DIV","Ticker VOLUME","TLRY","TLRY DOOM","TLRY KELLY","TLRY WSB","TLRY CALL","TLRY DIV","TLRY VOLUME","TMUS","TMUS DOOM","TMUS KELLY","TMUS WSB","TMUS CALL","TMUS DIV","TMUS VOLUME","TROW","TROW DOOM","TROW KELLY","TROW WSB","TROW CALL","TROW DIV","TROW VOLUME","TSLA","TSLA DOOM","TSLA KELLY","TSLA WSB","TSLA CALL","TSLA DIV","TSLA VOLUME","TWTR","TWTR DOOM","TWTR KELLY","TWTR WSB","TWTR CALL","TWTR DIV","TWTR VOLUME","UBER","UBER DOOM","UBER KELLY","UBER WSB","UBER CALL","UBER DIV","UBER VOLUME","UPWK","UPWK DOOM","UPWK KELLY","UPWK WSB","UPWK CALL","UPWK DIV","UPWK VOLUME","UVXY","UVXY DOOM","UVXY KELLY","UVXY WSB","UVXY CALL","UVXY DIV","UVXY VOLUME","V","V DOOM","V KELLY","V WSB","V CALL","V DIV","V VOLUME","VAR","VAR DOOM","VAR KELLY","VAR WSB","VAR CALL","VAR DIV","VAR VOLUME","VFC","VFC DOOM","VFC KELLY","VFC WSB","VFC CALL","VFC DIV","VFC VOLUME","WBA","WBA DOOM","WBA KELLY","WBA WSB","WBA CALL","WBA DIV","WBA VOLUME","WFC","WFC DOOM","WFC KELLY","WFC WSB","WFC CALL","WFC DIV","WFC VOLUME","WKHS","WKHS DOOM","WKHS KELLY","WKHS WSB","WKHS CALL","WKHS DIV","WKHS VOLUME","WMT","WMT DOOM","WMT KELLY","WMT WSB","WMT CALL","WMT DIV","WMT VOLUME","XOM","XOM DOOM","XOM KELLY","XOM WSB","XOM CALL","XOM DIV","XOM VOLUME"];
	const tickers = [" "]
	let cached_tickers = demo_tickers.slice(0,5);
	let batch_commands = ["call", "wise"];
	let selected_ticker = "";
	let wysiwyg_ticker = "";
	let dispatched_ticker = "";

	const progress = tweened(0, {
		duration: 400,
		easing: cubicOut
	});


	let api_output = {"symbol":"welcome"};
	
	function concatArraysWithoutRepetition(arr1, arr2) {
		let cleaned_arr2 = arr2.filter( ( el ) => !arr1.includes( el ) );
		return arr1.concat(cleaned_arr2)
	}
	
	function numPartiallyMatchedFromArrayOfStrings(str1, arr_strs) {
		matches = arr_strs.filter( this_str => str1.toLowerCase().includes(this_str) );
		return matches.length
		
	}
	
	function skillType(query, batch_commands) {
		//if ( numPartiallyMatchedFromArrayOfStrings(query, batch_commands) > 0 ) {
		if ( query.toLowerCase().includes("call") ||  query.toLowerCase().includes("wise") ) {
			return "Slow skill: "
		}
		else {
			return ""
		}
	}
	
	function stashWysiwygTextInput(input_text) {
		wysiwyg_ticker = input_text
		return input_text;
	}
	
	async function updateWysiwygTextInput() {
		wysiwyg_ticker = selected_ticker
	}

	async function handleKeydown(event) {
		if (event.key === 'Enter') {
			//event.preventDefault();
			runAPI();
		}
		else {
			selected_ticker = ""
			return;
		}
	}
	function runAPI() {

			api_output = {"symbol":"waiting"};
			progress.set(0);
			//if ( selected_ticker === "") {
			if ( selected_ticker === "" ) {
				dispatched_ticker = wysiwyg_ticker
			}
			else {
				if ( selected_ticker !== wysiwyg_ticker) {
				wysiwyg_ticker = selected_ticker
				}
				dispatched_ticker = selected_ticker
			}
			fetch("./api/test?input_cmd="+dispatched_ticker)
				.then(d => d.text())
				.then(d => (api_output = JSON.parse(d)));
			selected_ticker = ""
			cached_tickers = concatArraysWithoutRepetition([dispatched_ticker],cached_tickers).slice(0,5)
	}
</script>


<!--
<div style='text-align: center; max-width:90%; margin: 0 auto;'>
</div>
        <button on:click={runAPI}>
		GO
	</button>
-->
        <AutoComplete class="my-ac"
		      textCleanFunction={stashWysiwygTextInput}
		      items={concatArraysWithoutRepetition(cached_tickers,tickers)} bind:selectedItem={selected_ticker}
		      on:keydown={handleKeydown}
		      maxItemsToShowInList=10 hideArrow=true placeholder={dispatched_ticker} showClear=true />


	<button class="button icon-only">
  <img src="https://icongr.am/feather/search.svg?size=24">
		on:click={runAPI}
</button>

<!--	
<Button 
	    on:mouseenter={ e => button_text="Go" }
	    on:mouseleave={ e => button_text="Go" }
	    on:click={runAPI}
	>{button_text}</Button>
	<p>Input:{wysiwyg_ticker}, Selected:{selected_ticker}, Dispatched:{dispatched_ticker} ...</p>
    <br>
-->

{#if api_output.symbol == "waiting"}
    <h1>{skillType(dispatched_ticker,batch_commands)+dispatched_ticker} ...</h1>
	<figure style='width:10%'>
		<img alt='Loading' src='loadcat.gif'>
	</figure>
{:else if api_output.symbol == "welcome"}
    <h2>Type then pick ☝️ </h2>
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
<p><strong>📯 Sign up for the <a href='https://oracled.mailchimpsites.com/'>DailySpread</a></strong></p>
