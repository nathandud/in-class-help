/**
 * Created by ndudley on 4/17/15.
 */

$.fn.drawAnimatedCircle = function(centerX, centerY, canvas, img, isSelected) {
    const CIRCLE_RADIUS_TO_CANVAS_RATIO = 0.02;
    const BEGIN_RADIUS_TO_END_RADIUS_RATIO = 0.07;
    const CIRCLE_GROWTH_TO_BEGIN_RADIUS_RATIO = 2;

    var context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);

    var end_radius = canvas.width * CIRCLE_RADIUS_TO_CANVAS_RATIO;
    var begin_radius = end_radius * BEGIN_RADIUS_TO_END_RADIUS_RATIO;

    var radius = begin_radius;

    context.drawImage(img, 0, 0, img.width, img.height);
    draw();

    function draw() {
        if (isSelected) {
          context.fillStyle = '#FFFFFF';

        } else {
          context.fillStyle = '#8FAE8F';
        }

        context.strokeStyle = '#1F5C1F';
        context.lineWidth = "1.5";
        context.beginPath();
        context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
        context.fill();
        context.stroke();


        radius += CIRCLE_GROWTH_TO_BEGIN_RADIUS_RATIO;
        if (radius < end_radius) {
            requestAnimationFrame(draw);
        }
    }
};

$.fn.drawCircle = function(centerX, centerY, canvas, img, isSelected) {
    const CIRCLE_RADIUS_TO_CANVAS_RATIO = 0.02;

    var context = canvas.getContext('2d');
    //context.clearRect(0, 0, canvas.width, canvas.height);

    var end_radius = canvas.width * CIRCLE_RADIUS_TO_CANVAS_RATIO;
    var radius = end_radius;

    draw();

    function draw() {
        if (isSelected) {
          context.fillStyle = '#AE8F8F';
          context.strokeStyle = '#342A2A';
        } else {
          context.fillStyle = '#8FAE8F';
          context.strokeStyle = '#1F5C1F';
        }

        context.lineWidth = "1.5";
        context.beginPath();
        context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
        context.fill();
        context.stroke();
    }
};
