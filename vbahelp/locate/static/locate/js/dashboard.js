/**
 * Created by ndudley on 8/24/15.
 */

$(function() {

    var canvas = document.getElementById('classroom-layout');
    var context = canvas.getContext('2d');
    var img = document.getElementById('background-img');

    var img_original_width = img.width;
    var img_original_height = img.height;

    var selected_circle_id = '';

    raw_coord_array = $.parseJSON(coordinates_from_django);
    coord_array = [];

    for (index = 0; index < raw_coord_array.length; ++index) {
        coord_array.push(raw_coord_array[index].fields);
    }

    console.log(coord_array);

    drawCanvas();
    drawLocationCircles();

    var id;
    $(window).resize(function() {
        drawCanvas();
        clearTimeout(id);
        id = setTimeout(doneResizing, 500);
    });

    $('#ticket-list-table tr').hover(function() {
        //$(this).addClass('hover');
        selected_circle_id = $(this).attr("data-ts-id")
        drawLocationCircles()

      }, function() {
        selected_circle_id = ''
        drawLocationCircles()
        //$(this).removeClass('hover');
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
      //Better to abstract this out
      for (index = 0; index < coord_array.length; ++index) {
        console.log("CANDIDATE:" + coord_array[index]['ticket'] + ' MATCH:' + selected_circle_id);
        //TODO: Trying to get these two strings to match!
        row_id = coord_array[index]['ticket']

        if (coord_array[index]['ticket'] == selected_circle_id) {
          console.log('SELECTED');
          drawLocationCircle(index, true)
        } else {
          drawLocationCircle(index, false);
        }

      }
    }

    function drawLocationCircle(index, isSelected) {

            var canvas_width = $('#classroom-layout').width();
            var canvas_height = $('#classroom-layout').height();

            var img_width = coord_array[index].img_width;
            var img_height = coord_array[index].img_height;
            var xcoord = coord_array[index].xcoord;
            var ycoord = coord_array[index].ycoord;


            xcoord = canvas_width / img_width * xcoord;
            ycoord = canvas_height / img_height * ycoord;

            $('#classroom-layout').drawCircle(xcoord, ycoord,
                                              canvas, img, isSelected);
    }




});
