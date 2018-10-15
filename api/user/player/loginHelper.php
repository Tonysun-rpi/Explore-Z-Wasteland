<?php

function isCorrectPassword($username, $passwordH, $redis)
{
    $result = $redis->hGet('password', $username);
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