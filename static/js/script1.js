/* for time and date */
 // Initial call to display immediately
/* for time and date end */


  
   // Update every second
   



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
