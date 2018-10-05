$( document ).ready(function() {
  $(".profile-image").mouseenter(function(){
    $("#lateral-bar").css("width", "11vw");
  });

  $(".profile-image").mouseleave(function(){
    $("#lateral-bar").css("width", "9vw");
  });
});
