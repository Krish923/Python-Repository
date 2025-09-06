book1_title = input()
book1_year = int(input())
book2_title = input()
book2_year = int(input())
book3_title = input()
book3_year = int(input())

library_collection = ((book1_title, book1_year), (book2_title, book2_year), (book3_title, book3_year))
publication_years = [book[1] for book in library_collection]
oldest_book = min(library_collection, key=lambda x: x[1])

print("Oldest book:", oldest_book[0])
print("Latest year:", max(publication_years))
print("Books before 2000:", len([year for year in publication_years if year < 2000]))
