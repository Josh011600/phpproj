<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Scheduler</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles2.css') }}">
    <script src="{{ url_for('static', filename='js/testscript.js') }}"></script>
    <style>
       
    </style>
</head>
<body>
    
    <button class="toggle-nav-btn" onclick="toggleNavbar()">☰</button>
    <nav class="navbar" id="navbar">
        <div class="home">Home</div>
        <ul class="nav-links">
            <li><button onclick="toggleContent('home')">Create</button></li>
            <li><button onclick="toggleContent('about')">View Tasks</button></li>
            <li><button onclick="toggleContent('completedTasks')">View Completed Tasks</button></li>
            <li><button onclick="toggleContent('failedTasks')">View Failed Tasks</button></li>
            <li><button onclick="toggleContent('Logout')">Logout</button></li>
        </ul>
    </nav>
    
    <div class="content" id="content">
        
        <div class="task-container page" id="home">
            
            <label for="task" class="label1"><strong>Add Task Schedule</strong></label>
            <input type="text" name="task" class="txtTask" id="add_task" placeholder="Enter task">
            <input id="party" type="datetime-local" name="party-date" value="2025-06-01T08:30" />
            <button class="add_Button" onclick="addTask()">Add Task</button>
    
            <h1 class="task_list_title">Task List</h1>
            <table id="taskTable">
                <thead>
                    <tr>
                        <th>Time and Date</th>
                        <th>ID</th>
                        <th>Task Name</th>
                        <th>Scheduled Date</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </div>
    
        <div id="about" class="page">This is the About Page.</div>
        <div id="completedTasks" class="page">This is the Completed Tasks Page.</div>
        <div id="failedTasks" class="page">
            <h2>Failed Tasks</h2>
            <table id="taskTable">
            <thead>
                <tr>
                    <th>Time and Date Today</th>
                    <th>ID</th>
                    <th>Task Name</th>
                    <th>Scheduled Date</th>
                    <th>Action</th>
                </tr>
            </thead>
            </table>
            
        </div>
    </div>
    
    
</body>
</html>
