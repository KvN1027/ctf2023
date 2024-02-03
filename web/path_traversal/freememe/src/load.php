<?php
header('content-type:html');
if(isset($_GET['file'])){
    echo file_get_contents("photos/".$_GET['file']) ;
}
?>