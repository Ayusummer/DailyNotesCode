<?php
class S{
    public $test="pikachu";
    public $a = array('a' => 'Apple' ,'b' => 'banana' , 'c' => 'Coconut');
}
$s=new S(); //创建一个对象

echo '序列化后的数据为：'.serialize($s).'</br>';
echo '使用 json_encode() 函数序列化后的数据为：'.json_encode($s).'</br>';

$a = array('a' => 'Apple' ,'b' => 'banana' , 'c' => 'Coconut');
echo '序列化后的数据为：'.serialize($a).'</br>';

echo '使用 json_encode() 函数序列化后的数据为：'.json_encode($a).'</br>';


class animal {
    private $name = 'caixukun';

    public function sleep(){
        echo "<hr>";
        echo $this->name . " is sleeping...\n";
    }
    public function __wakeup(){
        echo "<hr>";
        echo "调用了__wakeup()方法\n";
    }
    public function __construct(){
        echo "<hr>";
        echo "调用了__construct()方法\n";
    }
    public function __destruct(){
        echo "<hr>";
        echo "调用了__destruct()方法\n";
    }
    public function __toString(){
        echo "<hr>";
        echo "调用了__toString()方法\n";
        return "";
    }
    public function __set($key, $value){
        echo "<hr>";
        echo "调用了__set()方法\n";
    }
    public function __get($key) {
        echo "<hr>";
        echo "调用了__get()方法\n";
    }
}

$ji = new animal();
$ji->name = 1;
echo $ji->name;
$ji->sleep();
$ser_ji = serialize($ji);
//print_r($ser_ji);
print_r(unserialize($ser_ji));
