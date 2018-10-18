<?php
/**
 * Created by PhpStorm.
 * User: wangj
 * Date: 2018/10/17
 * Time: 16:25
 */
require_once ("monster_data.php");

class monster
{
    //var $redis;
    var $name;
    var $health;
    var $magic_resistance;
    var $armor;

    var $wealth; //掉落金币
    var $reword; //掉落素材

    function __construct( $n ){
        $redis=connectDB();
        $this->name=$n;
        $this->health=$redis->hget($n,"health");
        $this->magic_resistance=$redis->hget($n,"magic_resistance");
        $this->armor=$redis->hget($n,"armor");
        $this->wealth=$redis->hget($n,"wealth");



    }

    function is_attacted($h){
        $this->health-=$h;
        return;
    }

}

?>