<style>
body {
        max-width:80rem;
        margin:0 auto;
    }
	figure {
		margin: 0 0 1em 0;
	}
	img {
		width: 100%;
		margin: 0 0 1em 0;
	}
</style>

<svelte:head>

</svelte:head>
<script>
import {Button,Container,Row,Col,Card,Modal} from 'svelte-chota';
function openModalPayment() {
  window.open('https://paypal.me/metolabs/3','_blank');
  modal_open = false
}
function openModalSignup() {
  window.open('https://oracled.mailchimpsites.com/','_blank');
  modal_open = false
}
</script>

<h1 class="is-center">Pricing</h1>
<div class="row">
    <div class="col-4 card">
      <header>
        <h4>Free</h4>
      </header>
      10 free skills on
      <ul>
          <li>Stocks</li>
          <li>Options</li>
          <li>WSB Sentiment</li>
      </ul>
      <br>
      <footer class="is-center">
         <Button primary on:click={openModalSignup}>Sign up</Button>
      </footer>
    </div>
    <div class="col-4 card bg-light">
      <header>
        <h4>Amateur:<br> $6/Mo or $60/yr</h4>
      </header>
      Personalized stock lists
      Extra skills like
      <ul>
          <li>Twitter Sentiment</li>
          <li>More coming soon..</li>
      </ul>
      <footer class="is-center">
         <Button primary on:click={openModalSignup}>Sign up</Button>
      </footer>
    </div>
    <div class="col-4 card">
      <header>
        <h4>Professional:</h4>
      </header>
      Why don't you want to pay thousands for bloomberg?
      If you are really done with them call us and maybe we can do something for you
      <br><br><br>
      <footer class="is-center">
         <Button primary on:click={openModalSignup}>Sign up</Button>
      </footer>
    </div>

</div>
