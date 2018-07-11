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

console.log("Running Click Events Script");

// Challenge #1
function setColorOfBoxesTo(color) {
  // Get all of the boxes.
  // We ask for anything with class "box" that is a child of the element with
  // id "container1".
  let boxes = document.querySelectorAll("#container1 .box");
  for (let i = 0; i < boxes.length; i++) {
    boxes[i].style.backgroundColor = color;
  }
}

// Add a handler to the red box.
function handleRedClick() {
  console.log("I'm handling a red click");
  setColorOfBoxesTo("red");
}
let redBox = document.querySelector("#box1");
redBox.addEventListener("click", handleRedClick);

// Add a handler to the pink box.
function handlePinkClick() {
  console.log("I'm handling a pink click");
  setColorOfBoxesTo("pink");
}
let pinkBox = document.querySelector("#box2");
pinkBox.addEventListener("click", handlePinkClick);

// Add a handler to the orange box.
function handleOrangeClick() {
  console.log("I'm handling an orange click");
  setColorOfBoxesTo("orange");
}
let orangeBox = document.querySelector("#box3");
orangeBox.addEventListener("click", handleOrangeClick);
