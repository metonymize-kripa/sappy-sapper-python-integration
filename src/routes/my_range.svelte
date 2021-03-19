<svelte:head>
	<title>My Range </title>
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
    let symbol_list = ["ABBV","GILD","GME","IBM","MO","T","XOM"];
    let table_list= [];
    for(var i = 0; i < symbol_list.length; i++)
    {
        table_list.push({"symbol":symbol_list[i],"range_1wk":"NA","range_2wk":"NA","range_3wk":"NA"});
    }
    function get_portfolio_data() {
        for(var i = 0; i < table_list.length; i++)
        {
        fetch("https://www.insuremystock.com/options/range/"+table_list[i]['symbol'])
        .then(d => d.text())
        .then(function(d) {

            var my_dict = JSON.parse(d);
            for (var k = 0; k < table_list.length; k++)
            {
                if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                {
                    table_list[k].range_1wk = "$"+Math.round(my_dict.low_range)+"-$"+Math.round(my_dict.high_range);
                }
            }
          });
          fetch("https://www.insuremystock.com/options/range/"+table_list[i]['symbol']+"/?days=14")
          .then(d => d.text())
          .then(function(d) {

              var my_dict = JSON.parse(d);
              for (var k = 0; k < table_list.length; k++)
              {
                  if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                  {
                      table_list[k].range_2wk = "$"+Math.round(my_dict.low_range)+"-$"+Math.round(my_dict.high_range);
                  }
              }
            });
            fetch("https://www.insuremystock.com/options/range/"+table_list[i]['symbol']+"/?days=21")
            .then(d => d.text())
            .then(function(d) {

                var my_dict = JSON.parse(d);
                for (var k = 0; k < table_list.length; k++)
                {
                    if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                    {
                        table_list[k].range_3wk = "$"+Math.round(my_dict.low_range)+"-$"+Math.round(my_dict.high_range);
                    }
                }
              });


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
          <th>1Wk</th>
          <th>2Wk</th>
          <th>3wk</th>
        </tr>
    </thead>
    <tbody>
        {#each table_list as { symbol,range_1wk,range_2wk,range_3wk}, i}
            <tr class="bullish">
                <td>{symbol}</td>
                <td>{range_1wk}</td>
                <td>{range_2wk}%</td>
                <td>{range_3wk}</td>
            </tr>

        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data()}>
    Refresh
</button>
