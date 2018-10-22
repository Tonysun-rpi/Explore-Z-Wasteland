<?php

require_once '../../serverConnection/connectDB.php';

function isCorrectPassword($username, $passwordH, $redis)
{
    $result = $redis->hGet($username, 'password');
    if(!$result)
    {
        return false;
    }

    if ($result != $passwordH)
    {
        return false;
    }

    return true;
}