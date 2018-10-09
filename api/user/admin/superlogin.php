<?PHP
header("Content-Type: text/html; charset=utf8");


if (!isset($_POST["submit"])) {
    exit("Error");
}//valid submit or not

include("../../serverConnection/connectDB.php");
include("../../view/alertAndPageJump.php");

$con=connectDB("127.0.0.1","root","","users");

$name = $_POST['name'];//get username
$passowrdH =$_POST['password'];//get password

if ($name and $_POST['password']) {//if username and password are entered, query
    $sql = "select * from superuser where user_name = '$name' and user_password='$passowrdH'";
    $result = $con->query($sql);

    if ($result->num_rows>0) {
        header("refresh:0;url=../../../htdocs/superpage.html");
        exit;
    } else {
        alertAndJump("Wrong username or Password","../../../users/superlogin.html",2000);
    }

} else {
    alertAndJump("Please fill in all fields","../../../users/superlogin.html",2400);
}

$con->close();
?>