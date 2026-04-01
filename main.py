# Import the PostfixCalculator class
from postfix_calculator import PostfixCalculator


def run_test_case(calculator, variables, expression, case_name):
    # Print a separator for readability
    print("\n" + "=" * 60)

    # Print the name of the test case
    print(case_name)

    # Print another separator
    print("=" * 60)

    # STEP 1: Insert variables into the BST
    print("\nSetting variables:")

    # Loop through each (key, value) pair
    for key, value in variables:
        # Insert variable into the calculator's BST
        calculator.set_variable(key, value)

        # Print confirmation
        print(f"  {key} = {value}")

    # STEP 2: Show postfix expression
    print(f"\nPostfix Expression: {expression}")

    # STEP 3: Display BST structure
    print("\nBinary Search Tree:")

    # Call display method from BST
    calculator.variable_tree.display_tree()

    # STEP 4: Evaluate postfix expression
    try:
        # Call evaluation method
        result = calculator.evaluate_postfix_expression(expression)

        # Print the result
        print(f"\nResult: {result}")

    except Exception as error:
        # Catch any errors (invalid expression, etc.)
        print(f"\nError: {error}")

    # STEP 5: Delete all variables
    calculator.delete_all_variables()

    # Confirm deletion
    print("\nAll variables deleted.")

    # STEP 6: Display BST again to confirm it's empty
    print("\nBinary Search Tree after delete_all():")

    # Should now show empty tree
    calculator.variable_tree.display_tree()


def main():
    # Print welcome message explaining the program
    print("Welcome to the Postfix Calculator with BST")
    print("This program evaluates postfix expressions using a stack")
    print("and stores variables in a binary search tree.\n")

    # Create a calculator object
    calculator = PostfixCalculator()

    # Define test case variables and expressions

    variables1 = [("x", 5), ("y", 3), ("z", 4)]
    expression1 = "x y + z *"

    variables2 = [("a", 2), ("b", 3), ("c", 4)]
    expression2 = "a b c + *"

    variables3 = [("m", 8), ("n", 2), ("p", 3)]
    expression3 = "m n / p +"

    variables4 = [("q", 7), ("r", 3), ("s", 2)]
    expression4 = "q r - s *"

    variables5 = [("d", 1), ("e", 2), ("f", 3)]
    expression5 = "d e + f +"

    variables6 = [("g", 2), ("h", 3), ("i", 4), ("j", 5)]
    expression6 = "g h i + * j /"

    variables7 = [("k", 2), ("l", 3), ("m", 4), ("n", 5)]
    expression7 = "k l * m n + +"

    variables8 = [("o", 9), ("p", 3), ("q", 5), ("r", 2), ("s", 7)]
    expression8 = "o p / q r * + s -"

    # Run all test cases one by one

    run_test_case(calculator, variables1, expression1, "Postfix Expression 1")
    run_test_case(calculator, variables2, expression2, "Postfix Expression 2")
    run_test_case(calculator, variables3, expression3, "Postfix Expression 3")
    run_test_case(calculator, variables4, expression4, "Postfix Expression 4")
    run_test_case(calculator, variables5, expression5, "Postfix Expression 5")
    run_test_case(calculator, variables6, expression6, "Postfix Expression 6")
    run_test_case(calculator, variables7, expression7, "Postfix Expression 7")
    run_test_case(calculator, variables8, expression8, "Postfix Expression 8")


# This ensures the program only runs when executed directly
if __name__ == "__main__":
    main()