// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("Running Window Events Script");

// Challenge #5

function scrollHandler() {
  let windowPosition = window.scrollY;

  let rectangle = document.querySelector("#rect");
  if (windowPosition > 50) {
    // Challenge #5
    rectangle.style.backgroundColor = "black";

    // "DOM master" extension
    let domMasterParagraph = document.querySelector("#dom-master");
    domMasterParagraph.textContent = "Congratulations, you are a DOM master!";

  } else if (windowPosition < 50) {
    // "Added difficulty" extension
    rectangle.style.backgroundColor = "tomato";
  }

}

// Listen to the event the window creates when we scroll on the page.
window.addEventListener("scroll", scrollHandler);

// Challenge #4

window.addEventListener("keypress", e=> {
console.log("A key was pressed, it has code: " + e.keyCode);

// Get the purple box, which has id box6
let purpleBox = document.querySelector("#box6");

if (e.keyCode == 99) {
  console.log("Detected that the 'c' key was pressed");
  console.log("Turning the purple box into a smaller circle.");
  // Set the border radius, which effectively turns the box into a circle.
  purpleBox.style.borderRadius = "25px";
  // Shrink the box to half its former size.
  purpleBox.style.height = "50px";
  purpleBox.style.width = "50px";
} else if (e.keyCode == 115) {
  console.log("Detected that the 's' key was pressed");
  purpleBox.style.borderRadius = "";
  purpleBox.style.height = "100px";
  purpleBox.style.width = "100px";
}
})


// insert a function that prints out the key code of a key pressed
