$( document ).ready(function() {

  $(".profile-image").mouseenter(function(){
    $("#lateral-bar").css("width", "11vw");
    $(this).css("filter", "grayscale(0%)");

    current_profile = this.id.split('-')[1];
    student_box_pos = 1 + parseInt(this.id.split('-')[2])*(7);

    image_url = "img/"+current_profile+".jpg"

    $(this).css("width", "8vw");
    $(this).css("height", "8vw");
    $("#student-box").css({top: student_box_pos.toString()+"vw"});
    $("#student-box").show();

    $("#student-box-picture").css("background-image", "url("+image_url+")");

    $("#box-name").html($(this).data("name"));
    $("#box-number").html($(this).data("number"));
    $("#box-role").html($(this).data("role"));
  });

  $(".profile-image").mouseleave(function(){
    $(this).css("width", "6vw");
    $(this).css("height", "6vw");
    $("#lateral-bar").css("width", "9vw");
    $(this).css("filter", "grayscale(100%)");
    $("#student-box").hide();
  });

  $(".assignment-image").mouseenter(function(){
    $(this).css("filter", "grayscale(0%)");
  });

  $(".assignment-image").mouseleave(function(){
    $(this).css("filter", "grayscale(100%)");
  })

});
