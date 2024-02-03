<?php
// 設定上傳目錄
$uploadDirectory = 'upload/';

// 檢查是否有上傳檔案
if (isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // 檢查是否有錯誤碼
    if ($file['error'] === UPLOAD_ERR_OK) {
        // 檢查檔案大小是否大於500KB
        $maxFileSize = 500 * 1024; // 500KB
        if ($file['size'] > $maxFileSize) {
            die('Error: 檔案大小不能超過 500KB.');
        }

        // 檢查是否僅允許單一檔案
        if (count($_FILES) > 1) {
            die('Error: 一次僅允許上傳單一檔案.');
        }

        // 取得檔案名稱及副檔名
        $originalFileName = $file['name'];
        $fileExtension = pathinfo($originalFileName, PATHINFO_EXTENSION);
        
        // 產生8位隨機數字
        $randomNumber = bin2hex(random_bytes(4));

        // 新的檔案名稱
        $newFileName = $randomNumber . '_' . $file['name'];

        // 移動檔案到上傳目錄
        if (@move_uploaded_file($file['tmp_name'], $uploadDirectory . $newFileName)) {
            echo 'SUCCESS~檔案上傳成功！';
        } else {
            echo 'Error: 檔案上傳失敗.';
        }
    } else {
        echo 'Error: 檔案上傳錯誤.';
    }
} else {
    echo 'Error: 沒有選擇檔案上傳.';
}
?>

<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
<title>process</title>
<section class="vh-100" style="background-color: #9A616D;">
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col col-xl-10">
                <div class="card" style="border-radius: 1rem;">
                    <div class="row g-0">
                        <div class="col-md-6 col-lg-5 d-none d-md-block">
                            <img src="<?php echo "upload/".$newFileName; ?>" alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
                        </div>
                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                            <div class="card-body p-4 p-lg-5 text-black">

                                <form method="POST" action="preview.php" enctype="multipart/form-data">
                                    <div class="d-flex align-items-center mb-3 pb-1">
                                        <span class="h1 fw-bold mb-0">Processes2.0</span>
                                    </div>

                                    
                                    
                                    <div class="d-flex align-items-center mb-3 pb-1">
                                        <span class="h1 fw-bold mb-0">@<?php 
                                    if ($_SERVER["REQUEST_METHOD"] == "POST") {
                                        if (isset($_POST["username"])  && isset($_POST["password"])) {
                                            echo $_POST["username"];
                                        } else {
                                            echo "username or password is empty";
                                        }
                                    }
                                        ?></span>
                                    </div>
                                    <h5 class="fw-normal mb-3 pb-3 text-black-50" style="letter-spacing: 1px;">screenshot to share with your friend!</h5>
                                </form>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>