import { writable } from "svelte/store";

const UserStore = writable({
  username: "none",
  first_name: "none",
  last_name: "none",
  email: "none",
});

export default UserStore;
