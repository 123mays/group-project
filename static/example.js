/*
This JavaScript file adds interactive functionality to a webpage by defining event handlers and 
functions to respond to user interactions. 

Author: Kellen Knop

*/

function addDropdownItem() {
  alert("Button clicked!");
}

the_title = document.getElementById("hello");

old_color = the_title.style.color

the_title.onmouseenter = function(){
	the_title.style.color = "purple";
  the_title.style.textDecoration = "underline";
}

the_title.onmouseout = function(){
	the_title.style.color = old_color;
  the_title.style.textDecoration = "none";
}
