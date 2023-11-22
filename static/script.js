// console.log("Script connected.");
// toggle navbar during mobile view
const hamburger = document.querySelector(".hamburger");
const navbar = document.querySelector(".navlist");

hamburger.addEventListener("click", ()=>{
    navbar.classList.toggle("slide");
});


// text typing animation  after record button, submit button is clicked

const textContainer1 = document.querySelector(".recording");
const text1 = "Recording...";

let index = 0;
let typingInterval;





// Get the record button element and add a click event listener
const startButton = document.getElementById("recordButton");
startButton.addEventListener("click", function() {

  function showNextCharacter() {
    textContainer1.textContent += text1.charAt(index);
    index++;
    
    if (index >= text1.length) {
      clearInterval(typingInterval);
    }
  }
  // Start the typing animation
  startTypingAnimation();
  function startTypingAnimation() {
    // Start the typing interval
    typingInterval = setInterval(showNextCharacter, 100);
  }

  // Stop the animation after 10 seconds
  setTimeout(function() {
    clearInterval(typingInterval);
    textContainer1.textContent = "";
  }, 10000);
  index = 0;
});


const textContainer2 = document.querySelector(".uploading");
const text2 = "File uploading...";

//Get the submit button element and add a click event listener
const submitButton = document.getElementById("sendbtn");
submitButton.addEventListener("click", function() {

  function showNextCharacter() {
    textContainer2.textContent += text2.charAt(index);
    index++;
    
    if (index >= text2.length) {
      clearInterval(typingInterval);
    }
  }
  // Start the typing animation
  startTypingAnimation();
  function startTypingAnimation() {
    // Start the typing interval
    typingInterval = setInterval(showNextCharacter, 100);
  }

  // Stop the animation after 10 seconds
  setTimeout(function() {
    clearInterval(typingInterval);
    textContainer2.textContent = "";
  }, 10000);
  index = 0;
});






// text slide show animation
const slider = document.querySelector(".slider");

const leftArrow = document.querySelector(".left");
const rightArrow = document.querySelector(".right");
const indicatorParents = document.querySelector(".controls ul");

var sectionIndex = 0;

function setIndex(){
  document.querySelector(".controls .selected").classList.remove("selected");
  slider.style.transform = "translate(" + (sectionIndex) * -25 +"%)";
}

document.querySelectorAll(".controls li").forEach(function(indicator, ind){
  indicator.addEventListener("click", function(){
    sectionIndex = ind;
    setIndex();
    indicator.classList.add("selected");
  });
});

leftArrow.addEventListener("click", function(){
  sectionIndex =  (sectionIndex > 0) ? sectionIndex - 1 : 0;
  setIndex();
  indicatorParents.children[sectionIndex].classList.add("selected");
  
});
      
rightArrow.addEventListener("click", function(){
  sectionIndex =  (sectionIndex < 3) ? sectionIndex + 1 : 3;
  setIndex();
  indicatorParents.children[sectionIndex].classList.add("selected");
  
});

// show result container after the analysis button clicked

const button = document.getElementById("complexityButton");
const resultdDiv = document.getElementById("result_container");
const timeComplexityDiv = document.getElementById("time_complexity_heading");
const wordCountDiv = document.getElementById("word_count_heading");

button.addEventListener('click', function() {
  // prompt("Button clicked");
  resultdDiv.classList.add('result_container');
  timeComplexityDiv.classList.add('time_complexity_heading');
  wordCountDiv.classList.add('word_count_heading');
});


