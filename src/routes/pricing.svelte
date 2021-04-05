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
  window.open('https://us1.list-manage.com/survey?u=cd4eb9eb314b5da2719efa0b6&id=4dd04bd1c1&e=26ea9ce559','_blank');
  modal_open = false
}
</script>

<h1 class="is-center">Pricing</h1>
<div class="row">
    <div class="col-4 card">
      <header>
        <h4>$10/Month</h4>
      </header>
      Cancel any time
      <ul>
          <li>Price range outlook</li>
          <li>Options implied bet sizing</li>
          <li>WSB activity screening</li>
      </ul>
      <br>
      <footer class="is-center">
         <Button primary on:click={openModalSignup}>Sign up</Button>
      </footer>
    </div>
    <div class="col-4 card bg-light">
      <header>
        <h4>$60/Year</h4>
      </header>
      Bespoke Skills list
      <ul>
          <li>Personalized stock lists</li>
          <li>Custom alert screening logic</li>
          <li>More coming soon..</li>
      </ul>
      <footer class="is-center">
         <Button primary on:click={openModalSignup}>Sign up</Button>
      </footer>
    </div>

</div>
