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

# Multi-line comment!
"""
Most of our functions perform operations on shopping_list, changing what is in
the list. This would be a great candidate for a class!
The class would have:

def __init__(self):
  self.shopping_list = []

and define methods that add, remove, check, and delete items.

For extra credit, try to complete this exercise using a class.
"""
shopping_list = []


# Adds the item to your list and informs the user it was added.
# Warning: this function does not check for duplicates!
def add_item_and_confirm(item):
  shopping_list.append(item)
  print("Added %s to your shopping list" % item)


# Removes the item from your list and informs the user it was removed.
# Warning: this function does not check that the item is actually in the list.
# Make sure to check that before calling this function.
def remove_item_and_confirm(item):
  shopping_list.remove(item)
  print("Removed %s from your shopping list" % item)


# Add an item to the list
def add_items():
  # Notice that I strip the input after receiving it.
  # This means that "blueberries" and "  blueberries " are the same.
  from_user = raw_input("What item(s) should I add? ").strip()

  items = from_user.split(",")
  for new_item in items:
    # Reassign `new_item` to itself, but with whitespace trimmed.
    new_item = new_item.strip()
    # I don't want to add empty strings to my shopping list.
    if new_item != "":
      if new_item in shopping_list:
        print("%s is already in your list" % new_item)
      else:
        add_item_and_confirm(new_item)


# Remove an item from the list
def remove_item():
  item = raw_input("What item should I remove? ").strip()
  if item in shopping_list:
    is_sure = raw_input(
        "Are you sure you want to remove %s? [y|N]: " % item).strip()
    if is_sure == "y":
      remove_item_and_confirm(item)
    else:
      print("%s is still in your shopping list" % item)
  else:
    print("%s is not in your shopping list" % item)


# Check that an item is in the list
def check_item():
  item = raw_input("What item should I check for? ").strip()
  if item in shopping_list:
    print("%s is in your shopping list" % item)
    remove_it = raw_input(
        "Would you like to remove %s from your list? [y|N]: " % item).strip()
    if remove_it == "y":
      remove_item_and_confirm(item)
  else:
    print("%s is not in your shopping list" % item)
    add_it = raw_input(
        "Would you like to add %s to your list? [y|N]: " % item).strip()
    if add_it == "y":
      add_item_and_confirm(item)


# List all items
def list_items():
  # If only I had a pluralize function to use...
  print("Your shopping list has %s item(s):" % len(shopping_list))
  for item in shopping_list:
    print(" * %s" % item)


# Prints the menu of choices for the user.
def print_menu():
  print("a. Add an item to the list")
  print("b. Remove an item from the list")
  print("c. Check to see if an item is on the list")
  print("d. Show all items on the list")
  print("e. exit")


# The main program loop
while choice.lower() != "e":
  print("Please choose your action from the following list:")
  print_menu()

  # Strip spaces from the user's input and make it lower case.
  choice = raw_input("Enter your choice [a|b|c|d|e]: ").strip().lower()

  if choice == "a":
    add_items()
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
