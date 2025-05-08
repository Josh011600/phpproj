<!DOCTYPE html>
<html lang="en">
<head>
    
    <title>Document</title>
</head>

<body>
<link rel="stylesheet" href="tools/css/testing.css">

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "test";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT id, firstname, lastname, middlename FROM employees";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. " " . $row["middlename"] . "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();

?><br>
<input type="text" placeholder="Enter firstnumber" style=""><br>
<input type="text" placeholder="Enter secondnumber">

</body>
</html>