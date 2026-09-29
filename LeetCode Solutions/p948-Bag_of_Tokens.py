# Greedy solution for the Bag of Tokens problem.
# Sort tokens, then use the smallest token when possible and the largest token when needed.
def bagOfTokens(tokens, power):
    # Sort tokens so the smallest value is at the left and largest at the right.
    tokens.sort()

    left = 0
    right = len(tokens) - 1
    score = 0
    maxScore = 0

    while left <= right:
        # If we have enough power to face the smallest token, gain a score.
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1

            if score > maxScore:
                maxScore = score

        # Otherwise, if we have score and there is a larger token to trade, spend one score
        # to increase power and continue exploring other options.
        elif score >= 1 and left < right:
            power += tokens[right]
            score -= 1
            right -= 1

        else:
            break

    return maxScore


# Read tokens and starting power from the user.
tokens = list(map(int, input("Enter tokens(separated by spaces): ").split()))
print(tokens)
power = int(input("Enter power: "))
print(f"Max Score: {bagOfTokens(tokens, power)}")

