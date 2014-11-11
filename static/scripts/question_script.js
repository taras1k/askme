var question_form = $('#question_form');
var progress = $('#progress');
var progress_bar = $($('#progress-bar')[0]);
var answer = $('#answer');
var answer_text = $('#answer_text');
var description = $('#description');
var error_block = $('#error_block');
var question_form_group = $('#question_form_group');

var sucess_post = function(data){
    question_form.hide();
    var counter = 0;
    progress.show();
    var looper = setInterval(function(){
        counter += 2;
        progress_bar.width(counter+'%');
        if (counter > 100)
        {
            clearInterval(looper);
            progress.hide();
            progress_bar.width('0%');
            answer_text.html(data.answer);
            description.hide();
            answer.fadeIn();
        }
     }, 80)
}

var error_post = function(data){
    error_block.html(data.responseJSON.error);
    question_form_group.addClass('has-error');
    console.log(data.responseJSON);
}

form_ajax(question_form, sucess_post, error_post);
