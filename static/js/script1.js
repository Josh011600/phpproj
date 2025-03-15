let taskId = 1;
        function addTask() {
            const tableBody = document.querySelector("#taskTable tbody");
            const taskInput = document.getElementById("add_task");
            const dateInput = document.getElementById("party");
            const taskName = taskInput.value.trim();
            const scheduleDate = dateInput.value;
            const today = new Date().toLocaleString();
            if (taskName === "" || scheduleDate === "") {
                alert("Please enter a task and select a date.");
                return;
            }
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${today}</td>
                <td>${taskId}</td>
                <td>${taskName}</td>
                <td>${scheduleDate}</td>
                <td>
                    <button onclick="editTask(this)" style="font-size: 1rem">Edit</button>
                    <button onclick="removeTask(this)" style="font-size: 1rem">Remove</button>
                </td>
            `;
            tableBody.appendChild(row);
            taskInput.value = "";
            dateInput.value = "";
            taskId++;
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
        function toggleNavbar() {
            const navbar = document.getElementById('navbar');
            const content = document.getElementById('content');
            const toggleBtn = document.querySelector('.toggle-nav-btn');
            navbar.classList.toggle('hidden');
            content.classList.toggle('shifted');
            if (navbar.classList.contains('hidden')) {
                toggleBtn.innerHTML = '☰';
                toggleBtn.style.left = '10px';
            } else {
                toggleBtn.innerHTML = '✖';
                toggleBtn.style.left = '260px';
            }
        }


/* Toogle navs */
function toggleContent(pageId) {
    const pages = document.querySelectorAll('.page');
    const taskContainer = document.querySelector('.task-container');

    // Hide all content by default
    pages.forEach(p => p.style.display = 'none');
    taskContainer.style.display = 'none';

    // Show the selected content
    if (pageId === 'home') {
        taskContainer.style.display = 'block';  // Show Task Scheduler
    } else {
        const selectedPage = document.getElementById(pageId);
        if (selectedPage) {
            selectedPage.style.display = 'block';  // Display selected page
        } else {
            console.error(`Page with ID "${pageId}" not found.`);
        }
    }
}

// Default page to show on load
document.addEventListener('DOMContentLoaded', () => {
    toggleContent('home');
});

/*Toogle navs end */