var currentTrack = null;
var paused = false;

$(document).ready(function(){
    var a = document.getElementById("currentTrack");
    currentTrack = a.getAttribute("value");
    //currentTrack = $('#currentTrack').val();

    $('#play').click(function(){
        let y = document.getElementById("currentTrack");
        alert(y.innerHTML);
        play();
    });
    $('#stop').click(function(){
        stop();
    });
    $('#pause').click(function(){
        pause();
    });
});


function play(){
    if (pause == false){
        stop();
       // currentTrack = $('#currentTrack').val();
       currentTrack = a.getAttribute("value");
       document.getElementById(currentTrack).load();
    }
    document.getElementById(currentTrack).play();
}

function stop(){
    if (currentTrack) {
        document.getElementById(currentTrack).pause();
        paused = false;
    }
}

function pause(){
    paused = true;
    document.getElementById(currentTrack).pause();
}

