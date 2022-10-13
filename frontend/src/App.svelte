<script>
  import { Router, Link, Route, navigate } from "svelte-routing";
  import { onDestroy } from "svelte";
  import Home from "./pages/Home.svelte";
  import Login from "./pages/Login.svelte";
  import Signup from "./pages/Signup.svelte";
  import Profile from "./pages/Profile.svelte";
  import UserStore from "./stores/UserStore.js";

  export let url = "";

  const login = async (e) => {
    await fetch("http://localhost:8000/movies/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({
        username: e.detail.username,
        password: e.detail.password,
      }),
    });
    console.log("login");
    console.log(e.detail.username, e.detail.password);
    await navigate("/profile", { replace: true });
  };

  const signup = async (e) => {
    await fetch("http://localhost:8000/movies/signup/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: e.detail.username,
        first_name: e.detail.first_name,
        last_name: e.detail.last_name,
        email: e.detail.email,
        password: e.detail.password,
      }),
    });
    console.log(e.detail.username, e.detail.first_name);
    console.log("signup");

    await navigate("/login", { replace: true });
  };

  const datiutente = async () => {
    const response = await fetch("http://localhost:8000/movies/profile/", {
      headers: { "Content-Type": "application/json" },
      credentials: "include",
    });

    const content = await response.json();
    //console.log(content);
    $UserStore = {
      username: content.username,
      first_name: content.first_name,
      last_name: content.last_name,
      email: content.email,
    };
    console.log("USERPAGE");
    console.log($UserStore);
  };

  const logout = async () => {
    const response = await fetch("http://localhost:8000/movies/logout/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
    });

    let res = await response.json();

    $UserStore = {
      username: null,
      first_name: null,
      last_name: null,
      email: null,
    };
    console.log("logout user");
    console.log($UserStore);

    await navigate("/login", { replace: true });
  };
</script>

<Router {url}>
  {#if $UserStore.username}
    <h2>Logged:{$UserStore.username}</h2>
  {/if}
  <nav>
    <Link to="/">Home</Link>

    {#if $UserStore.username}
      <Link to="/profile">Profile</Link>
      <button on:click={logout}>Logout</button>
    {:else}
      <Link to="/login">Login</Link>
      <Link to="/signup">Signup</Link>
    {/if}
  </nav>
  <h1>MoviesApp</h1>
  <div>
    <Route path="/"><Home /></Route>
    <Route path="/login"><Login on:login={login} /></Route>
    <Route path="/signup"><Signup on:signup={signup} /></Route>
    <Route path="/profile"
      ><Profile $UserStore on:datiutente={datiutente} /></Route
    >
  </div>
</Router>
