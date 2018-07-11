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
window.addEventListener("keypress", e=> {
console.log("A key was pressed, it has code: " + e.keyCode);
// Get the purple box, which has id box6
let purpleBox = document.querySelector("#box6");
console.log("Turning the purple box into a smaller circle.");
// Set the border radius, which effectively turns the box into a circle.
purpleBox.style.borderRadius = "25px";
// Shrink the box to half its former size.
purpleBox.style.height = "50px";
purpleBox.style.width = "50px";
})


// insert a function that prints out the key code of a key pressed
