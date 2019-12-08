<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}


h2{color:blue;}

</style>
</head>
<body>

<h2>Online Questions!!!</h2>


<?php 

$command = escapeshellcmd('nctest.py');
$output = shell_exec($command);
echo $output;

?>



</body>
</html>
