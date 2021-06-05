const buddy = document.querySelector(".buddy svg");

// Only add the class if Buddy isn't sad
setInterval(() => {
  if (!document.querySelector("#sad:checked")) buddy.classList.add("wink");
}, 5000);

// Remove the wink class to reset the animation after it ends
buddy.addEventListener("animationend", () => {
  buddy.classList.remove("wink");
});