document.addEventListener("DOMContentLoaded", function() {
  const name = "Joshua Saculo";
  let index = 0;
  let typingElement = document.getElementById("typing");

  function typeEffect() {
      if (index < name.length) {
          typingElement.innerHTML += name.charAt(index);
          index++;
          setTimeout(typeEffect, 150);
      } else {
          setTimeout(() => {
              typingElement.innerHTML = "";
              index = 0;
              typeEffect();
          }, 2000);
      }
  }

  typeEffect();
});