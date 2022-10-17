$(".button").on("click", function(event) {
    event.preventDefault();
    html2canvas(document.getElementById("textArea"), {
        allowTaint: true,
        taintTest: false,
        onrendered: function(canvas) {
            canvas.id = "mycanvas";
            //生成base64图片数据
            var dataUrl = canvas.toDataURL();
            var newImg = document.createElement("img");
            newImg.src =  dataUrl;
            document.body.appendChild(newImg);
        }
    });
});
