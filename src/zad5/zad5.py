
import requests #pragma: no cover

class Meals():
    def getMealsByLetter(self, letter):
        if type(letter) != str or len(letter) != 1:
            raise ValueError("Argument powinien być pojedyncza litera!")
        req = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
        if not req.json()['meals']:
            raise ValueError("Nie znaleziono żadnych potraw.")
        result= []
        for i in req.json()['meals']:
            result.append(i['strMeal'])
        return result

    def getMealById(self, id):
        if type(id) != int or id < 0:
            raise ValueError("Argument powinien być dodatnią liczba całkowita!")
        req = requests.get(f"http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
        if not req.json()['meals']:
            raise ValueError("Nie znaleziono żadnej potrawy.")
        return req.json()['meals'][0]['strMeal']


    def getMealByName(self, name):
        if type(name) != str or len(name) == 0:
            raise ValueError("Argument powinien być napisem!")
        req = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={name}")
        if not req.json()['meals']:
            raise ValueError("Nie znaleziono żadnej potrawy.")
        return req.json()['meals'][0]['strMeal']


    def getAllCategories(self):
        req = requests.get(f"https://www.themealdb.com/api/json/v1/1/categories.php")
        result = []
        for i in req.json()['categories']:
            result.append(i['strCategory'])
        return result

    def getAllIngredients(self):
        req = requests.get(f"https://www.themealdb.com/api/json/v1/1/list.php?i=list")
        result = []
        for i in req.json()['meals']:
            result.append(i['strIngredient'])
        return result
