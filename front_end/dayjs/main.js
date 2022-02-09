// get the modal element
var modal = document.getElementById("simpleModal");
// Get modal button
var modalBtn = document.getElementById("modalBtn");
// Get close button
var closeBtn = document.getElementsByClassName("closeBtn")[0];

// listen for a open click

modalBtn.addEventListener("click",openModal);

// listen for close click

closeBtn.addEventListener("click",closeModal);

// listen for outside click

window.addEventListener("click",outsideclick)

// function to open model

function openModal(){
    modal.style.display = "block"
}

// function to close model

function closeModal(){
    modal.style.display = "none"
}

// function to close model if outside click

function outsideclick(e){
    if(e.target == modal){
    modal.style.display = "none"
    }
}
