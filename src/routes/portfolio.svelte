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

	let symbol_list = ["AAPL","BIGC","BZUN","GRWG","APHA","AMC","LAC","SNOW","PGNY"];
    //let table_dict= {};
    let table_list=[];
    let table_show = [];
    for(var i = 0; i < symbol_list.length; i++)
    {
        table_list.push({"symbol":symbol_list[i].toUpperCase(),"range":"NA","prob_up":"NA","prob_down":"NA", "color":"bearish"});
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
                        table_list[k].prob_up = '<a class="text-white bg-primary bd-dark" style="margin:1rem; font-size:1.5rem;" href="https://fatneo.com/?cmd=put&symbol='+my_dict.symbol.toUpperCase()+'">put</a>'+Math.round(my_dict.prob_up*100)+'%';
                        table_list[k].prob_down = '<a class="text-white bg-primary bd-dark" style="margin:1rem; font-size:1.5rem;" href="https://fatneo.com/?cmd=call&symbol='+my_dict.symbol.toUpperCase()+'">call</a>'+Math.round(my_dict.prob_down*100)+'%';
                        if (my_dict.prob_up > my_dict.prob_down)
                            table_list[k].color="bullish";
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
                        table_list[k].range = '$'+Math.round(my_dict.low_range)+'-$'+Math.round(my_dict.high_range);
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
        {#each table_list as { symbol,range,prob_up,prob_down,color}, i}

            <tr class="{color}">
                <td class="emphasis"> <a  href="/?symbol={symbol}&cmd=call">{symbol}</a></td>
                <td class="emphasis">{range}</td>
                <td class="no-emphasis">{@html  prob_up}</td>
                <td class="no-emphasis">{@html  prob_down}</td>
            </tr>

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
