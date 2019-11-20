function simulation(sim){ // like like_thread
    var to_url = $(sim).attr('data-to-url'); 
    // var from_url = $(sim).attr('data-from-url');
    var action = $(sim).attr('data-action');
    var ajaxdata = {
        // from_url: from_url,
        action: action,
    };
    $.ajax({
        url: to_url,
        data: JSON.stringify(ajaxdata),
        dataType: 'json',
        method: 'POST',
        beforeSend: function (xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token)
        },
        // success: function(result){
        //     var sentences = '';
        //     // var swither = true;
        //     for (var key in result) {
        //         // swither?
        //         sentences += '<h5 class="text-success-sim-info"><i>'+key+': '+result[key]+'</i></h5><hr class="my-4">'; //:
        //         // sentences += '<h5 class="text-info translated_sentences"><i>'+sim[key]+'</i></h5><hr class="my-4">';
        //         // swither = !swither;
        //     };
        //     // console.log(sentences);
        //     $('#simulation_info').html(sentences);
        // }
    });
};
// data-id // onclick
function refresh_simulation(sim){
    var to_url = $(sim).attr('data-to-url'); 
    var from_url = $(sim).attr('data-from-url');
    var ajaxdata = {
        from_url: from_url,
    };
    $.ajax({
        url: to_url,
        data: JSON.stringify(ajaxdata),
        dataType: 'json',
        method: 'POST',
        beforeSend: function (xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token)
        },
        success: function(result){
            for (var key in result) {
                var sentence = '';
                sentence = key + ': ' + result[key]
                $("#" + key + "").text(sentence);
            };
        }
    });
};

//${id}