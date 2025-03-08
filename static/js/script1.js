let taskId = 1; // Unique task ID

function addTask() {
    const tableBody = document.querySelector("#taskTable tbody");
    const taskInput = document.getElementById("add_task");
    const dateInput = document.getElementById("party");

    // Get values from input fields
    const taskName = taskInput.value.trim();
    const scheduleDate = dateInput.value;
    const today = new Date().toLocaleString(); // Get current date and time

    // Validate input
    if (taskName === "" || scheduleDate === "") {
        alert("Please enter a task and select a date.");
        return;
    }

    // Create row
    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${today}</td>
        <td>${taskId}</td>
        <td>${taskName}</td>
        <td>${scheduleDate}</td>
        <td>
            <button onclick="editTask(this)">Edit</button>
            <button onclick="removeTask(this)">Remove</button>
        </td>
    `;

    // Append row to table
    tableBody.appendChild(row);

    // Clear input fields
    taskInput.value = "";
    dateInput.value = "";

    taskId++; // Increment task ID
}

function editTask(button) {
    const row = button.closest("tr");
    const taskCell = row.children[2];
    const newTaskName = prompt("Edit task:", taskCell.textContent);
    if (newTaskName !== null) {
        taskCell.textContent = newTaskName;
    }
}

function removeTask(button) {
    const row = button.closest("tr");
    row.remove();
}
