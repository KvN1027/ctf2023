<?php
session_start();

if (!isset($_COOKIE['passwd'])) {
	setcookie('login', 'robert');
	setcookie('passwd', 'flag{i_hate_calculus}');
}

$cards = [];
if (file_exists($_SESSION['xss_db'] ?? '')) {
	$cards = json_decode(file_get_contents($_SESSION['xss_db']), true);
}
$cards = array_reverse($cards);
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<link href="https://cdn.rawgit.com/TeaMeow/TocasUI/2.3.2/dist/tocas.css" rel='stylesheet'>
	<script src="https://cdn.rawgit.com/TeaMeow/TocasUI/2.3.2/dist/tocas.js"></script>
	<title>1want詢問區</title>
	<style>
		input[name='title'] {
			font-size: 28px;
		}
	</style>
</head>
<body>
	<br>
	<br>
	<br>
	<br>
	<!-- 窄容器網格系統 -->
	<div class="ts narrow relaxed stackable container grid">
		<!-- 欄位 -->
		<div class="sixteen wide column">
			<!-- 標題 -->
			<h1 class="ts center aligned header">
				1want詢問區
				<div class="sub header">
					向教授提問時：請保持禮貌、並盡可能簡化問題
				</div>
			</h1>
			<!-- / 標題 -->
		</div>
		<!-- / 欄位 -->

		<!-- 表單欄位 -->
		<form action="submit.php" method="POST" class="sixteen wide column">
			<!-- 片段 -->
			<div class="ts segment">
				<!-- 輸入欄位 -->
				<div class="field">
					<input name="title" placeholder="標題" autocomplete="off">
				</div>
				<div class="ts borderless horizontally fitted fluid input">
					<textarea name="content" placeholder="在此輸入你想詢問的問題...." autocomplete="off"></textarea>
				</div>
				<!-- / 輸入欄位 -->

				<!-- 底部對齊用選單-->
				<div class="ts secondary fitted menu">
					<!-- 左側拉伸項目 -->
					<div class="stretched item">
						<div class="ts tiny faded fitted basic message">
							為了避免嚴重危害，此 Demo 只會顯示來自您自己的便利貼。
						</div>
					</div>
					<!-- / 左側拉伸項目 -->
					<div class="item">
						<button class="ts mini primary button" type="submit">送出</button>
					</div>
				</div>
				<!-- / 底部對齊用選單 -->
			</div>
			<!-- / 片段 -->
		</form>
		<!-- / 表單欄位 -->

		<!-- 便利貼欄位 -->
		<div class="sixteen wide column">
			<!-- 瀑布流卡片群組 -->
			<div class="ts stackable three waterfall cards">
<?php foreach ($cards as $card) { ?>
				<!-- 單張卡片 -->
				<div class="ts card">
					<div class="content">
						<div class="header"><?= $card['title'] ?></div>
						<div class="meta">
							<div>今天</div>
						</div>
						<div class="description">
							<p><?= $card['content'] ?></p>
						</div>
					</div>
				</div>
				<!-- / 單張卡片 -->
<?php } ?>

				<!-- 單張卡片 -->
				<div class="ts card">
					<div class="content">
						<div class="header">樓頂風大</div>
						<div class="meta">
							<div>一天前</div>
						</div>
						<div class="description">
							<p>喂，教授嗎？ 我現在在我家樓頂，我的微積分作業真的寫不完了，下週報告也做不出來，這裡風好大我好害怕...</p>
						</div>
					</div>
				</div>
				<!-- / 單張卡片 -->

				<!-- 單張卡片 -->
				<div class="ts card">
					<div class="content">
						<div class="header">好了啦數學哥</div>
						<div class="meta">
							<div>一天前</div>
						</div>
						<div class="description">
							<p>好了啦數學哥下週可以不要再出作業了嗎= =</p>
							<p>有沒有想過這麼多怎麼可能寫完</p>
						</div>
					</div>
				</div>
				<!-- / 單張卡片 -->

				<!-- 單張卡片 -->
				<div class="ts card">
					<div class="content">
						<div class="header">貓咪🐱</div>
						<div class="meta">
							<div>兩天前</div>
						</div>
						<div class="description">
							<p>假設現在你有一隻貓咪，現在你又得到了一隻貓咪，你可以數一下現在你總共有幾隻貓咪，你會得到答案是兩隻，一隻貓咪加一隻貓咪等於兩隻貓咪，也就是1+1=2，這就是基本的算術原則。</p>
                            <p>我想問的是，一般來說用不完的貓咪要放在哪裡？</p>
						</div>
					</div>
				</div>
				<!-- / 單張卡片 -->

				<!-- 單張卡片 -->
				<div class="ts card">
					<div class="content">
						<div class="header">教授看一下</div>
						<div class="meta">
							<div>一天前</div>
						</div>
						<div class="description">
							<p>教授拜託看一下><</p>
                            <p><a href="https://youtube.com/shorts/_5belT9OsNM?feature=share">youtube.com/shorts/_5belT9OsNM?</a></p>
						</div>
					</div>
				</div>
                <div class="ts card">
					<div class="content">
						<div class="header">為什麼不能除以零</div>
						<div class="meta">
							<div>一天前</div>
						</div>
						<div class="description">
							<p>幼稚園的時候老師告訴我不能除以0，要不然的話貓咪會不高興，但到底為什麼不能除以0...</p>
						</div>
					</div>
				</div>

				<!-- / 單張卡片 -->
			</div>
			<!-- / 瀑布流卡片群組 -->
		</div>
		<!-- / 便利貼欄位 -->

		<button class="ts negative large button" onclick="location.href = 'flush.php';" style="margin: 42px;">清除紀錄</button>
	</div>
	<!-- / 窄容器網格系統 -->
</body>
</html>
<!-- Modified from https://examples.tocas-ui.com/pages/notes.html -->