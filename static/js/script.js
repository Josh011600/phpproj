document.addEventListener("DOMContentLoaded", function() {
  const name = "Joshua Saculo";
  let index = 0;
  let typingElement = document.getElementById("typing");

  if (!typingElement) {
    console.error("Element with id 'typing' not found!");
    return;
  }

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
          }, 2000); // Reset after 2 seconds
      }
  }

  typeEffect();
});
