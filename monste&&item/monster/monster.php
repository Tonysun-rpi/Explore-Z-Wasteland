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
    var $redis;
    var $name;
    var $health;
    var $magic_resistance;
    var $armor;

    var $wealth; //掉落金币
    var $reword; //掉落素材

    function __construct( $n ){
        $this->redis=connectDB();
        $this->name=$n;


    }

    function is_attacted($h){
        $this->health-=$h;
    }

}

?>