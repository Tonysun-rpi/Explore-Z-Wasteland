<?php
header("Content-Type: text/html; charset=utf8");

if (!isset($_POST['submit'])) {
    exit("Error");
}//valid submit or not

include("signUpHelper.php");
include("../../view/alertAndPageJump.php");
include("../../serverConnection/connectDB.php");

$con=connectDB("127.0.0.1","root","","users");

$name = $_POST['name'];//get user name
$email = $_POST['email'];
//check password validity
if(strlen($_POST['password'])<8){
    alertAndJump('Please use a password longer than 7 characters','../../../users/signup.html',1);
    return;
}
$passwordH =md5($_POST['password']);//get user password


//check duplication
$is_dup=checkDup($name,$con);
if($is_dup) {
    $con->close();
    alertAndJump('Please pick another Username','../../../users/signup.html',1);
    return;
}

//we insert user into to DB
register($name,$passwordH,$email,$con);

//close connection
$con->close();

//redirect to home page and keep login status
alertAndJump("you have sign up successfully","../../../htdocs/index.html",3000)
?>