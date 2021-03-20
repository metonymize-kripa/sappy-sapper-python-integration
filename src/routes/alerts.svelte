<script>
import { user } from "./store.js";
</script>

<style>
  .content {
    display: grid;
    grid-template-columns: 20% 80%;
    grid-column-gap: 10px;
  }
</style>

<h1>Form</h1>
<form class="content">
  <label>Name</label>
  <input type="text" bind:value={$user.name} />
  <label>E-mail</label>
  <input type="text" bind:value={$user.email} />
  <label>Tickers to track</label>
  <input type="text" bind:value={$user.tickers} />
</form>
<p>
	{JSON.stringify($user, 0, 2)}</p>
<h2 style='color:black;'>AAPL : <a style='font-size:1rem;border:1px solid black;' href='https://fatneo.com/?cmd=put&symbol=AAPL'>sell put</a>114-126 <a style='font-size:1rem;border:1px solid black;' href='https://fatneo.com/?cmd=call&symbol=AAPL'>sell call</a>. Windfall Chance 7%</h2><h2 style='color:black;'>TSLA : <a style='font-size:1rem;border:1px solid black;' href='https://fatneo.com/?cmd=put&symbol=TSLA'>sell put</a>577-733 <a style='font-size:1rem;border:1px solid black;' href='https://fatneo.com/?cmd=call&symbol=TSLA'>sell call</a>. Windfall Chance 24%</h2>
