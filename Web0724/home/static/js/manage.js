var containerDOM = null;

$(document).ready(function(){
    containerDOM = document.getElementById("container");
    $(".like").click(function(){
        var like = $(this).prop('value');
        if (like == 'N'){
             $(this).addClass("btn-danger").removeClass("btn-light").attr('value','Y');
         }else{
             $(this).addClass("btn-light").removeClass("btn-danger").attr('value','N');
        };
    });

    $(".play-voice").click(function(){
        var b = $(this).text();
        getaudio(b+'.mp3');
        play();
    });

    $('.replay').click(function(){
        launchAJAX();
    });

});


function getaudio(Songname){
    let Rock = document.getElementById('Rock');
   //document.getElementById('play').innerHTML+= "<audio  id='Rock' src='/static/uploads/"+Songname+"' preload='auto'></audio>";
    if (Rock == null){
        document.getElementById('play').innerHTML+= "<audio  id='Rock' src='"+Songname+"' preload='auto' loop='true'></audio>";
    }else{
        $('#Rock').attr('src',Songname);
        play();
    }
    a.innerHTML=Songname;
}

//利用AJAX取得資料
function launchAJAX(){
    $.ajax({
        type: 'GET',
        url: 'http://api.jirengu.com/fm/getSong.php',
        dataType: 'json',
        success: function(response){
            var m = response.song[0];
            let anchor = document.getElementById('anchor');
            getaudio(m.url);
            a.innerHTML = m.title;
            anchor.innerHTML = m.artist;
            play();

        },
    })

};

function PageAJAX(hash){
    let url = 'http://127.0.0.1:8000/%5Ehome/'+hash;
    $.ajax({
        type: 'GET',
        url: url,
        dataType: 'html',
        success: function(html){
            setPjaxContainer(html);
            launchPushState(hash);
        },
    });
};

function setPjaxContainer(html){
    containerDOM.innerHTML = html;
};

function launchPushState(hash){
    let name = hash.match(/(.*)/)[1];
    let stateObj = {index:name};
    window.history.pushState(stateObj,name,hash);
};