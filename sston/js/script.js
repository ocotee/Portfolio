const bookBtn = document.querySelector(".bookmark-btt");
const section = document.querySelector("section");
const label = document.querySelector("label");

bookBtn.addEventListener("click", () => {
  section.style.left = 0;
  label.style.opacity = 0;
});

bookBtn.addEventListener("blur", () => {
  section.style.left = "-200px";
  label.style.opacity = 1;
});

// let start = document.querySelector(".start");
// let end = document.querySelector(".end");
// let btn = document.querySelector(".btn");

// btn.addEventListener("click", () => {
//   location.href = `https://map.kakao.com/?map_type=TYPE_MAP&target=car&rt=%2C%2C523953%2C1084098&rt1=${start.value}&rt2=${end.value}&rtIds=%2C&rtTypes=%2C`;
// });

//경로 찾기로 가기 연결 부분
function Page() {
  window.location.href = "index.html";
}
