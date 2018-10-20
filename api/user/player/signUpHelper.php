<?php

include "playerDataInitializer.php";

function checkDup($username, $redis){

//check duplicate
    $result = $redis->exists($username);
    if ($result) {

        return true;
    } else {

        return false;
    }
}

function checkValid($username)
{
    if(strpos($username, '_') !== false) return false;
    return true;
}

function register($username, $passwordH,$email, $redis)
{
    $redis->hSet($username,'password',$passwordH);
    $redis->hSet($username,'email',$email);


    playerDataInitialize($username,$redis);
}

?>