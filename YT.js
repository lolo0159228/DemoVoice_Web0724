/*function onYoutubeIframeAPIReady(){

    var q = document.getElementById('youtube-audio');

 //   var icon = document.createElement("span");
 //   icon.setAttribute("id","youtube-icon");
 //   icon.setAttribute("class","oi oi-media-play");
 //   q.appendChild(icon);

    var div = document.createElement("div");
    div.setAttribute("id","player");
    q.appendChild(div);

    var toggleButton = function (play){
        if (play == true){
            $('#youtube-icon').addClass(" oi-media-pause").removeClass(" oi-media-play");
        }else{
            $('#youtube-icon').addClass(" oi-media-play").removeClass(" oi-media-pause");
        }
    }

    q.onclick = function(){
        if (player.getPlayerState() === YT.PlayerState.PLAYING || player.getPlayerState() === YT.PlayerState.BUFFERING){
            player.pauseVideo();
            toggleButton(false);
        }else{
            player.playVideo();
            toggleButton(true);
        }
    }

    var player = new YT.Player('player',{
        height: '0',
        width: '0',
        videoId:q.dataset.video,
        playerVars:{
            autoplay: q.dataset.autoplay,
            loop: q.dataset.loop,
        },
        events: {
            'onReady': function(e){
                player.setPlaybackQuality("small");
                toggleButton(player.getPlayerState() !== player.PlayerState.CUED);
            },
            'onStateChange': function(e){
                if (e.data === player.PlayerState.ENDED){
                    toggleButton(false);
               }
            }
        }
    });

}*/

function onYouTubeIframeAPIReady() {
    var videotime = 0;
    var timeupdater = null;
    var e = document.getElementById("youtube-audio"),

    //播放紐
    player_button = document.createElement("button");
    player_button.setAttribute("id", "youtube-icon");
    player_button.setAttribute("class","btn btn-sm btn-danger btn-circle")
    player_button.style.cssText = "cursor:pointer;cursor:hand";
    e.appendChild(player_button);

    //播放icon
    button_icon = document.createElement("span");
    button_icon.setAttribute("id","icon-play");
    button_icon.setAttribute("class","align-items-center oi oi-media-play");
    player_button.appendChild(button_icon);

    //創造replace Iframe的div
    var YT_player = document.createElement("div");
    YT_player.setAttribute("id", "youtube-player");
    e.appendChild(YT_player);

    var changeState = function(e) {
        //var a = e ? "IDzX9gL.png" : "quyUPXN.png";
        //t.setAttribute("src", "https://i.imgur.com/" + a)
        if (e == 0) {
            $("#icon-play").addClass(" oi-media-play").removeClass(" oi-media-pause");
        }else{
            $("#icon-play").addClass(" oi-media-pause").removeClass(" oi-media-play");
        };

    };

    player_button.onclick = function() {
        if (r.getPlayerState() == YT.PlayerState.PLAYING || r.getPlayerState() == YT.PlayerState.BUFFERING) {
            r.pauseVideo();
            changeState(0);
        }else {
            r.playVideo();
            changeState(1);
        };

    };

    var r = new YT.Player("youtube-player", {
        height: "0",
        width: "0",
        videoId: e.dataset.video,
        playerVars: {
            autoplay: e.dataset.autoplay,
            loop: e.dataset.loop
        },
        events: {
            onReady: function(e) {
                r.setPlaybackQuality("small");
                onPlayerReady();
                changeState(r.getPlayerState() !== YT.PlayerState.CUED);
            },
            onStateChange: function(e) {
                e.data === YT.PlayerState.ENDED && changeState(0) ; //先改成1 播完時，重複播，loop不知道為啥無效，再研究
            }
        }
    });


    function onPlayerReady() {
      function updateTime() {
        var oldTime = videotime;
        if(r && r.getCurrentTime) {
          videotime = r.getCurrentTime();
        }
        if(videotime !== oldTime) {
          onProgress(videotime);
        }
      }
      timeupdater = setInterval(updateTime, 100);
    }

    // when the time changes, this will be called.
    function onProgress(currentTime) {
      if(currentTime > 10) {
        handleProgress(r.getCurrentTime(),r.getDuration());
      }
    }
}

