<svelte:head>
	<title>Buy</title>
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
    import { stores } from '@sapper/app';
    const { preloading, page, session } = stores();

	let symbol_list = ["AAPL","TSLA"];
    //let table_dict= {};
    let table_list=[];
    let table_show = [];
    for(var i = 0; i < symbol_list.length; i++)
    {
        table_list.push({"symbol":symbol_list[i].toUpperCase(),"range":"NA","prob_up":"NA","prob_down":"NA"});
    }
    function compare( a, b ) {
      if ( parseFloat(a.prob_up) > parseFloat(b.prob_up) ){
        return -1;
      }
      if ( parseFloat(a.prob_up) < parseFloat(b.prob_up)){
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
                        table_list[k].prob_up = Math.round(my_dict.prob_up*100);
                        table_list[k].prob_down = Math.round(my_dict.prob_down*100);
                    }
                }
              });

              fetch("https://www.insuremystock.com/options/range/"+table_list[i]['symbol'])
              .then(d => d.text())
              .then(function(d) {
                  var my_dict = JSON.parse(d);
                  for (var k = 0; k < table_list.length; k++)
                  {
                      if (table_list[k].symbol == my_dict.symbol.toUpperCase())
                      {
                        table_list[k].range = '<a class="text-white bg-primary bd-dark" href="https://fatneo.com/?cmd=put&symbol='+my_dict.symbol.toUpperCase()+'>sell put</a>$'+Math.round(my_dict.low_range)+'-$'+Math.round(my_dict.high_range)+'<a class="text-white bg-primary bd-dark" href="https://fatneo.com/?cmd=call&symbol='+my_dict.symbol.toUpperCase()+'>sell call</a>';
                      }
                }
                });
        }
        table_list = table_list.sort(compare);
    }

/*get_portfolio_data();*/

</script>

<h1>Picks for daily spread</h1>

<table class="striped">

    <thead>
        <tr>
          <th class="emphasis">Symbol</th>
          <th class="emphasis">Range</th>
          <th class="no-emphasis">Windfall%🔱</th>
          <th class="no-emphasis">Doom%🔱</th>

        </tr>
    </thead>
    <tbody>
        {#each table_list as { symbol,range,prob_up,prob_down}, i}
        {#if prob_up>prob_down}
            <tr class="bullish">
                <td class="emphasis"> <a  href="/?symbol={symbol}&cmd=call">{symbol}</a></td>
                <td class="emphasis">{@html range}</td>
                <td class="no-emphasis">{prob_up}%</td>
                <td class="no-emphasis">{prob_down}%</td>
            </tr>
            {:else}
            <tr class="bearish">
            <td class="emphasis"> <a  href="/?symbol={symbol}&cmd=call">{symbol}</a></td>
            <td class="emphasis">{@html range}</td>
            <td class="no-emphasis">{prob_up}%</td>
            <td class="no-emphasis">{prob_down}%</td>
            </tr>
            {/if}
        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data}>
    Fetch/Sort
</button>
<br><br><br>
* - Optimal allocation amounts for a $100 portfolio
<br>
🔱 - Windfall(Doom) is probability that the stock moves up(down) 10% in a week
