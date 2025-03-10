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
            document.getElementById('navbar').classList.toggle('hidden');
            document.getElementById('content').classList.toggle('shifted');
        }