<?php

/***
to auto-load class definitions from PHP files
***/
spl_autoload_register(function($class) {
    $path = $class . ".php";
    require_once $path; 
    
});


?>