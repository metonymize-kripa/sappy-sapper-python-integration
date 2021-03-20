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

