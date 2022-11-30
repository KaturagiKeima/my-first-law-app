function clickEvent() {
    alert('成功！');
}

$(function() {

    // show popupボタンクリック時の処理
    $('#show').click(function(e) {
        $('#popup, #layer').show();
    });

    // レイヤー/ポップアップのcloseボタンクリック時の処理
    $('#close, #layer').click(function(e) {
        $('#popup, #layer').hide();
    });

});

jQuery('.my-parts').on('click', function() {
	if(jQuery('.nav.menubar').css('display') === 'block') {
		jQuery('.nav .menubar').slideUp('1500');
	}else {
		jQuery('.nav .menubar').slideDown('1500');
	}
});


    
