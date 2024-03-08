###############################################################################
# TODO: 1. (6 pts)
#
#   For this _TODO_, we are going to bring together many of the concepts that
#   we have learned.
#
#   We will be creating a basic recipe book where a user can enter a recipe
#   name and some ingredients for each recipe. It should ask the user for more
#   ingredients until the user is done with that recipe's ingredient list.
#   Then, it should prompt them to do another recipe until they are done
#   entering recipes.
#
#   You will use a dictionary for each recipe that has two fields:
#       - name          <-- this is a string
#       - ingredients   <-- this is a set of strings
#
#   As you go, you should add the dictionaries to a list called recipes. So in
#   the end you should have a list of dictionaries.
#   
#   Here is a step-by-step breakdown of how this should work:
#
#       1. Prints "Welcome to Recipe Book!"
#       2. Prompts the user to enter a recipe name like this:
#           "Please enter a recipe name: "
#          and saves it to the key "name" in a dictionary
#       3. Prompts the user to enter an ingredient like this:
#           "Please enter an ingredient: "
#          and adds it to a set of ingredients
#       4. Repeat step 3 until the user types "end" and then saves the set of
#          ingredients to the key "ingredients" in the dictionary.
#       5. Repeat steps 2-4 until the user types "end" and then adds the
#          dictionary to the list of recipes.
#       6. Prints the list of recipes one recipe at a time (HINT: use a loop
#          here)
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
print("Welcome to Recipe Book!")
name = input("Please enter a recipe name: ")
def ingredients_list():
    total = 0
    while True:
        user_input = str(input("Please enter an ingredient (When you are finished adding ingredients type end): "))
        if user_input == "end":
                break
        total += user_input
        print(f"The ingredients are {total}.")
ingredients = ingredients_list()


###############################################################################
# TODO: 2. EXTRA CREDIT (2 pts)
#
#   For this extra credit _TODO_, try to look into how you could print out the
#   recipes in a better format that is a little easier to read. Your solution
#   should print things on multiple lines. Modify your code above to do this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
