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

