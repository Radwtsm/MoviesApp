<script>
  import { createEventDispatcher } from "svelte";

  let dispatch = createEventDispatcher();

  let username = "",
    password = "";

  const handleLogin = () => {
    const user = {
      username,
      password,
    };
    dispatch("login", user);
  };
</script>

<form on:submit|preventDefault={handleLogin}>
  <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

  <input
    bind:value={username}
    type="text"
    class="form-control"
    placeholder="username"
    required
  />

  <input
    bind:value={password}
    type="password"
    class="form-control"
    placeholder="Password"
    required
  />

  <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
</form>
