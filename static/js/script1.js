/* for time and date */
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

 // Update every second
updateDateTime(); // Initial call to display immediately
/* for time and date end */

/* for appendchild test
const addButton = document.querySelector(".add_Button"); // Selecting the ADD button
const specificTask = document.getElementById("txtTask").value;
    const datetime = document.getElementById("party").value;

    if (!specificTask || !datetime) {
        alert("Please fill in all fields.");
       // return;
    }

    // Create a new row with the correct data
    const newRow = `
        <tr>
            <td>${new Date().toLocaleString()}</td>
            <td>0</td>
            <td>${specificTask}</td>
            <td>${datetime}</td>
            <td>
                <button class="done_btn">Done</button>
                <button class="edit_btn">Edit</button>
                <button class="remove_btn">Remove</button>
                <button class="clear_btn">Clear</button>
            </td>
        </tr>`;

    // Append row to tbody
    tbodyEl.innerHTML += newRow;
}

// Attach event listener to the ADD button
addButton.addEventListener("click", onAddWebsite);
*/
function addTask()
{
let textinp = $('add_task').value;
const node = document.createElement("td");

// Create a text node:
const textnode = document.createTextNode(textinp);

// Append the text node to the "li" node:
node.appendChild(textnode);

// Append the "li" node to the list:
document.getElementById("content_body").appendChild(node);
}