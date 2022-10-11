<script>
  import { Router, Link, Route } from "svelte-routing";
  import Homepage from "./Homepage.svelte";

  export let url = "";
</script>

<h1>MoviesApp</h1>
<Router {url}>
  <nav>
    <Link to="/">Home</Link>
  </nav>
  <div>
    <Route path="/"><Homepage /></Route>
  </div>
</Router>

<style>
  h1 {
    color: #5bc0be;
  }
</style>
