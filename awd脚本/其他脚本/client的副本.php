<?php
class Rsa {
private static $PRIVATE_KEY = '';
 
private static function getPrivateKey()
{
	$privKey = self::$PRIVATE_KEY;
	return openssl_pkey_get_private($privKey);
}
 
public static function privEncrypt($data = '')
{
	if (!is_string($data)) {
		return null;
	}
	return openssl_private_encrypt($data,$encrypted,self::getPrivateKey()) ?base64_encode($encrypted) : 	
	null;
}
}
$rsa = new Rsa();
$cmd = $_POST['cmd'];
$action = "enc";
if($action!==Null){
if($action==="enc"){
	$privEncrypt = $rsa->privEncrypt($cmd);
	echo $privEncrypt;
	}
}

