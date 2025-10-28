# Your code here
# Read inputs
X = int(input())        # Weekly rental cost
D = int(input())        # Number of rental days
S = input().strip()     # Staff status ("true" or "false")

# Base cost is always X for up to 7 days
total_cost = X

# If rental is more than 7 days and not staff, add extra charges
if D > 7 and S == "false":
    extra_days = D - 7
    total_cost += extra_days * 2

# Staff members or rentals within 7 days pay only X

# Output the total cost
print(total_cost)
