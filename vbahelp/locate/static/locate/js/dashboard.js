/**
 * Created by ndudley on 8/24/15.
 */

$(function() {

    var canvas = document.getElementById('classroom-layout');
    var context = canvas.getContext('2d');
    var img = document.getElementById('background-img');

    var img_original_width = img.width;
    var img_original_height = img.height;

    raw_array = $.parseJSON(data_from_django);
    //console.log(raw_array);
    coord_array = [];

    for (index = 0; index < raw_array.length; ++index) {
        coord_array.push(raw_array[index].fields);
    }

    drawCanvas();
    drawLocationCircles();

    var id;
    $(window).resize(function() {
        drawCanvas();
        clearTimeout(id);
        id = setTimeout(doneResizing, 500);
    });

    function doneResizing(){
      drawLocationCircles();
    }

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


    function drawLocationCircles() {
        for (index = 0; index < coord_array.length; ++index) {

            var canvas_width = $('#classroom-layout').width();
            var canvas_height = $('#classroom-layout').height();

            var img_width = coord_array[index].img_width;
            var img_height = coord_array[index].img_height;
            var xcoord = coord_array[index].xcoord;
            var ycoord = coord_array[index].ycoord;

            xcoord = canvas_width / img_width * xcoord;
            ycoord = canvas_height / img_height * ycoord;

            $('#classroom-layout').drawCircle(xcoord, ycoord,
                                              canvas, img);
        }
    }


});
