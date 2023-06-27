# 4) Imagine uma playlist de músicas. Faça uma pesquisa binária para encontrar a posição de 
# uma música específica.


playlist = [
    "Black - Pearl Jam", 
    "Carry on - Angra", 
    "Carry on Wayward Son - Kansas", 
    "Come Together - The Beatles",
    "Do You Wanna Dance? - Ramones", 
    "Everlong - Foo Fighters", 
    "Falling Away from Me - Korn",
    "Heart-Shaped Box - Nirvana",
    "Hit the Road Jack - Ray Charles", 
    "Iron Maiden - Iron Maiden", 
    "Jonny B. Goode - Chuck Berry",
    "King of Pain - The Police", 
    "Misery Business - Paramore", 
    "Oceans - Hillsong UNITED",
    "Pretty Fly - The Offspring", 
    "Redemption Song - Bob Marley", 
    "Silent Lucidity - Queensryche",
    "Show Me How to Live - Audioslave", 
    "Somewhere Over the Rainbow - Israel 'IZ' Kamakawiwo'ole",
    "Spit It Out - Slipknot", 
    "Zombie - The Cranberries"
]

def binary_search_modified(playlist, keyword):
    low = 0
    high = len(playlist) - 1
    matching_songs = []
    search_count = 0

    while low <= high:
        mid = (low + high) // 2
        current_song = playlist[mid]
        search_count += 1

        if keyword.lower() in current_song.lower():
            matching_songs.append((current_song, mid))

        left = mid - 1
        right = mid + 1

        while left >= low and keyword.lower() in playlist[left].lower():
            matching_songs.append((playlist[left], left))
            left -= 1

        while right <= high and keyword.lower() in playlist[right].lower():
            matching_songs.append((playlist[right], right))
            right += 1

        if current_song.lower() < keyword.lower():
            low = right
        else:
            high = left

    return matching_songs, search_count

keyword = input("Digite uma palavra-chave para pesquisar músicas: ").lower()
matching_songs, search_count = binary_search_modified(playlist, keyword)

if matching_songs:
    print("Músicas correspondentes encontradas:")
    for song, position in matching_songs:
        print(f"{position + 1} - {song}")
    print("Número de pesquisas binárias realizadas:", search_count)
else:
    print("Nenhuma música correspondente encontrada.")