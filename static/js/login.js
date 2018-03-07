$(function(){

        name_error = false;
        pwd_error = false;

        if(true){
           $('.name_input').next().html('请输入5-20个字符的用户名')
		   $('.name_input').next().show();
        }

        if({{error_name}}==1){
           $('.user_error').html('user name is incorrect').show();
        }

        if({{error_pwd}}==1){
           $('.pwd_error').html('password is incorrect').show();
        }

        if('.name_input').blur(function(){
          if($('.name_input').val().length==0){
              $('.user_error').html('please fill the user name').show();
              name_error=false;
          }else{
              $('.user_error').hide();
              name_error=true;
          }
        )};

        $('.pass_input').blur(function(){
            if($(this).val().length==0){
                $('.pwd_error').html('please input the password').show();
                pwd_error=false;
            }else{
                $('.pwd_error').hide();
                pwd_error=true;
            }
         });

         $('form').submit(function(e){
                  alert("Submitted");
         });
     })