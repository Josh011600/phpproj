<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Admin - User Management</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/admin_dashboard.css') }}">
  
  <link rel="stylesheet" href="css/admin_dashboard.css">
</head>
<body>

<div class="container">
  <h2>Add New User</h2>
  <form id="userForm">
  <div class="form-group">
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" required>
  </div>

  <div class="form-group">
    <label for="age">Age</label>
    <input type="number" id="age" name="age">
  </div>

  <div class="form-group">
    <label for="email">Email</label>
    <input type="email" id="email" name="email">
  </div>

  <div class="form-group">
    <label for="username">Username</label>
    <input type="text" id="username" name="username">
  </div>

  <div class="form-group">
    <label for="password">Password</label>
    <input type="password" id="password" name="password">
  </div>

  <div class="form-group">
    <label for="role">Role</label>
    <select id="role" name="role">
      <option value="user">User</option>
      <option value="admin">Admin</option>
    </select>
  </div>

  <div class="form-group">
    <label for="status">Status</label>
    <select id="status" name="status">
      <option value="active">Active</option>
      <option value="inactive">Inactive</option>
    </select>
  </div>

  <div class="error" id="errorMsg"></div>
  <button type="submit">Add User</button>
</form>


  <h2>User List</h2>
  <table id="userTable">
    <thead>
      <tr>
        <th>#</th>
        <th>Full Name</th>
        <th>Age</th>
        <th>Email</th>
        <th>Username</th>
        <th>Role</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <!-- Users will be inserted here -->
    </tbody>
  </table>
</div>

<script>
/*  let userCount = 0;

  document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const errorMsg = document.getElementById('errorMsg');
    errorMsg.textContent = '';

    const name = document.getElementById('name').value.trim();
    const age = document.getElementById('age').value;
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;
    const status = document.getElementById('status').value;

    // Simple validation
    if (name.length < 3) {
      errorMsg.textContent = 'Name must be at least 3 characters.';
      return;
    }
    if (password.length < 6) {
      errorMsg.textContent = 'Password must be at least 6 characters.';
      return;
    }

    userCount++;
    const table = document.getElementById('userTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.innerHTML = `
      <td>${userCount}</td>
      <td>${name}</td>
      <td>${age}</td>
      <td>${email}</td>
      <td>${username}</td>
      <td>${role}</td>
      <td>${status}</td>
    `;

    alert("User added successfully!");

    // Reset the form
    document.getElementById('userForm').reset();
  });*/
</script>

</body>
</html>
