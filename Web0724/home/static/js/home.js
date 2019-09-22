
$(document).ready(function(){

    $('.yt-id').click(function(){
        $('#youtube-audio').attr('data-video',$(this).attr('data-YtId'));
        r.loadVideoById($(this).attr('data-YtId'),1); //用videoid loading youtube
        progressbar.style.cssText = 'width:0%'; //progress bar 進度歸零
        $("#icon-play").addClass(" oi-media-pause").removeClass(" oi-media-play");
        $('#currentTrack').text($(this).attr('data-Yttitle'));
        $('#anchor').text($(this).attr('data-Ytauthor'));
    });

    $('.Add-Song').click(function(){
        //console.log(this.dataset.ytid)
        //console.log(this.dataset.yttitle)
        //console.log(this.dataset.ytauthor)
        $.ajax({
            url:this.dataset.url,
            type: 'GET',
            dataType:'json',
            cache:false,
            data:{
                VoiceSrc: this.dataset.ytid,
                VoiceSongname: this.dataset.yttitle,
                VoiceAuthor: this.dataset.ytauthor
            },
            success:function(data){
                alert(data['message'])
                //console.log(data)
            },
            error:function(e){
                console.log(e)
               // console.log(e['message'])
            }
        });

    });

    $('#SearchBtn').click(function(){
        var q = document.getElementById('inputSmall')
        $.ajax({
            url: this.dataset.url,
            type:'GET',
            dataType:'json',
            cache:false,
            data:{
                Query:q.value,
                page:1
            },
            success:function(data){
                var string = '';
                $.each(data,function(index,value){
                    let i = data[index][1].id
                    let t = data[index][1].Songname
                    let a = data[index][1].author
                    string = string +
                     '<li class="list-group-item" data-YtId="'+i+'">'+
                     '<button type="button" class="btn btn-sm btn-light btn-circle yt-id" data-YtId="'+i+'" data-Yttitle="'+t+'" data-Ytauthor="'+a+'"> <span class="oi oi-media-play"></span> </button>'+
                     '<p>'+t+'</p>'+
                     '</li>'
                  // console.log(data[index][1])
                });


                $('#search-list').html(
                '<ul class="list-group list-group-flush"> '+string+'</ul>')

                PJAX_loadJS('JS','/static/js/home.js');
            },
            error:function(e){
                console.log(e)
            }
        })
    });

});