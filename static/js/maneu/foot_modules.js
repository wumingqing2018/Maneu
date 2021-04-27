var window_height=window.screen.height;
var foot_modules = document.getElementById('body');
var foot_height = foot_modules.offsetHeight;

foot_modules.style.height = window_height-foot_height+'px'

alert(foot_modules);
