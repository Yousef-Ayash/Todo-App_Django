// * Top Part of The Task (Name, Update and Delete) Start * //
var task_name = document.getElementsByClassName("task-name");

var accessData = function() {
    var t_attr = this.getAttribute("data-el");
    var b_ele = document.querySelector("[data-b='" + t_attr + "']");
    
    if (b_ele.style.display == "flex") {
        b_ele.style.display = "none";
    }
    else {
        b_ele.style.display = "flex";
    }
}

for (var i = 0; i < task_name.length; i++) {
    task_name[i].addEventListener("click", accessData, false);
}
// * Top Part of The Task (Name, Update and Delete) End * //

//!
//?
//!
            
var cnDlt = document.getElementById('confirm-delete');

function show_delete() {
    cnDlt.style.display = "flex";
}
function hide_delete() {
    cnDlt.style.display = "none";
}
