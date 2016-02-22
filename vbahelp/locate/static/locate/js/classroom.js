/**
* Created by ndudley on 4/16/15.
*/
$(function() {

    var canvas = document.getElementById('classroom-layout');
    var context = canvas.getContext('2d');
    var img = document.getElementById('background-img');

    var img_original_width = img.width;
    var img_original_height = img.height;

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

    $('#classroom-layout').off('click').on('click', function(evt) {

        var offset = $(this).offset();
        var centerX = (evt.pageX - offset.left);
        var centerY = (evt.pageY - offset.top);

        $(this).drawAnimatedCircle(centerX, centerY, canvas, img, false);

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

    //https://realpython.com/blog/python/django-and-ajax-form-submissions/
    // Submit post on submit
    var frm = $('#get-help-form');

    frm.submit (function () {
        event.preventDefault();

        $.ajax({
           // get the form data
          type: frm.attr('method'), // GET or POST
          url: frm.attr('action'), // the file to call
          data: frm.serialize(),

          // handle a successful response
          success : function(data) {
              console.log("success"); // another sanity check
          },

          // handle a non-successful response
          error : function(xhr,errmsg,err) {
              $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                  " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
              console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          }
        });
    });



});
