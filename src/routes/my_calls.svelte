<svelte:head>
	<title>My Calls </title>
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
        table_list.push({"symbol":symbol_list[i],"call_1wk":"NA","call_2wk":"NA","call_3wk":"NA"});
    }
    function get_portfolio_data() {
        for(var i = 0; i < table_list.length; i++)
        {
        fetch("https://www.insuremystock.com/options/call_trades/"+table_list[i]['symbol'])
        .then(d => d.text())
        .then(function(d) {

            var my_dict = JSON.parse(d);
            for (var k = 0; k < table_list.length; k++)
            {
                if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                {
                    if (my_dict.best_call.strike > 0)
                        table_list[k].call_1wk = my_dict.best_call.strike+"c exp "+my_dict.best_call.expiry+" @ "+my_dict.best_call.bid+"-"+my_dict.best_call.ask;
                }
            }
          });
          fetch("https://www.insuremystock.com/options/call_trades/"+table_list[i]['symbol']+"/?days=14")
          .then(d => d.text())
          .then(function(d) {

              var my_dict = JSON.parse(d);
              for (var k = 0; k < table_list.length; k++)
              {
                  if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                  {
                      if (my_dict.best_call.strike > 0)
                          table_list[k].call_1wk = my_dict.best_call.strike+"c exp "+my_dict.best_call.expiry+" @ "+my_dict.best_call.bid+"-"+my_dict.best_call.ask;
                  }
              }
            });
            fetch("https://www.insuremystock.com/options/call_trades/"+table_list[i]['symbol']+"/?days=21")
            .then(d => d.text())
            .then(function(d) {

                var my_dict = JSON.parse(d);
                for (var k = 0; k < table_list.length; k++)
                {
                    if (table_list[k].symbol.toUpperCase() == my_dict.symbol.toUpperCase())
                    {
                        if (my_dict.best_call.strike > 0)
                            table_list[k].call_1wk = my_dict.best_call.strike+"c exp "+my_dict.best_call.expiry+" @ "+my_dict.best_call.bid+"-"+my_dict.best_call.ask;
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
        {#each table_list as { symbol,1Wk,2Wk,3Wk}, i}
            <tr class="bearish">
                <td>{symbol}</td>
                <td>{1Wk}</td>
                <td>{2Wk}%</td>
                <td>{3Wk}</td>
            </tr>

        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data()}>
    Refresh
</button>
