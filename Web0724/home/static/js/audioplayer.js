var currentTrack = null;
var paused = true;
var audio = null;
var a = null;

$(document).ready(function(){
    a = document.getElementById("currentTrack");
    currentTrack = a.getAttribute("value");
    audio = "<audio  id='Rock' src='/static/uploads/Sleep_Away.mp3' preload='auto'></audio>";
    getaudio();
    //currentTrack = $('#currentTrack').val();

    $('#play').click(function(){
        //document.getElementById("play").innerHTML="<audio  id='Rock' src='/static/uploads/Sleep_Away.mp3' preload='auto'></audio>";
        /*let y = document.getElementById("currentTrack");
        1alert(y.innerHTML);  test用*/
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
        currentTrack = a.getAttribute("value");
        $('#icon-audio').addClass(" oi-media-play").removeClass(" oi-media-pause");
        //document.getElementById('icon-audio').innerHTML+= "<span class='oi oi-media-play'></span>";
       // currentTrack = $('#currentTrack').val();
       document.getElementById(currentTrack).pause();
       pause = true;
    }else{
        $('#icon-audio').addClass(" oi-media-pause").removeClass(" oi-media-play");
        //document.getElementById('icon-audio').innerHTML+=  "<span class='text-center oi oi-media-pause'>";
        //currentTrack = a.getAttribute("value");
        //document.getElementById(currentTrack).load(); 重載更新
        document.getElementById(currentTrack).play();
        pause = false;
    }

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

function getaudio(){
    document.getElementById('play').innerHTML+= audio;
}

