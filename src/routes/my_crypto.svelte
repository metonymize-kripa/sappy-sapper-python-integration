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
        table_list.push({"symbol":symbol_list[i],"price":"NA","range":"NA","volume_pct":"NA","wedge":"NA","ascending_triangle ":"NA","wedge_st":"NA","ascending_triangle_st":"NA"});
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
							table_list[k].price = currencyFormat(my_dict.price,0);
							table_list[k].range = '$'+currencyFormat(my_dict.low_range,0)+" - $"+currencyFormat(my_dict.high_range,0);
						}
					   else if (my_dict.price > 10)
					   {
					   		table_list[k].price = currencyFormat(my_dict.price,2);
							table_list[k].range = '$'+currencyFormat(my_dict.low_range,2)+" - $"+currencyFormat(my_dict.high_range,2);
						}
					   else if (my_dict.price > 2)
					   {
						   	table_list[k].price = currencyFormat(my_dict.price,3);
							table_list[k].range = '$'+currencyFormat(my_dict.low_range,3)+" - $"+currencyFormat(my_dict.high_range,3);
						}
						else if (my_dict.price > 0.1)
						{
	  						table_list[k].price = (my_dict.price).toFixed(4);
							table_list[k].range = '$'+(my_dict.low_range).toFixed(4)+" - $"+(my_dict.high_range).toFixed(4);
					    }
						else
						{
							table_list[k].price = (my_dict.price).toFixed(6);
							table_list[k].range = '$'+(my_dict.low_range).toFixed(6)+" - $"+(my_dict.high_range).toFixed(6);
						}
						table_list[k].volume_pct = (my_dict.today_volume/my_dict.avg_10d_volume).toFixed(2);

						table_list[k].wedge = (my_dict.low_slope - my_dict.high_slope);
                        if ( (my_dict.low_slope > my_dict.high_slope) && my_dict.high_slope <0.0001)
                            table_list[k].wedge += 0.2;
                        table_list[k].wedge = (table_list[k].wedge*1000).toFixed(2);
                        if (table_list[k].wedge <0)
                            table_list[k].wedge = 0;
						else if (table_list[k].wedge > 100)
	                            table_list[k].wedge = 100;

                        if ( my_dict.high_slope <0.01 &&  my_dict.high_slope > 0.01)
                            {
                                if (my_dict.low_slope>0.02)
                                    table_list[k].ascending_triangle = 0.5+my_dict.low_slope*10;
                            }
                        else{table_list[k].ascending_triangle = -1+my_dict.low_slope-my_dict.high_slope;}
                         if (table_list[k].ascending_triangle <0)
                            table_list[k].ascending_triangle = 0;
						else if (table_list[k].ascending_triangle > 1)
							   table_list[k].ascending_triangle = 1;

						table_list[k].wedge_st = (my_dict.low_slope_st - my_dict.high_slope_st);
                        if ( (my_dict.low_slope_st > my_dict.high_slope_st) && my_dict.high_slope_st <0.0001)
                            table_list[k].wedge_st += 0.2;
                        table_list[k].wedge_st = (table_list[k].wedge_st*1000).toFixed(2);
                        if (table_list[k].wedge_st <0)
                            table_list[k].wedge_st = 0;
						else if (table_list[k].wedge_st > 100)
                            table_list[k].wedge_st = 100;

                        if ( my_dict.high_slope_st <0.01 &&  my_dict.high_slope_st > 0.01)
                            {
                                if (my_dict.low_slope_st>0.02)
                                    table_list[k].ascending_triangle_st = 0.5+my_dict.low_slope_st*10;
                            }
                        else{table_list[k].ascending_triangle_st = -1+my_dict.low_slope_st-my_dict.high_slope_st;}
                         if (table_list[k].ascending_triangle_st <0)
                            table_list[k].ascending_triangle_st = 0;
						else if (table_list[k].ascending_triangle_st >1)
							table_list[k].ascending_triangle_st = 1;


                    }
                }
              });
        }

    }
if (process.browser)
        get_portfolio_data();

</script>

<h1>Picks for daily spread</h1>

<table class="striped">

    <thead>
        <tr>
          <th class="emphasis">Symbol</th>
          <th class="no-emphasis">Price</th>
          <th class="no-emphasis">Range🧰</th>
          <th class="no-emphasis">Vol🔱</th>
		  <th class="emphasis">Wedge🏁</th>
		  <th class="emphasis">🔼📐</th>
		  <th class="emphasis">ST Wedge🏁</th>
		 <th class="emphasis">ST 🔼📐</th>
          <th class="no-emphasis">Chart</th>
        </tr>
    </thead>
    <tbody>
        {#each table_list as {symbol,price,range,volume_pct,wedge,ascending_triangle,wedge_st,ascending_triangle_st}, i}

            <tr >
                <a href="https://www.tradingview.com/symbols/{symbol.replace('-','')}" target="_blank" ><td class="emphasis"> {symbol}</td></a>
                <td class="no-emphasis">${price}</td>
                <td class="no-emphasis">{range}</td>
                <td class="no-emphasis">{volume_pct}</td>
				<td class="emphasis">{wedge}%</td>
				<td class="emphasis">{(ascending_triangle*100).toFixed(2)}%</td>
				<td class="emphasis">{wedge_st}%</td>
				<td class="emphasis">{(ascending_triangle_st*100).toFixed(2)}%</td>
				<a href="https://www.tradingview.com/symbols/{symbol.replace('-','')}" target="_blank" ><td class="no-emphasis">Chart</td>
            </tr>


        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data}>
    Fetch/Sort
</button>
<br><br><br>
🧰 - Most likely one week range given past month performance
<br>
🔼📐- Chance that the coin is in Ascending Triangle Formation. Long Term Foramtion (one month)
<br>
🏁 - Chance that the coin is in Downward Wedge Formation. Long Term Foramtion (one month).
<br>
🔱 - Today's volume as a ratio of 10 day average
