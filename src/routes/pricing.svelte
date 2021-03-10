<style>
	figure {
		margin: 0 0 1em 0;
	}
	img {
		width: 100%;
		margin: 0 0 1em 0;
	}
</style>

<svelte:head>
	<title>Pricing</title>
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
      Institutional Grade analysis in a jiffy. Includes:
      <ul>
          <li>Stocks</li>
          <li>Options</li>
          <li>Sentiment</li>
      </ul>
      <footer class="is-center">
         <Button primary on:click={openModalSignup}>Sign up</Button>
      </footer>
    </div>
    <div class="col-4 card bg-light">
      <header>
        <h4>Basic: $3/Month</h4>
      </header>
      <strong>Free+</strong>
      <ul>
         <li>Buy Ideas</li>
         <li> What to sell</li>
         <li>Risk Management</li>
      </ul>
      <br>
      <footer class="is-center">
         <Button primary on:click={openModalPayment}>Sign up</Button>
      </footer>
    </div>
    <div class="col-4 card">
      <header>
        <h4>Advanced: $30/Month</h4>
      </header>
      <strong>Basic+</strong>
      <ul>
         <li>Custom Screening</li>
         <li>Custom skills</li>
         <li>One 30 min call with our analysts</li>
      </ul>
      <footer class="is-center">
         <Button primary on:click={openModalPayment}>Sign up</Button>
      </footer>
    </div>
    <div class="col-3 "></div>
    <div class="col-6 card">
      <header>
        <h4>Enterprise: $Bespoke</h4>
      </header>
      <strong>Advanced+</strong>
      <ul>
         <li>Custom alerts</li>
         <li>API Integration</li>
         <li>Monthly 30 min call with our analysts</li>
      </ul>
      <footer class="is-center">
         <Button primary on:click={openModalPayment}>Sign up</Button>
      </footer>
    </div>

</div>
