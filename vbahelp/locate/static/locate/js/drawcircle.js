/**
 * Created by ndudley on 4/17/15.
 */

$.fn.drawCircle = function(centerX, centerY, canvas, img) {
    const CIRCLE_RADIUS_TO_CANVAS_RATIO = 0.02;
    const BEGIN_RADIUS_TO_END_RADIUS_RATIO = 0.07;
    const CIRCLE_GROWTH_TO_BEGIN_RADIUS_RATIO = 2;

    var context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);

    var end_radius = canvas.width * CIRCLE_RADIUS_TO_CANVAS_RATIO;
    var begin_radius = end_radius * BEGIN_RADIUS_TO_END_RADIUS_RATIO;


    //console.log(offset);
    //console.log('ycoord: ' + ycoord + ', ' + 'xcoord: ' + xcoord);
    //console.log('centerY: ' + centerY + ', ' + 'centerX: ' + centerX);

    var radius = begin_radius;

    context.drawImage(img, 0, 0, img.width, img.height);
    draw();

    function draw() {
        context.fillStyle = '#8FAE8F';
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