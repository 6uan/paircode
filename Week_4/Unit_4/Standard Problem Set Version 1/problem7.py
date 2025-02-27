'''
Problem 7: Validate NFT Addition
You want to ensure that NFTs are added in a balanced way. For example, every "add" action must be
properly closed by a corresponding "remove" action.

Write the validate_nft_actions() function, which takes a list of actions (either "add" or "remove")
and returns True if the actions are balanced, and False otherwise.

A sequence of actions is considered balanced if every "add" has a corresponding "remove" and no "remove" occurs before an "add".

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def validate_nft_actions(actions):
    pass
Example Usage:

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))
Example Output:

True
True
False
'''

# For this solution our time would be O(n) and space would be O(n)
# Our stack will grow based on actions
# We will loop n times through the actions
# And for each action we will perform an O(1) operation on it

def validate_nft_actions(actions):
    stack = []

    for action in actions:
        if action == "add":
            stack.append(action)
        elif action == "remove":
            if not stack:
                return False
            else:
                stack.pop()

    return True

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))