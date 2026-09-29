def bagOfTokens(tokens, power):
    tokens.sort()
    
    left = 0
    right = len(tokens) - 1
    score = 0
    maxScore = 0
    
    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            
            if score > maxScore:
                maxScore = score
                
        elif score >= 1 and left < right:
            power += tokens[right]
            score -= 1
            right -= 1
            
        else:
            break
        
    return maxScore
            

tokens = list(map(int, input("Enter tokens(separated by spaces): ").split()))
print(tokens)
power = int(input("Enter power: "))
print(f"Max Score: {bagOfTokens(tokens, power)}")

