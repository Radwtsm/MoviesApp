<script>
  import { onMount } from "svelte";

  import Slider from "./lib/Slider.svelte";

  let movielist = [];
  onMount(() => {
    fetch("http://127.0.0.1:8000/movies/")
      .then((response) => response.json())
      .then((data) => (movielist = data));
  });
</script>

<Slider {movielist} />
