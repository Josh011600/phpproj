
const numbers = ["45", "4", "9", "16", "25"];

let txt = "";
myFunction();
document.getElementById("demo").innerHTML = txt;

function myFunction() {
  for(let i=0;i<=3;i++)
  {
    txt +=document.getElementById("demo").innerHTML = numbers[i] + '<br>';
  }
}
