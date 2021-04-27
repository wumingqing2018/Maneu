// 这是把id=body 的div 居中显示的js
window_height=window.screen.height;
body = document.getElementById('body');
body_height = body.offsetHeight;
move_height = body.style.marginTop=(window_height-body_height)/4+'px';