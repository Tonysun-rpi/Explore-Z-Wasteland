<?php

include "playerDataInitializer.php";

function checkDup($username, $con){

//check duplicate
    $q = "SELECT * FROM `user` WHERE account_id=$username";
    $result = $con->query($q);
    if ($result->num_rows > 0) {
        return true;
    } else {
        return false;
    }
}

function register($username, $passwordH,$email, $con)
{
    $q = "INSERT INTO `user` (`user_id`, `account_id`, `password`, `email`) 
    VALUES (NULL, '$username', '$passwordH', '$email')";
    $con->query($q);


    playerDataInitialize($username,$con);
}

?>