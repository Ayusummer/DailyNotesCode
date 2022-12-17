<?php
class K0rz3n
{
    private $test;
    public $K0rz3n = "i am K0rz3n";

    function __construct()
    {
        $this->test = new L();
    }

    function __destruct()
    {
        $this->test->action();
    }
}

class L
{
    function action()
    {
        echo "Welcome to XDSEC";
    }
}

class Evil
{

    var $test2;

    function action()
    {
        eval($this->test2);
    }
}

unserialize($_GET['test']);