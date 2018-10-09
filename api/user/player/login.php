<?PHP
header("Content-Type: text/html; charset=utf8");


if (!isset($_POST["submit"])) {
    exit("Error");
}//valid submit or not

include("../../serverConnection/connectDB.php");
include("../../view/alertAndPageJump.php");

$con=connectDB("127.0.0.1","root","","users");

$name = $_POST['name'];//get username
$passowrdH = md5($_POST['password']);//get password

if ($name and $_POST['password']) {//if username and password are entered, query
    $sql = "select * from user where account_id = '$name' and password='$passowrdH'";
    $result = $con->query($sql);

    if ($result->num_rows>0) {
        header("refresh:0;url=../../../htdocs/index.html");
        exit;
    } else {
        alertAndJump("Wrong username or Password","../../../users/login.html",2000);
    }

} else {
    alertAndJump("Please fill in all fields","../../../users/login.html",2400);
}

$con->close();
?>