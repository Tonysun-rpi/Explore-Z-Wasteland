<?php
/**
 * Created by PhpStorm.
 * User: lihon
 * Date: 8/23/2018
 * Time: 11:26 AM
 */


function connectDB()
{
    try{
    $redis = new redis();
    }
    catch(Exception $e){
        die($e->getMessage());
    }

    return $redis;
}






?>