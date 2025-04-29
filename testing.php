<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="tools/css/testing.css">
    <title>Document</title>
</head>

<body>
    <script src=""></script>
    <form class="login-form" action="#">
    <h2>Login</h2>
    <label for="username">Username</label>
    <input type="text" id="username" name="username" placeholder="Enter username" required>

    <label for="password">Password</label>
    <input type="password" id="password" name="password" placeholder="Enter password" required>

    <button type="submit">Login</button>
  </form>

  <?php
require_once 'db/connection.php';
require_once 'User.php';

session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $db = new Database();
    $conn = $db->connect();

    $user = new User($conn);

    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($user->login($username, $password)) {
        $_SESSION['username'] = $username;
        echo "Login successful. Welcome, $username!";
        // header("Location: dashboard.php"); // Uncomment to redirect
    } else {
        echo "Invalid username or password.";
    }
}
?>

   
</body>
</html>