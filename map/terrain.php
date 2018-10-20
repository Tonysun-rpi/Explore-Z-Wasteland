<?php
/**
 * Created by PhpStorm.
 * User: wangj
 * Date: 2018/10/20
 * Time: 16:01
 */
//forest
//lake,river
class terrain
{
    var $name;
    var $is_barrier;

    function __construct($n)
    {
        $this->name=$n;
        if($n=="river"){
            $this->is_barrier=true;
        }
        else{
            $this->is_barrier=false;
        }
    }

}