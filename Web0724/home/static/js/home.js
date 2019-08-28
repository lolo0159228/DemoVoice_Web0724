
$(document).ready(function(){

    $('.yt-id').click(function(){
        $('#youtube-audio').attr('data-video',$(this).attr('data-YtId'));
        r.loadVideoById($(this).attr('data-YtId'),1); //用videoid loading youtube
        progressbar.style.cssText = 'width:0%'; //progress bar 進度歸零
        $("#icon-play").addClass(" oi-media-pause").removeClass(" oi-media-play");
        $('#currentTrack').text($(this).attr('data-Yttitle'));
        $('#anchor').text($(this).attr('data-Ytauthor'));
    });

});