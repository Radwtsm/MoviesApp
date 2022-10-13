<script>
  import { createEventDispatcher } from "svelte";

  let dispatch = createEventDispatcher();

  let username = "",
    first_name = "",
    last_name = "",
    email = "",
    password = "";

  const handleSignup = () => {
    const userdata = {
      username,
      first_name,
      last_name,
      email,
      password,
    };
    dispatch("signup", userdata);
  };
</script>

<form on:submit|preventDefault={handleSignup}>
  <h1 class="h3 mb-3 fw-normal">Please register</h1>

  <input
    bind:value={username}
    class="form-control"
    placeholder="username"
    required
  />
  <input
    bind:value={first_name}
    class="form-control"
    placeholder="firstname"
    required
  />
  <input
    bind:value={last_name}
    class="form-control"
    placeholder="lastname"
    required
  />

  <input
    bind:value={email}
    type="email"
    class="form-control"
    placeholder="Email"
    required
  />

  <input
    bind:value={password}
    type="password"
    class="form-control"
    placeholder="Password"
    required
  />

  <button class="w-100 btn btn-lg btn-primary" type="submit">Submit</button>
</form>
