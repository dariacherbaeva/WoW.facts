$('.likes-button').click(function(){
    var ansid;
    ansid = $(this).attr("data-ansid");
            $.get('/blog/add_like/', {answer_id: ansid}, function(data){
        $('#like_count').html(data);
    $('#likes').hide();
});
});
