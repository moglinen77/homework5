immutable_var = ('лещ', 'карась', 'щука', 'рак', 1, True)
print(immutable_var)
#immutable_var[4] = 'вобла' # кортежсодержит неизменяемые данные, это связанно схранением данных в памяти программы
mutable_var = ['лещ', 'карась', 'щука', 'рак', 1, True]
print(mutable_var)
mutable_var[2] = 'вобла'
print(mutable_var)