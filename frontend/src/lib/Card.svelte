<script>
  import MdFavoriteBorder from "svelte-icons/md/MdFavoriteBorder.svelte";

  let isShowing = false;
  export let moviedata;
</script>

<div
  style="background-image:
  linear-gradient(to bottom, rgba(31, 31, 31, 0.52), rgba(5, 5, 5, 0.73)),
  url('http://127.0.0.1:8000/{moviedata.cover}');"
  class="card-container"
>
  <img src="http://127.0.0.1:8000/{moviedata.thumbnail}" alt="" />
  <div class="top-card">
    <h2>{moviedata.title}</h2>
    <p>{moviedata.release_date}</p>
    <p>
      {#if moviedata.introduction.length > 150}
        {#if isShowing}
          {moviedata.introduction}<span class="text-switch">...less</span>
        {:else}
          {moviedata.introduction.slice(0, 150)}<span class="text-switch"
            >...more</span
          >
        {/if}
      {:else}
        {moviedata.introduction}
      {/if}
    </p>
    <div class="likes">
      <span class="icon"><MdFavoriteBorder /></span>
      <p>{moviedata.likes}</p>
    </div>
  </div>
</div>

<style>
  .likes {
    font-size: 2rem;
    font-weight: bold;
    width: min-content;
    display: flex;
    gap: 2rem;
    justify-content: center;
    align-items: center;
  }

  .icon {
    width: 3rem;
  }

  .text-switch {
    color: gray;
  }

  .card-container {
    -webkit-box-shadow: -1px 6px 12px -2px rgba(0, 0, 0, 0.88);
    box-shadow: -1px 6px 12px -2px rgba(0, 0, 0, 0.88);

    padding: 5rem;
    color: white;
    display: flex;

    justify-content: center;
    align-items: center;
  }

  div {
    border-radius: 20px;
    margin-top: 2rem;
  }
  img {
    max-width: 50%;
    border-radius: 20px;
  }

  .top-card {
    margin: 1rem;
    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;
  }
</style>
