<?PHP
header("Content-Type: text/html; charset=utf8");


if (!isset($_POST["submit"])) {
    exit("Error");
}//valid submit or not

include("../../serverConnection/connectDB.php");
include("../../view/alertAndPageJump.php");
require_once ("loginHelper.php");

$redis=connectDB();

$name = $_POST['name'];//get username
$passowrdH = md5($_POST['password']);//get password

if ($name and $_POST['password']) {//if username and password are entered, query
    $result = isCorrectPassword($name, $passowrdH, $redis);

    if ($result) {
        header("refresh:0;url=../../../htdocs/index.html");
        exit;
    } else {
        alertAndJump("Wrong username or Password","../../../users/login.html",2000);
    }

} else {
    alertAndJump("Please fill in all fields","../../../users/login.html",2400);
}

$redis->close();
?>