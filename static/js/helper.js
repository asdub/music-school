const link = document.querySelector(".span-alt a");

link.addEventListener("click", clickHandler);

function clickHandler(e) {
  e.preventDefault();
  const href = this.getAttribute("href");
  const offset = document.querySelector(href).offsetTop;
  const offsetTop = offset - 90;

  scroll({
    top: offsetTop,
    behavior: "smooth"
  });
}