# template
class Estudent:
	# attribute
	name = '"name"'
	id = '"000"'

# object / instance
beatriz = Estudent()
beatriz.name = "beatriz"
beatriz.id = 193

rivaldo = Estudent()
rivaldo.name = "rivaldo"
rivaldo.id = 203

# access
print(beatriz.name)
print(rivaldo.id)

print(beatriz.__dict__)
print(rivaldo.__dict__)