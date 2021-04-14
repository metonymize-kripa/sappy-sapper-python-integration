<svelte:head>
	<title>Watch</title>
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

	let symbol_list = ["BTC-USD","ETH-USD","DOGE-USD","BNB-USD","XRP-USD","LTC-USD"];
    //let table_dict= {};
    let table_list=[];
    let table_show = [];
    for(var i = 0; i < symbol_list.length; i++)
    {
        table_list.push({"symbol":symbol_list[i],"price":"NA","range":"NA","volume_pct":"NA","wedge":"NA","ascending_triangle ":"NA"});
    }
	function currencyFormat(num,decimals) {
	 return num.toFixed(decimals).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
   }

    function get_portfolio_data() {

        for(var i = 0; i < table_list.length; i++)
        {
            fetch("https://www.insuremystock.com/crypto/range/"+table_list[i]['symbol'])
            .then(d => d.text())
            .then(function(d) {
                var my_dict = JSON.parse(d);
                for (var k = 0; k < table_list.length; k++)
                {
                    if (table_list[k].symbol == my_dict.symbol.toUpperCase())
                    {
					   if (my_dict.price > 100)
					   	{
							table_list[k].price = Math.round(my_dict.price);
							table_list[k].range = '$'+currencyFormat(my_dict.low_range,0)+" - $"+currencyFormat(my_dict.high_range,0);
						}
					   else if (my_dict.price > 10)
					   {
					   		table_list[k].price = (my_dict.price).toFixed(2);
							table_list[k].range = '$'+currencyFormat(my_dict.low_range,2)+" - $"+currencyFormat(my_dict.high_range,2);
						}
					   else if (my_dict.price > 2)
					   {
						   	table_list[k].price = (my_dict.price).toFixed(3);
							table_list[k].range = '$'+currencyFormat(my_dict.low_range,3)+" - $"+currencyFormat(my_dict.high_range,3);
						}
						else if (my_dict.price > 0.1)
						{
	  						table_list[k].price = (my_dict.price).toFixed(4);
							table_list[k].range = '$'+currencyFormat(my_dict.low_range,4)+" - $"+currencyFormat(my_dict.high_range,4);
					    }
						else
						{
							table_list[k].price = (my_dict.price).toFixed(6);
							table_list[k].range = '$'+currencyFormat(my_dict.low_range,6)+" - $"+currencyFormat(my_dict.high_range,6);
						}
						table_list[k].volume_pct = (my_dict.today_volume/my_dict.avg_10d_volume).toFixed(2);
						table_list[k].wedge = (Math.random()*100).toFixed(2);
						table_list[k].ascending_triangle = (Math.random()*100).toFixed(2)

                    }
                }
              });
        }

    }

/*get_portfolio_data();*/

</script>

<h1>Picks for daily spread</h1>

<table class="striped">

    <thead>
        <tr>
          <th class="emphasis">Symbol</th>
          <th class="no-emphasis">Price</th>
          <th class="no-emphasis">Range</th>
          <th class="no-emphasis">Vol🔱</th>
		  <th class="emphasis">Wedge</th>
		  <th class="emphasis">🔼📐</th>

        </tr>
    </thead>
    <tbody>
        {#each table_list as {symbol,price,range,volume_pct,wedge,ascending_triangle}, i}
            <tr >
                <td class="emphasis"> {symbol}</td>
                <td class="no-emphasis">${price}</td>
                <td class="no-emphasis">{range}</td>
                <td class="no-emphasis">{volume_pct}</td>
				<td class="emphasis">{wedge}%</td>
				<td class="emphasis">{ascending_triangle}%</td>
            </tr>

        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data}>
    Fetch/Sort
</button>
<br><br><br>
🔼📐- Chance of Ascending Triangle Forming
<br>
🔱 - Today's volume as a ratio of 10 day average
