
function change_slide(index){
    let dots = document.getElementsByClassName("dot");
    let slides = document.getElementsByClassName("blog_cards");
    dots[index-1].className +=" active";
    slides[index-1].style.display="block";
    for(let i=0; i<dots.length ;i++ ){
        if(i != index-1){
            slides[i].style.display="none";
            dots[i].className="dot";
        }
    }
}

function openform() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }

function popup(){
    document.getElementById("popUp").className="popUp";
    document.getElementById("cover").className="cover";
}
function revert(){
    document.getElementById("popUp").className="nothing";
    document.getElementById("cover").className="nothing";
}