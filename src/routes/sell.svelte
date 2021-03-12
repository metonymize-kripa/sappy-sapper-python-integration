<svelte:head>
	<title>Sell</title>
</svelte:head>
<style>
body {
        max-width:80rem;
        margin:0 auto;
    }
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
    let symbol_list = ["IAC", "PLTR", "BB","CVNA","GME", "SKT", "AMC"];
    let table_list= [];
    let table_show = [];
    for(var i = 0; i < symbol_list.length; i++)
    {
        table_list.push({"symbol":symbol_list[i].toUpperCase(),"kelly":"NA","prob_down":"NA"});
        //table_dict[symbol_list[i].toUpperCase()] = {"kelly":"NA","prob_down":"NA"}
    }
    function compare( a, b ) {
      if ( parseFloat(a.kelly) < parseFloat(b.kelly) ){
        return -1;
      }
      if ( parseFloat(a.kelly) > parseFloat(b.kelly)){
        return 1;
      }
      return 0;
    }
    function get_portfolio_data() {

        for(var i = 0; i < table_list.length; i++)
        {
            fetch("https://www.insuremystock.com/options/prob_pct/"+table_list[i]['symbol']+"?days=7&percent=10")
            .then(d => d.text())
            .then(function(d) {
                var my_dict = JSON.parse(d);
                for (var k = 0; k < table_list.length; k++)
                {
                    if (table_list[k].symbol == my_dict.symbol.toUpperCase())
                    {
                        table_list[k].prob_down = Math.round(my_dict.prob_down*100);
                    }
                }
              });

              fetch("https://www.insuremystock.com/options/kelly/"+table_list[i]['symbol'])
              .then(d => d.text())
              .then(function(d) {
                  var my_dict = JSON.parse(d);
                  for (var k = 0; k < table_list.length; k++)
                  {
                      if (table_list[k].symbol == my_dict.symbol.toUpperCase())
                      {
                          table_list[k].kelly = (my_dict.kelly2*100).toFixed(2);
                      }
                }
                });
        }
        table_list = table_list.sort(compare);
    }

/*get_portfolio_data();*/
</script>

<h1>Candidates </h1>

<table class="striped">

    <thead>
        <tr>
            <th class="emphasis">Symbol</th>
            <th class="emphasis">Max $ allowed 🔱</th>

        </tr>
    </thead>
    <tbody>
        {#each table_list as { symbol,kelly,prob_down}, i}
        {#if kelly>0}
            <tr class="bullish">
                <td class="emphasis">{symbol}</td>
                <td class="emphasis">${kelly}</td>

            </tr>
            {:else}
            <tr class="bearish">
                <td>{symbol}</td>
                <td>${kelly}</td>

            </tr>
            {/if}
        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data}>
    Sort
</button>
<br><br>
🔱 - Do not allocate more than this in a $100 portfolio.
