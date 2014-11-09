var question_form = $('#question_form');

var sucess_post = function(data){
    console.log(data);
}

var error_post = function(data){
    console.log(data.responseJSON);
}

form_ajax(question_form, sucess_post, error_post);
