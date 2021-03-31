<svelte:head>
	<title>Social Trader</title>
</svelte:head>
<h1>💎 Oracle, How much should I buy?</h1>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<!--<script context="module">
	export async function preload({ params }) {
    console.log(params);
	let slug = params.slug;
	return {slug};
	}
</script>
-->
<script>
import { stores } from '@sapper/app';
const { preloading, page } = stores();
const { host, path, params, query } = $page;
//export let slug;
let ticker = params.slug.toUpperCase();
let portfolio_size = 100;
let my_kelly = 0;
let api_output = {};
let post_url = "https://social.oracled.com/stocks/"
let post_title = "How%20much%20should%20you%20spend%20on:%20"

function calculateKelly() {
    fetch("https://www.insuremystock.com/options/kelly/"+ticker)
        .then(d => d.text())
        .then(d => {
                    api_output = JSON.parse(d);
                    console.log(api_output);
                    my_kelly = api_output.kelly2;

        });
}
function goback(){
}

function currencyFormat(num,decimals) {
  return num.toFixed(decimals).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}

if (process.browser)
    calculateKelly();

function updateClipboard(newClip) {
  navigator.clipboard.writeText(newClip).then(function() {

    window.open("https://www.robinhood.com/stocks/"+ticker);
  }, function() {
    /* clipboard write failed */
  });
}
</script>
<style>
	figure, img {
		width: 100%;
		margin: 0;
	}
    .fa {
      padding: 1rem;
      font-size: 1.5rem;
      width: 4rem;
      text-align: center;
    }
    .fa:hover {
        opacity: 0.7;
    }
    .fa-twitter {
      background: #55ACEE;
      color: white;
    }
    .fa-google {
      background: #dd4b39;
      color: white;
    }
    .fa-linkedin {
      background: #007bb5;
      color: white;
    }
    .fa-reddit {
      background: #ff5700;
      color: white;
    }
    .fa-whatsapp {
      background: #43d854;
      color: white;
    }
    .fa-envelope {
      background: #3f4144;
      color: white;
    }
</style>

<div class="row">
    <div class="card col-8 bg-light" >
      <header>
        <h4>Oracle says do not invest more than:</h4>
      </header>
        <h2 style="margin-bottom:0;">${currencyFormat(my_kelly*portfolio_size,2)} in {ticker}</h2>
        My Portfolio Size (${currencyFormat(portfolio_size,0)}):
        <input bind:value={portfolio_size} type="range" min="0" max="10000" step="100" style="width:50%;">
        <br>
        <button class="text-white bg-dark" style="margin:0 0 2rem 0 ;padding:0.5rem; font-size:1.25rem;" on:click={updateClipboard((my_kelly*portfolio_size).toFixed(2))}>copy and trade@RH</button>
        <br>
        <a href="https://reddit.com/submit?url={post_url}{ticker}&title={post_title}{ticker}" class="fa fa-reddit"></a>
        <a href="https://twitter.com/share?url={post_url}{ticker}&text={post_title}{ticker}&hashtags=kelly,fatneo" class="fa fa-twitter"></a>
        <a href="https://api.whatsapp.com/send?text={post_title}{ticker} {post_url}{ticker}" class="fa fa-whatsapp"></a>
        <a href="https://mail.google.com/mail/u/1/?fs=1&su={post_title}{ticker}&tf={post_url}/{ticker}" class="fa fa-envelope"></a>
    </div>

</div>
