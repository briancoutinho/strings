
/*-------------------------------------------------
  Web program to run on the client side
  Dependancy - jquery is used to handle most DOM tasks
-------------------------------------------------*/

var app = new function () {

$( document ).ready(function() {
 
    $("#journal").append("<h4> Who let the dogs out</h4>");

    // Tab switching
    //Journal
    $("#header a")
        .eq(0)
        .click(function () {
           $("#journal").show(); 
           $(this).attr("id", "selected");
        })
        .end();
    // --> Tasks
    $("#header a")
        .eq(1)
        .click(function () {
           $("#journal").hide(); 
           $(this).attr("id", "selected");
        });

 });



} (); // modular and auto invoked
