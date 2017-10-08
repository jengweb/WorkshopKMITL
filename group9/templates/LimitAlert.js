window.onload = function onLoad() {
    var circle = new ProgressBar.Circle('#progress', {
       	  strokeWidth: 6,
		  easing: 'easeInOut',
		  duration: 1400,
		  color: '#708090',
		  trailColor: 'white',
		  trailWidth: 1,
		  svgStyle: null
    });

    circle.animate(0.3);



};