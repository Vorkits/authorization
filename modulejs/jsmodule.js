
function redirect_to_auth(provider,url){
    window.location = `http://ralae.com/${provider}/?url=${url}`
}
document.addEventListener("DOMContentLoaded", function(){
    console.log('start')
    vk=document.getElementById('vkauth')
    gmail=document.getElementById('gmailauth')
    facebook=document.getElementById('facebookauth')
    yandex=document.getElementById('yandexauth')
    mailru=document.getElementById('mailruauth')
    ok=document.getElementById('okauth')
    url=document.getElementById('authwidget').getAttribute('data-url-auth');
    console.log(url)
    vk.addEventListener('click', function(){
        redirect_to_auth('vk',url);
     });
     gmail.addEventListener('click', function(){
        redirect_to_auth('google',url);
     });
     facebook.addEventListener('click', function(){
        redirect_to_auth('facebook',url);
     });
     yandex.addEventListener('click', function(){
      redirect_to_auth('yandex',url);
   });
   mailru.addEventListener('click', function(){
      redirect_to_auth('mailru',url);
   });
   ok.addEventListener('click', function(){
      redirect_to_auth('ok',url);
   });
     
});