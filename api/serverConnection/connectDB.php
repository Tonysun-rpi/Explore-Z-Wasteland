<?php
/**
 * Created by PhpStorm.
 * User: lihon
 * Date: 8/23/2018
 * Time: 11:26 AM
 */


function connectDB($host, $username, $password,$database)
{
    $con = new mysqli($host,$username,$password,$database);
    if(!$con){
        die("can't connect");
    }

    return $con;
}






?>