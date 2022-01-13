
function redirect_to_auth(provider,url){
    window.location = `http://ralae.com/${provider}/?url=${url}`
}
document.addEventListener("DOMContentLoaded", function(){
    console.log('start')
    vk=document.getElementById('vkauth')
    gmail=document.getElementById('gmailauth')
    url=document.getElementById('authwidget').getAttribute('data-url-auth');
    console.log(url)
    vk.addEventListener('click', function(){
        redirect_to_auth('vk',url);
     });
     gmail.addEventListener('click', function(){
        redirect_to_auth('google',url);
     });
     
});