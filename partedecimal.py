n_string=input("ingrese un numero: ")
decimal="0"
es_decimal=False
for i in range(len(n_string)):
	if n_string[i]==".":
		es_decimal=True
	if es_decimal:
		decimal+=n_string[i]
if not(es_decimal):
	print(0.0)
else:
	print(decimal)