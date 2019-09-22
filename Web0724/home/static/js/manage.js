var containerDOM = null;

$(document).ready(function(){
    containerDOM = document.getElementById("container");
   /* var liketags = document.getElementsByClassName('likeactive')
    for (let i=0; i<liketags.length;i++){

    }
*/
    $(".like").click(function(){
        var likeA = this.getAttribute("class")  //this.getElementsByClassName('likeactive').length ==0
        if (likeA.match('likeactive')){
            var likeYN = true
            $(this).addClass("btn-light").removeClass("btn-danger likeactive").attr('value','N');
        }else{
            var likeYN = false
            $(this).addClass("btn-danger likeactive").removeClass("btn-light").attr('value','Y');
        }

        $.ajax({
            url: this.dataset.url,
            type:'GET',
            dataType:'json',
            data:{
                likeYN: likeYN,
                sid: this.dataset.sid,
                SongName: this.getElementsByTagName('p')[0].innerHTML
            },
            cache:false,
            success:function(data){
                console.log(data)
            },
            error:function(e){
                console.log(e)
            }

        });

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