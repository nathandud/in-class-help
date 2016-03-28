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

    raw_ticket_array = $.parseJSON(tickets_from_django);
    ticket_array = [];

    for (index = 0; index < raw_ticket_array.length; ++index) {
        ticket_array.push(raw_ticket_array[index].fields);
    }

    raw_coord_array = $.parseJSON(coordinates_from_django);
    coord_array = [];

    for (index = 0; index < raw_coord_array.length; ++index) {
        coord_array.push(raw_coord_array[index].fields);
    }

    drawCanvas();
    drawAllCircles();

    var myTextArea = document.getElementById("code-mirror-div");
    myTextArea.value = 'Option Explicit \n\n'

    var editor = CodeMirror(function(elt) {
        console.log(myTextArea.parentNode);
        myTextArea.parentNode.replaceChild(elt, myTextArea);
        },
        {
            lineNumbers: true,
            matchBrackets: true,
            value: myTextArea.value,
            mode: "vbscript"
        });

    // var editor = CodeMirror.fromTextArea(document.getElementById("code-mirror-div"), {
    //     lineNumbers: true,
    //     matchBrackets: true,
    //     mode: "vbscript"
    //   });


    // var id;
    // $(window).resize(function() {
    //     drawCanvas();
    //     clearTimeout(id);
    //     id = setTimeout(doneResizing, 500);
    // });

    $('#ticket-list-table tr').hover(function() {
        selected_circle_id = $(this).attr("data-ts-id")
        drawLocationCircle(getCircleIndexFromId(selected_circle_id), true);
        $("#student-question").text(ticket_array[index].student_question);
        editor.getDoc().setValue(ticket_array[index].student_code);
      }, function() {
        selected_circle_id = '';
        drawAllCircles()
    });

    function doneResizing(){
      drawAllCircles();
    }

    function drawCanvas() {
        var parent = img.parentNode;
        var ratio = img.width / img.height;

        if (img_original_width > parent.offsetWidth - 100) {
            img.width = (parent.offsetWidth - 100) * 0.75;
            img.height = (img.width / ratio) * 0.75;
            canvas.width = (parent.offsetWidth - 100) * 0.75;
            canvas.height = (canvas.width / ratio) * 0.75;
        } else {
            img.width = img_original_width;
            img.height = img_original_height;
            canvas.width = img_original_width;
            canvas.height = img_original_height;
        }

        context.drawImage(img, 0, 0, img.width, img.height);
    }

    function drawAllCircles() {
      //Better to abstract this out
      for (index = 0; index < coord_array.length; ++index) {
        row_id = coord_array[index]['ticket'];

        if (coord_array[index]['ticket'] == selected_circle_id) {
          drawLocationCircle(index, true);
        } else {
          drawLocationCircle(index, false);
        }
      }
    }

    function getCircleIndexFromId(circle_id) {
      for (index = 0; index < coord_array.length; ++index) {
        if ( coord_array[index]['ticket'].trim() == circle_id.trim() ) {
          return index;
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
