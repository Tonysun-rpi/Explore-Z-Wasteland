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
    var $damage;
    var $health;
    var $magic_resistance;
    var $armor;
    var $max_health;

    var $wealth; //掉落金币
    var $reward_1; //掉落素材
    var $reward_2;
    var $reward_3;
    var $reward_4;
    var $reward_rate; //掉落素材倍率

    function __construct( $n ){
        $this->redis=connectDB();
        $this->name=$n;
        $this->damage=$this->redis->hget($n,"damage");
        $this->health=$this->redis->hget($n,"health");
        $this->magic_resistance=$this->redis->hget($n,"magic_resistance");
        $this->armor=$this->redis->hget($n,"armor");
        $this->wealth=$this->redis->hget($n,"wealth");
        $this->reward_1=$this->redis->hget($n,"reward_1");
        $this->reward_2=$this->redis->hget($n,"reward_2");
        $this->reward_3=$this->redis->hget($n,"reward_3");
        $this->reward_4=$this->redis->hget($n,"reward_4");
        $this->reward_rate=$this->redis->hget($n,"reward_rate");
        $this->max_health=$this->health;
        //here



    }

    public function get_info(){
        $info=[$this->health,$this->damage,$this->armor,$this->magic_resistance];
        return $info;
    }

    public function give_reword(){
        //p 是获得该物品的概率
        $p1=$this->redis->hget("reward",$this->reward_1)*$this->reward_rate;
        $p2=$this->redis->hget("reward",$this->reward_2)*$this->reward_rate;
        $p3=$this->redis->hget("reward",$this->reward_3)*$this->reward_rate;
        $p4=$this->redis->hget("reward",$this->reward_4)*$this->reward_rate;
        $reward_list=array($this->reward_1=>$p1,$this->reward_2=>$p2,
                            $this->reward_3=>$p3,$this->reward_4=>$p4);
        foreach($reward_list as $key=>$value){
            $random=rand(0,1);
            if($random>$value){
                $reward_list[$key]=0; //如果random比概率大，不获得该物品
            }
            else{
                $num=ceil($value/$random);
                $reward_list[$key]=$num;
            }
        }
        return $reward_list;
    }





    function is_attacted($h){
        $this->health-=$h;
        return;
    }

}

?>