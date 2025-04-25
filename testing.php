<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test</title>
    <link rel="stylesheet" href="css/testing.css">
</head>
<body>
    <!--Started Learning Php 4/26/2024 ->
   <?php
   $bookName = "Dark Matter";
   $read = true;
   $message = "you have read";
   ?>
        <h1>
        <?php
        if($read === true)
        {
            echo $message . $bookName;
        }
        else
        {
            echo "You didn't read " . $bookName;
        }
        ?>
<?= $message ?>
        </h1>
        
</body>
</html>