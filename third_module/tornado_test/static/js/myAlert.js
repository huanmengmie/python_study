function myAlert(options) {//鍙傛暟鏍煎紡{title:'Title',message:'message',callback:function(){alert('callback')}}or"闇€瑕佹彁绀虹殑璇�"
        var option={title:"鎻愮ず",message:"绋嬪簭鍛樺お鍌伙紝蹇樿杈撳叆鎻愮ず鍐呭鍟︹€︹€�",callback:function(){}}
        if(typeof(options)=="string"){
            option.message=options
        }else{
            option=$.extend(option,options);
        }
        var top=$(window).height()*0.3;
        $('body').append('<div class="myModa" style="z-index:999999"><div class="myAlertBox"  style="margin-top:'+top+'px"><p>'+option.message+'</p><div class="col2" style="text-align: center"><div class="btn sure" style="text-align: center">纭畾</div></div></div></div>');
        $('.btn.sure').click(function(){
            $('.myModa').remove();
        option.callback();
    })
}
 function myConfirm(options) {//鍙傛暟鏍煎紡{title:'Title',message:'message',callback:function(){alert('callback')}}or"闇€瑕佹彁绀虹殑璇�"$.myConfrim()
    var option={title:"鎻愮ず",message:"绋嬪簭鍛樺お鍌伙紝蹇樿杈撳叆鎻愮ず鍐呭鍟︹€︹€�",callback:function(){}}
    if(typeof(options)=="string"){
        option.message=options
    }else{
        option=$.extend(option,options);
    }
    var top=$(window).height()*0.3;
    $('body').append('<div class="myModa" style="z-index:999999"><div class="myAlertBox" style="margin-top:'+top+'px"><p>'+option.message+'</p><div class="col2" style="text-align: center"><div class="col" style=" width: 100px;"><div class="btn exit">鍙栨秷</div></div><div class="col" style="width: 100px; margin-left: 58px"><div class="btn sure">纭畾</div></div></div></div></div>');
    $('.btn.exit').click(function(){
        $('.myModa').remove();
    })
    $('.btn.sure').click(function(){
        $('.myModa').remove();
        option.callback();
    })
}
function loading(){

    var top=$(window).height()*0.3;   //class="myAlertBox"
    $('body').append('<div class="myModa" id="loading" style="z-index:999999;"><div class="myAlertBox"  style="margin-top:'+top+'px;width: 100px;background-color:rgba(255,255,255,0.1)"><p><i class="fa fa-spinner fa-spin fa-3x fa-fw" style="color: #e8874a;"></i></p></div></div>');
}
