/* for time and date */
 // Initial call to display immediately
/* for time and date end */


  
   // Update every second
   

<<<<<<< HEAD
=======
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
>>>>>>> 0a66c6f1cf15c1ec584743c28583eb50dfdaea34

    let taskId = 1; // Unique task ID

        function addTask() {
            const tableBody = document.querySelector("#taskTable tbody");

            // Create row
            const row = document.createElement("tr");

            // Get today's date
            const today = new Date().toISOString().split('T')[0];

            // Create table columns
            row.innerHTML = `
                <td>${today}</td>
                <td>${taskId}</td>
                <td><input type="text" placeholder="Enter task"></td>
                <td><input type="datetime-local"></td>
                <td>
                    <button onclick="editTask(this)">Edit</button>
                    <button onclick="removeTask(this)">Remove</button>
                </td>
            `;

            // Append row to table
            tableBody.appendChild(row);
            taskId++; // Increment task ID
        }

        function editTask(button) {
            const row = button.closest("tr");
            const taskInput = row.querySelector("input[type='text']");
            taskInput.focus();
        }

        function removeTask(button) {
            const row = button.closest("tr");
            row.remove();
        }
