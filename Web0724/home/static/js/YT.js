var r; //Youtube player

function onYouTubeIframeAPIReady() {
    var videotime = 0;
    var timeupdater = null;
    var e1 = document.getElementById("youtube-audio")

    //播放紐
    player_button = document.createElement("button");
    player_button.setAttribute("id", "youtube-icon");
    player_button.setAttribute("class","btn btn-sm btn-danger btn-circle")
    player_button.style.cssText = "cursor:pointer;cursor:hand";
    e1.appendChild(player_button);

    //播放icon
    button_icon = document.createElement("span");
    button_icon.setAttribute("id","icon-play");
    button_icon.setAttribute("class","align-items-center oi oi-media-play");
    player_button.appendChild(button_icon);

    //創造replace Iframe的div
    var YT_player = document.createElement("div");
    YT_player.setAttribute("id", "youtube-player");
    e1.appendChild(YT_player);

    var changeState = function(e) {
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

    r = new YT.Player("youtube-player", {
        height: "0",
        width: "0",
        videoId: e1.dataset.video,
        type: 'text/html',
        playerVars: {
            autoplay: e1.dataset.autoplay,
            loop: e1.dataset.loop,
            rel: "0",
            iv_load_policy: 3,
            playlist: e1.dataset.video,
        },
        events: {
            onReady: function(e) {
                r.setPlaybackQuality("small");
                onPlayerReady();
                changeState(r.getPlayerState() !== YT.PlayerState.CUED);
            },
            onStateChange: function(e) {
                e.data === YT.PlayerState.ENDED && r.playVideo() ;
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
      if(currentTime > 1) {
        handleProgress(r.getCurrentTime(),r.getDuration());
      }
    }
}

