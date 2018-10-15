<?php

include "playerDataInitializer.php";

function checkDup($username, $redis){

//check duplicate
    $result = $redis->hExists('password',$username);
    if ($result) {

        return true;
    } else {

        return false;
    }
}

function register($username, $passwordH,$email, $redis)
{
    $redis->hSet('password',$username,$passwordH);
    $redis->hSet('email',$username,$email);


    playerDataInitialize($username,$redis);
}

?>