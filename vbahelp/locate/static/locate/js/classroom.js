/**
* Created by ndudley on 4/16/15.
*/
$(function() {

    var canvas = document.getElementById('classroom-layout');
    var context = canvas.getContext('2d');
    var img = document.getElementById('background-img');

    var img_original_width = img.width;
    var img_original_height = img.height;

//    console.log($('#classroom-layout').width);
//
//    if ($('#classroom-layout').width === 0) {
//        location.reload();
//    }

    drawCanvas();
    var myTextArea = document.getElementById("id_code_submission");
    myTextArea.value = 'Option Explicit \n\n'

    var myCodeMirror = CodeMirror(function(elt) {
            myTextArea.parentNode.replaceChild(elt, myTextArea);
        },
        {
            value: myTextArea.value,
            mode: "vbscript"
        });

    console.log(myTextArea);




//    var myCodeMirror = CodeMirror(document.body, {
//      value: "Option Explicit\n\n",
//      mode:  "vbscript"
//    });


    $('#classroom-layout').off('click').on('click', function(evt) {

        var offset = $(this).offset();
        var centerX = (evt.pageX - offset.left);
        var centerY = (evt.pageY - offset.top);

        $(this).drawCircle(centerX, centerY, canvas, img);

        $('#id_xcoord').val(centerX);
        $('#id_ycoord').val(centerY);
        $('#id_img_width').val($(this).width());
        $('#id_img_height').val($(this).height());

    });

   $(window).resize(function() {
        drawCanvas();
    });

    function drawCanvas() {
        var parent = img.parentNode;
        var ratio = img.width / img.height;

        if (img_original_width > parent.offsetWidth - 100) {
            img.width = parent.offsetWidth - 100;
            img.height = img.width / ratio;
            canvas.width = parent.offsetWidth - 100;
            canvas.height = canvas.width / ratio;
        } else {
            img.width = img_original_width;
            img.height = img_original_height;
            canvas.width = img_original_width;
            canvas.height = img_original_height;
        }

        context.drawImage(img, 0, 0, img.width, img.height);
    }


});