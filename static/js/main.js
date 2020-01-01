// var body = document.getElementById('header')
// $(document).ready(function(){
//   $('body').scroll(function(){
//     console.log('work')
//   });
// });

$(window).on('load', function () {
  setTimeout(preloader, 1000)
  function preloader() {
    $('#preloader').fadeOut();
  }
});
$(document).ready(function(){
  $('#open-menu').click(function () {
    console.log('WORK')
    $('#menu-mobile').addClass('open')
  });
  $('#close_menu_el').click(function () {
    $('#menu-mobile').removeClass('open')
  })

});
