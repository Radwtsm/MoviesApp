<script>
  import { onMount } from "svelte";
  import UserStore from "../stores/UserStore";
  import { createEventDispatcher } from "svelte";

  let dispatch = createEventDispatcher();

  const fetchdati = () => {
    console.log($UserStore);
    dispatch("datiutente");
  };

  onMount(fetchdati);
</script>

{#if $UserStore.username}
  <h2>User</h2>
  <ul>
    <li>{$UserStore.username}</li>
    <li>{$UserStore.first_name}</li>
    <li>{$UserStore.last_name}</li>
    <li>{$UserStore.email}</li>
  </ul>
{:else}
  <h1>Non Loggato</h1>
{/if}

<style>
  ul {
    list-style-type: none;
  }
</style>
