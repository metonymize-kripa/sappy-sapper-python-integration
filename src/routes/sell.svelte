<svelte:head>
	<title>Sell</title>
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
    .no-emphasis{
    font-weight:100;
    }
    emphasis{
    font-weight:1800;
    }
</style>
<script>
    let symbol_list = ["CVNA","AMC","SKT","GME","GVIP"];
    let table_list= [];
    for(var i = 0; i < symbol_list.length; i++)
    {
        table_list.push({"symbol":symbol_list[i],"sell_rating":"NA","kelly":"NA","doom":"NA","prob_down":"NA"});
    }
    function compare( a, b ) {
      if ( a.sell_rating < b.sell_rating ){
        return -1;
      }
      if ( a.sell_rating > b.sell_rating ){
        return 1;
      }
      return 0;
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
                        table_list[k].prob_down = Math.round((1-my_dict.prob_up)*100);
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

          fetch("https://www.insuremystock.com/options/prob_sigma/"+table_list[i]['symbol']+"?days=7&sigma=0.5")
			.then(d => d.text())
            .then(function(d) {
                var my_dict = JSON.parse(d);
                console.log(my_dict);
                for (var k = 0; k < table_list.length; k++)
                {
                    if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                    {
                        table_list[k].sell_rating = (my_dict.prob_down*50/my_dict.prob_up).toFixed(2);
                    }
                }
              });

        }
        table_list=table_list.sort(compare);
    }

</script>

<h1>Portfolio at a glance</h1>

<table class="striped">

    <thead>
        <tr>

          <th class="emphasis">Symbol</th>
          <th class="emphasis">SellRating</th>
          <th class="emphasis">$ to invest</th>
          <th class="no-emphasis">Meltdown Prob</th>
          <th class="no-emphasis">Prob↓</th>

        </tr>
    </thead>
    <tbody>
        {#each table_list as { symbol,sell_rating,kelly,doom,prob_down}, i}
        {#if sell_rating<50}
            <tr class="bullish">
                <td class="emphasis">{symbol}</td>
                <td class="emphasis">{sell_rating}</td>
                <td class="emphasis">${kelly}</td>
                <td class="no-emphasis">{doom}%</td>
                <td class="no-emphasis">{prob_down}%</td>
            </tr>
            {:else}
            <tr class="bearish">
                <td>{symbol}</td>
                <td>{sell_rating}</td>
                <td>${kelly}</td>
                <td>{doom}%</td>
                <td>{prob_down}%</td>
            </tr>
            {/if}
        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data()}>
    Refresh
</button>
