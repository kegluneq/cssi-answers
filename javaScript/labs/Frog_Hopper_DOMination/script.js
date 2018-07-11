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

let currentlily = 1;

let frogger = document.querySelector("#frog");

frogger.addEventListener("click", function(){
  // Move to the second lily pad.
  frogger.style.left = "33.5%";
  frogger.style.top = "25%";
  // Grab the previous lily pad.
  let prevPad = document.querySelector("#lilypad" + currentlily);
  // Remove the "glow", represented by the "active" class.
  prevPad.classList.remove("active");

  // Update the current lily pad.
  currentlily = 2;
  let nextPad = document.querySelector("#lilypad" + currentlily);
  // Add the "glow", represented by the "active" class.
  nextPad.classList.add("active");
});

// Add a handler for when the user puts the mouse over the frog.
frogger.addEventListener("mouseover", function() {
  frogger.style.height = "80px";
  frogger.style.width = "80px";
});

// Add a handler for when the user's mouse leaves the frog.
frogger.addEventListener("mouseout", function() {
  frogger.style.height = "";
  frogger.style.width = "";
});

window.addEventListener("keypress", function(e) {
  if (e.keyCode == 32) {
    currentlily = 1;
    frogger.style.left = "";
    frogger.style.top = "";

    for (let i = 1; i < 6; i++) {
      document.querySelector("#lilypad" +i).classList.remove("active");
    }

    document.querySelector("#lilypad1").classList.add("active");
  }
});
