<?php
/**
 * Created by PhpStorm.
 * User: lihon
 * Date: 8/22/2018
 * Time: 4:22 PM
 */

function alertAndJump($msg, $addr, $time)
{
    echo "<script language=\"javascript\" type=\"text/javascript\">
    //password too weak
    alert('$msg');
    setTimeout(location.href=\"$addr\", $time);
    </script>";
}

?>