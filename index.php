<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="styles.css">

    <title>Troy's Card Database</title>
</head>
<body>
    <form method="post" autocomplete="off">
        <?php
        echo "<label for='card-name'>Enter the name of your card:</label>\n";
        echo "<input type='text' id='card-name' name='card-name' required ";
        if (!empty($_POST)) {
            echo "value='" . $_POST["card-name"] . "'";
        }
        echo ">\n";
        echo "<label for='card-set'>Enter the set of your card:</label>\n";
        echo "<input type='text' id='card-set' name='card-set' required ";
        if (!empty($_POST)) {
            echo "value='" . $_POST["card-set"] . "'";
        }
        echo ">\n";
        echo "<label for='temp-image'>Enter the image url</label>\n";
        echo "<input type='text' id='temp-image' name='temp-image' required ";
        if (!empty($_POST)) {
            echo "value='" . $_POST["temp-image"] . "'";
        }
        echo ">\n";
        ?>
        <input type="submit" value="Submit">
    </form>
    <?php
        if (!empty($_POST)) {
            echo "<img src='" . $_POST["temp-image"] . "'>";
        }
    ?>
</body>
</html>