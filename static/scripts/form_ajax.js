function form_ajax(form, sucessCallback, errorCallback){
  form.find('button[type=submit]').on('click', function(e){
    e.preventDefault();
    $.ajax({
      url: form.attr('action'),
      method: 'POST',
      data: form.serialize(),
      success: function(data){
        if(sucessCallback){
          sucessCallback(data);
        };
      },
      error: function(data){
        if(errorCallback){
          errorCallback(data);
        }
      }
    });
  });
}
