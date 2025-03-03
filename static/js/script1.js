/* for time and date */
 // Initial call to display immediately
/* for time and date end */


  
   // Update every second
   

function addTask()
{
    function updateDateTime() {
        const now = new Date();
        const options = { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric', 
            hour: '2-digit', 
            minute: '2-digit', 
            second: '2-digit' 
        };
        document.getElementById('datetime').textContent = now.toLocaleDateString('en-US', options);
      }
let textinp = document.getElementById('add_task').value;
const node = document.createElement("td");
if (textinp.trim() === "") {
    alert("Please enter a task.");
    return;
}
 // Create table row
 const row = document.createElement("tr");
 const cell = document.createElement("td");
 // Create a text node
 const textnode = document.createTextNode(textinp);

 // Append text node to td
 window.onload = function() {
   document.getElementById("datetime").innerHTML = updateDateTime();        
};

cell.appendChild(updateDateTime());
 cell.appendChild(textnode);
 row.appendChild(cell);

 // Append row to table body
 document.getElementById("content_body").appendChild(row);

 // Clear input field after adding
 document.getElementById('add_task').value = "";
}