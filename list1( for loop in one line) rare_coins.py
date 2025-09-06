coin_values = []
coin_count = int(input())
for i in range(coin_count):
    value = int(input())
    coin_values.append(value)

rare_threshold = int(input())
rare_coins = [value for value in coin_values if value >= rare_threshold]
print("Rare coins:", len(rare_coins));

collection_value = sum(coin_values)
print("Collection value:", collection_value);

most_valuable = max(coin_values)
least_valuable = min(coin_values)
print("Most valuable:", most_valuable);
