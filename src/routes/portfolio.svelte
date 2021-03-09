<svelte:head>
	<title>My Portfolio </title>
</svelte:head>
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
</style>
<script>
    let symbol_list = ["ABBV","AMC","GILD","GME","IBM","MO","T","XOM"];
    let table_list= [];
    for(var i = 0; i < symbol_list.length; i++)
    {
        table_list.push({"symbol":symbol_list[i],"doom":"NA","prob_up":"NA","kelly":"NA","twitter":"NA"});
    }
    function get_portfolio_data() {
        for(var i = 0; i < table_list.length; i++)
        {
            fetch("https://www.insuremystock.com/options/kelly/"+table_list[i]['symbol'])
            .then(d => d.text())
            .then(function(d) {
                var my_dict = JSON.parse(d);
                for (var k = 0; k < table_list.length; k++)
                {
                    if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                    {
                        table_list[k].kelly = (my_dict.kelly*100).toFixed(2);
                        table_list[k].prob_up = Math.round(my_dict.prob_up*100);
                    }
                }
              });
          fetch("https://www.insuremystock.com/options/doom/?days=30&percent=5&symbol="+table_list[i]['symbol'])
				.then(d => d.text())
            .then(function(d) {
                var my_dict = JSON.parse(d);
                console.log(my_dict);
                for (var k = 0; k < table_list.length; k++)
                {
                    if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                    {
                        table_list[k].doom = Math.round(my_dict.prob_down*100);
                    }
                }
              });
          fetch("https://www.insuremystock.com/sentiment/twitter/"+table_list[i]['symbol'])
			.then(d => d.text())
            .then(function(d) {
                var my_dict = JSON.parse(d);
                console.log(my_dict);
                for (var k = 0; k < table_list.length; k++)
                {
                    if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                    {
                        table_list[k].twitter = Math.round(my_dict.twitter_index);
                    }
                }
              });
        }
        }

</script>

<h1>Portfolio at a glance</h1>

<table class="striped">
    <caption>
        7 day forecast
    </caption>
    <thead>
        <tr>

          <th>Symbol</th>
          <th>Optimal Allocation</th>
          <th>Doom</th>
          <th>Upside Prob</th>
          <th>Twitter Sentiment</th>
        </tr>
    </thead>
    <tbody>
        {#each table_list as { symbol,doom,prob_up,kelly,twitter }, i}
        {#if prob_up>50}
            <tr class="bullish">
                <td>{symbol}</td>
                <td>${kelly}</td>
                <td>{doom}%</td>
                <td>{prob_up}%</td>
                <td>{twitter}%</td>
            </tr>
            {:else}
            <tr class="bearish">
            <td>{symbol}</td>
            <td>${kelly}</td>
            <td>{doom}%</td>
            <td>{prob_up}%</td>
            <td>{twitter}%</td>
            </tr>
            {/if}
        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data()}>
    Refresh
</button>
