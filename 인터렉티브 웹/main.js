let menuBtn = document.querySelector(".menu-btn");
let closeBtn = document.querySelector(".close-btn");
let navigation = document.querySelector(".navigation");

menuBtn.addEventListener("click", () => {
  navigation.classList.add("active");
});

closeBtn.addEventListener("click", () => {
  navigation.classList.remove("active");
});

window.addEventListener("scroll", () => {
  let header = document.querySelector("header");

  let scrollTop = document.body.scrollTop;
  let OffsetY = window.pageYOffset;

  header.classList.toggle("down", OffsetY != scrollTop);
});
