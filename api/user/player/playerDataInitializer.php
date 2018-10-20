<?php
/**
 * Created by PhpStorm.
 * User: lihon
 * Date: 8/22/2018
 * Time: 4:15 PM
 */

function playerDataInitialize($username,$redis)
{
    $redis->hset($username, 'x', 0);
    $redis->hset($username, 'y', 0);
    $redis->hset($username, 'level', 0);
}

?>