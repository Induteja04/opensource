b=int(input())
discount_percent=b*0.10
discount_flat=100
max_discount=max(discount_percent,discount_flat)
amount=b-max_discount
print(int(amount))
