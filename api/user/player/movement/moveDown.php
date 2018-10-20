<?php
/**
 * Created by PhpStorm.
 * User: wangj
 * Date: 2018/10/20
 * Time: 15:35
 */
require_once("../interactionHelper.php");

$username = $_POST['name'];
$result = moveDown($username);

/*
 *
 * <form action="welcome.php" method="post">

<input type="submit" value="提交">
 */