<?php
header("Content-Type: text/html; charset=utf8");

if (!isset($_POST['submit'])) {
    exit("Error");
}//valid submit or not

include("signUpHelper.php");
include("../../view/alertAndPageJump.php");
include("../../serverConnection/connectDB.php");

$redis=connectDB();

$name = $_POST['name'];//get user name
$email = $_POST['email'];
//check password validity
if(strlen($_POST['password'])<8){
    $password_err="Please use a password longer than 7 characters";
    alertAndJump('Please use a password longer than 7 characters','../../../users/signup.html',1);
    return;
}
$passwordH =md5($_POST['password']);//get user password

if (!preg_match("/([\w\-]+\@[\w\-]+\.[\w\-]+)/",$email)) {
    $email_err="Please enter an valid e-mail','../../../users/signup.html";
    alertAndJump('Please enter an valid e-mail','../../../users/signup.html',1);
    return;
}
//check duplication
$is_dup=checkDup($name,$redis);
$is_valid=checkValid($name);
if($is_dup || !$is_valid) {
    $user_err="Please pick another Username";
    alertAndJump('Please pick another Username','../../../users/signup.html',1);
    return;
}

//we insert user into to DB
register($name,$passwordH,$email,$redis);

//close connection
$redis->close();

//redirect to home page and keep login status
alertAndJump("you have sign up successfully","../../../htdocs/index.html",3000)
?>