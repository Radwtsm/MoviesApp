<script>
  // Import Swiper Svelte components

  import Card from "./Card.svelte";

  export let movielist;
</script>

{#each movielist as moviedata}
  <Card {moviedata} />
{/each}
