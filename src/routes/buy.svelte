<svelte:head>
	<title>Buy</title>
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
    let symbol_list = ["LBRDK","IAC","TWTR","SE","MELI","GME","TSLA","AMC","PLTR","SPY"];
    let table_dict= {};
    let table_array=[];
    for(var i = 0; i < symbol_list.length; i++)
    {
        //table_list.push({"symbol":symbol_list[i],"buy_rating":"NA","kelly":"NA","range":"NA","prob_up":"NA"});
        table_dict[symbol_list[i].toUpperCase()] = {"buy_rating":"NA","kelly":"NA","range":"NA","prob_up":"NA"}
    }
    function compare( a, b ) {
      if ( a[1].buy_rating < b[1].buy_rating ){
        return -1;
      }
      if ( a[1].buy_rating > b[1].buy_rating ){
        return 1;
      }
      return 0;
    }
    function get_portfolio_data() {
        for(const sym in table_dict )
        {
            fetch("https://www.insuremystock.com/options/range/"+sym)
            .then(d => d.text())
            .then(function(d) {
                var my_dict = JSON.parse(d);
                console.log(my_dict);
                var my_key = my_dict.symbol.toUpperCase();
                table_dict[my_key].range = "$"+Math.round(my_dict.low_range)+"-$"+Math.round(my_dict.high_range);
                table_dict[my_key].prob_up = Math.round(my_dict.prob_up*100);
              });

              fetch("https://www.insuremystock.com/options/kelly/"+sym)
              .then(d => d.text())
              .then(function(d) {
                  var my_dict = JSON.parse(d);
                  var my_key = my_dict.symbol.toUpperCase();
                  table_dict[my_key].kelly = (my_dict.kelly*100).toFixed(2);
                });
                fetch("https://www.insuremystock.com/options/prob_sigma/"+sym+"?days=7&sigma=0.5")
                .then(d => d.text())
                .then(function(d) {
                    var my_dict = JSON.parse(d);
                    var my_key = my_dict.symbol.toUpperCase();
                    table_dict[my_key].buy_rating = (my_dict.norm_prob_up*100).toFixed(2);
                  });
        }
        //table_dict.sort(compare);

    }

</script>

<h1>Portfolio at a glance</h1>

<table class="striped">

    <thead>
        <tr>
          <th class="emphasis">Symbol</th>
          <th class="emphasis">BuyRating</th>
          <th class="emphasis">$ to invest</th>
          <th class="no-emphasis">Range</th>
          <th class="no-emphasis">Prob↑</th>

        </tr>
    </thead>
    <tbody>
        {#each Object.entries(table_dict) as [symbol,my_obj]}
        {#if my_obj.buy_rating>50}
            <tr class="bullish">
                <td class="emphasis">{symbol}</td>
                <td class="emphasis">{my_obj.buy_rating}</td>
                <td class="emphasis">${my_obj.kelly}</td>
                <td class="no-emphasis">{my_obj.range}</td>
                <td class="no-emphasis">{my_obj.prob_up}%</td>
            </tr>
            {:else}
            <tr class="bearish">
                <td class="emphasis">{symbol}</td>
                <td class="emphasis">{my_obj.buy_rating}</td>
                <td class="emphasis">${my_obj.kelly}</td>
                <td class="no-emphasis">{my_obj.range}</td>
                <td class="no-emphasis">{my_obj.prob_up}%</td>
            </tr>
            {/if}
        {/each}
    </tbody>
</table>
<br>
<button class="pull-left button primary" on:click={get_portfolio_data()}>
    Refresh
</button>
