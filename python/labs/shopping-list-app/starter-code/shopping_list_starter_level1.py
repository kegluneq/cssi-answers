#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

# Add an item to the list
def add_item():
  # Notice that I strip the input after receiving it.
  # This means that "blueberries" and "  blueberries " are the same.
  new_item = raw_input("What item should I add? ").strip()
  shopping_list.append(new_item)
  print("Added %s to your shopping list" % new_item)

# Remove an item from the list
def remove_item():
  item = raw_input("What item should I remove? ").strip()
  # Level 1: assume the item is in the list
  shopping_list.remove(item)
  print("Removed %s from your shopping list" % item)

# Check that an item is in the list
def check_item():
  print("Checking for items is not implemented yet")

# List all items
def list_items():
  # If only I had a pluralize function to use...
  print("Your shopping list has %s item(s):" % len(shopping_list))
  for item in shopping_list:
    print(" * %s" % item)

# The main program loop
while choice.lower() != "e":
  print("Please choose your action from the following list:")
  print("a. Add an item to the list")
  print("b. Remove an item from the list")
  print("c. Check to see if an item is on the list")
  print("d. Show all items on the list")
  print("e. exit")

  choice = raw_input("Enter your choice [a|b|c|d|e]: ").strip()

  if choice == "a":
    add_item()
  elif choice == "b":
    remove_item()
  elif choice == "c":
    check_item()
  elif choice == "d":
    list_items()
  elif choice != "e":
    print("I don't know what to do with your choice, %s" % choice)

  # Print a line to visually separate the previous command from the next one.
  print(("=" * 80) + "\n")
