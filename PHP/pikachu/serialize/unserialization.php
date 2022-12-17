<?php
    class S{
        var string $test = "pikachu";
        function __construct(){
            echo $this->test;
            echo "构造函数捏<br/>";
        }
    }

    // 实例化 S 且 test = "pikachu_test"
    $testS = new S();
    $testS->test = "pikachu_test";
    // 序列化
    $testS = serialize($testS);
    // 反序列化
    $testS = unserialize($testS);
    echo $testS->test;
    // 这说明反序列化并没有调用到构造函数, 因此在这里魔术函数 __construct() 反而并不是利用点

    $html='';
    if(isset($_POST['o'])){
        $s = $_POST['o'];
        $html .= "获取到的数据为：".$s;
        if(!@$unser = unserialize($s)){
            $html.= "反序列化失败";
            $html.="<p>$s 不够劲儿啊大兄弟,来点劲爆点儿的!</p>";
        }else{
            $html.="<p>反序列化后的数据为：</p>";
            $html.="<pre>";
            $html.=print_r($unser,true);
            $html.="</pre>";
            $html.="<p>$unser->test</p>";
        }

    }
?>


<form method="post">
    <label>
        这是一个接受序列化数据的api:
        <input type="text" name="o"/>
    </label>
    <input type="submit" value="提交">
</form>

<?php
    echo $html;
    