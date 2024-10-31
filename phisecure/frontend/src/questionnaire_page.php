<html>
<head>
</head>
<body>

<?php
$f_name = $l_name = $username = $email = $empstat = $empdet = $financial_stat
= $pass_stat = $reuse_stat = $emp_phish = $emp_phish_det = "";

$f_name_error = $l_name_error = $username_error = $email_error = $empstat_error
= $financial_stat_error = $pass_stat_error = $reuse_stat_error = $emp_phish_error = "";

if ($_SERVER["REQUEST_METHOD"] == "POST")
{
    if(empty($_POST["fname"]))
    {
        $f_name_error = "First Name is Required";
    }
    else
    {
        $f_name = grab_input($_POST["fname"])
    }

    if(empty($_POST["lname"]))
    {
        $l_name_error = "Last Name is Required";
    }
    else
    {
        $l_name = grab_input($_POST["lname"])
    }

    if(empty($_POST["uname"]))
    {
        $username_error = "Username is Required";
    }
    else
    {
        $username = grab_input($_POST["uname"])
    }
    
    if(empty($_POST["email"]))
    {
        $email_error = "Email is Required";
    }
    else
    {
        $email = grab_input($_POST["email"])
    }

    if(empty($_POST["empstat"]))
    {
        $empstat_error = "Employment Status is Required";
    }
    else
    {
        $empstat = grab_input($_POST["empstat"])
    }

    $empdet = grab_input($_POST["empdet"])

    if(empty($_POST["financial"]))
    {
        $financial_stat_error = "Financial Status is Required";
    }
    else
    {
        $financial_stat = grab_input($_POST["financial"])
    }

    if(empty($_POST["pass"]))
    {
        $pass_stat_error = "This Field is Required";
    }
    else
    {
        $pass_stat = grab_input($_POST["pass"])
    }

    if(empty($_POST["reuse"]))
    {
        $reuse_stat_error = "This Field is Required";
    }
    else
    {
        $reust_stat = grab_input($_POST["reuse"])
    }

    if(empty($_POST["empphish"]))
    {
        $emp_phish_error = "This Field is Required";
    }
    else
    {
        $emp_phish = grab_input($_POST["fname"])
    }

    $emp_phish_det = grab_input($_POST["ead"])
    test_input()
}

function grab_input($data)
{
    $data = trim($data)
    $data = stripslashes($data)
    $data = htmlspecialchars($data)
    return $data
}

// Function to test input to make sure it was properly grabbed. For testing purposes only.
function test_input()
{
    echo "<h2>Your Input:</h2>";
    echo $f_name; echo "<br>";
    echo $l_name; echo "<br>";
    echo $username; echo "<br>";
    echo $email; echo "<br>";
    echo $empstat; echo "<br>";
    echo $empdet; echo "<br>";
    echo $nfinancial_stat; echo "<br>";
    echo $pass_stat; echo "<br>";
    echo $reuse_stat; echo "<br>";
    echo $emp_phish; echo "<br>";
    echo $emp_phish_det; echo "<br>";
}
?>

</body>
</html>