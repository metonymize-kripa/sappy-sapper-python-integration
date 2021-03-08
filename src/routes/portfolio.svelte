<svelte:head>
	<title>My Portfolio </title>
</svelte:head>
<script>
    let symbol_list = ["IBM","T","XOM","MO","GILD","ABBV"];
    let table_list= [];
    for(var i = 0; i < symbol_list.length; i++)
    {
        table_list.push({"symbol":symbol_list[i],"range":"NA","prob_up":"NA","wsb":"NA"});
    }
    function get_portfolio_data() {
        for(var i = 0; i < table_list.length; i++)
        {
			fetch("./api/test?input_cmd="+table_list[i]['symbol']+" range")
				.then(d => d.text())
				.then(d => (table_list[i].range = JSON.parse(d).main_point));
            fetch("./api/test?input_cmd="+table_list[i].symbol+" kelly")
				.then(d => d.text())
				.then(d => (table_list[i].prob_up = JSON.parse(d).meter_value));
        }
	}

</script>

<h1>Portfolio at a glance</h1>

<table class="striped">
    <caption>
        7 day outlook
    </caption>
    <thead>
        <tr>

          <th>Symbol</th>
          <th>Range</th>
          <th>Upside Prob</th>
          <th>WSB Mentions</th>
        </tr>
    </thead>
    <tbody>
        {#each table_list as { symbol,range,prob_up,wsb }, i}
            <tr>
                <td>{symbol}</td>
                <td>{range}</td>
                <td>{prob_up}</td>
                <td>{wsb}</td>
            </tr>
        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data}>
    Refresh
</button>
