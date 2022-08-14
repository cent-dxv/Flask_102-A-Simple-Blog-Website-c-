// document.getElementById("like_post").addEventListener("click", function(){alert("csdv")});

function like(post_id) {
  no_of_like = document.getElementById("no_of_like" + post_id);
  fetch("like_posts/" + post_id)
    .then((response) => response.json())
    .then((data) => no_of_like.innerHTML = data["likes"] );
   
    // no_of_like.innerHTML = await data["likes"]
}
