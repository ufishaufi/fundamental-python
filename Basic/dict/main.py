"""
Tipe data dictionary
"""

dictionary = {
    'kid': 'anak',
    'wife': 'istri',
    'father': 'ayah',
    'mother': 'ibu'
}

print(dictionary)
print(dictionary['father'])
print(dictionary['mother'])

data_from_server_gojek = {
    'tanggal': '2020-07-25',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 20},
        {'nama': 'Tri', 'jarak': 50},
        {'nama': 'Catur', 'jarak': 100},
        {'nama': 'Limo', 'jarak': 1000}
    ]
}

# print(data_from_server_gojek)
# print(f"Driver disekitar ini {data_from_server_gojek['driver_list']}")
print(f"Data driver #1 {data_from_server_gojek['driver_list'][0]}")
print(f"Driver terdekat berjarak {data_from_server_gojek['driver_list'][0]['jarak']} meter")

people = {'John' : 32, 'Rob' : 23}
print(people['John'])
print(people['Rob'])

# Dictionary function

numbers = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
}

print(1 in numbers)
print(numbers.get(2))
print(numbers.get(5, 'Key tidak ditemukan'))


# exercise
products = {
    'Chair' : 40,
    'Sofa' : 50,
    'Table' : 90,
    'Monitor' : 1,
    'Carpet' : 200
}

newproduct = input('Masukkan nama produk: ')
if(newproduct in products):
    print(f"jumlah produk {newproduct} yang tersedia ada: {products.get(newproduct)} unit")
else:
    print('Produk tidak ditemukan')