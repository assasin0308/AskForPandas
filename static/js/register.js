/*网页加载完成时执行*/
function bindEmailCaptchaClick(){
     $('#captcha-btn').click(function(event){
         var $this = $(this); /*获取当前jQuery对象*/


         event.preventDefault()

         email = $("input[name='email']").val();
         console.log('获取到的邮箱账号:  ' + email);
         $.ajax({
             url: "/auth/captcha/email?email=" + email,
             method: "GET",
             dataType: "json",
             success: function (result) {
                 console.log(result);
                 if (result.code == 200) {
                     //倒计时60秒
                     var countdown = 60;
                     /*取消按钮的点击事件*/
                     $this.off("click");
                     var timer = setInterval(function(){
                         $this.text(countdown + 's');
                         $this.css('color',  'blue');   // 设置文本颜色为蓝色
                         countdown -= 1;

                         if(countdown <= 0) {
                             /*清除定时器*/
                             clearInterval(timer);
                             /*修改按钮文字*/
                             $this.text('获取验证码');
                             /*重新绑定点击事件*/
                             bindEmailCaptchaClick();


                         }

                     },1000)



                     alert("邮箱验证码发送成功!")
                 }else{
                      alert(result.msg)
                 }
             },
             fail: function(error){
                console.log(error)
             }

         });
     });
}




$(function(){

     /*发送邮箱验证码*/
    bindEmailCaptchaClick();



});
