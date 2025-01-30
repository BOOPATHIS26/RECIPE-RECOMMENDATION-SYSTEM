class RecipeRecommendationSystem:
    def __init__(self):
        self.recipes = {
            'Tomato Rice': {
                'ingredients': ['rice', 'tomato', 'onion', 'garlic', 'spices'],
                'instructions': '1. Fry onions and garlic.\n2. Add tomatoes and cook.\n3. Add spices and cook rice.\n4. Serve hot.'
            },
            'Sambar': {
                'ingredients': ['dal', 'tomato', 'onion', 'tamarind', 'spices'],
                'instructions': '1. Cook dal and set aside.\n2. Prepare tamarind water.\n3. Fry onions, tomatoes, and spices.\n4. Add cooked dal and tamarind water. Cook until boiling.'
            },
            'Dosa': {
                'ingredients': ['rice', 'urad dal', 'salt'],
                'instructions': '1. Soak rice and dal overnight.\n2. Grind into a batter.\n3. Heat a pan, pour batter, and cook until crispy.'
            },
            'Idli': {
                'ingredients': ['rice', 'urad dal', 'salt'],
                'instructions': '1. Soak rice and dal overnight.\n2. Grind into a smooth batter.\n3. Pour batter into molds and steam for 10-15 minutes.'
            },
            'Vada': {
                'ingredients': ['urad dal', 'onion', 'green chilies', 'spices'],
                'instructions': '1. Soak dal and grind into a thick batter.\n2. Add chopped onions, chilies, and spices.\n3. Shape the batter into doughnuts and deep fry.'
            },
            'Pongal': {
                'ingredients': ['rice', 'moong dal', 'pepper', 'ginger', 'cashews'],
                'instructions': '1. Cook rice and dal together.\n2. Temper with mustard seeds, pepper, ginger, and cashews.\n3. Serve hot.'
            },
            'Coconut Rice': {
                'ingredients': ['rice', 'coconut', 'mustard seeds', 'green chilies', 'spices'],
                'instructions': '1. Cook rice and set aside.\n2. Fry coconut with mustard seeds and green chilies.\n3. Mix coconut mixture with rice and serve.'
            },
            'Biryani': {
                'ingredients': ['rice', 'chicken', 'onion', 'tomato', 'spices'],
                'instructions': '1. Fry onions and tomatoes.\n2. Add chicken and cook with spices.\n3. Add rice and cook until done.'
            },
            'Chapati': {
                'ingredients': ['wheat flour', 'water', 'salt'],
                'instructions': '1. Knead dough with water and salt.\n2. Roll dough into thin circles.\n3. Cook on a hot griddle until both sides are golden.'
            },
            'Paratha': {
                'ingredients': ['wheat flour', 'potato', 'onion', 'spices'],
                'instructions': '1. Boil and mash potatoes.\n2. Mix with spices and onions.\n3. Roll into balls and cook as parathas.'
            },
            'Pulao': {
                'ingredients': ['rice', 'vegetables', 'spices'],
                'instructions': '1. Fry onions and spices.\n2. Add vegetables and cook.\n3. Add rice and water, cook until rice is done.'
            },
            'Aloo Gobi': {
                'ingredients': ['potato', 'cauliflower', 'onion', 'spices'],
                'instructions': '1. Fry onions and spices.\n2. Add potatoes and cauliflower.\n3. Cook until vegetables are tender.'
            },
            'Butter Chicken': {
                'ingredients': ['chicken', 'butter', 'tomato', 'cream', 'spices'],
                'instructions': '1. Fry chicken with spices.\n2. Add tomato and cook down into a sauce.\n3. Add cream and butter, simmer until thick.'
            },
            'Tikka Masala': {
                'ingredients': ['chicken', 'tomato', 'cream', 'spices'],
                'instructions': '1. Marinate chicken in yogurt and spices.\n2. Cook chicken and set aside.\n3. Make a sauce with tomatoes and cream, add chicken, and simmer.'
            },
            'Chole Bhature': {
                'ingredients': ['chickpeas', 'flour', 'yogurt', 'spices'],
                'instructions': '1. Cook chickpeas with spices.\n2. Prepare dough for bhature.\n3. Deep fry bhature and serve with chole.'
            },
            'Paneer Butter Masala': {
                'ingredients': ['paneer', 'tomato', 'butter', 'cream', 'spices'],
                'instructions': '1. Fry paneer cubes.\n2. Prepare a sauce with tomatoes, butter, and cream.\n3. Add paneer and cook until well mixed.'
            },
            'Baingan Bharta': {
                'ingredients': ['eggplant', 'onion', 'tomato', 'spices'],
                'instructions': '1. Roast eggplant until soft.\n2. Peel and mash.\n3. Fry onions and tomatoes, then add the eggplant and cook.'
            },
            'Methi Thepla': {
                'ingredients': ['fenugreek', 'wheat flour', 'spices'],
                'instructions': '1. Mix fenugreek leaves with wheat flour and spices.\n2. Roll out into circles and cook on a griddle.'
            },
            'Kadhi Pakora': {
                'ingredients': ['yogurt', 'gram flour', 'onion', 'spices'],
                'instructions': '1. Prepare gram flour fritters (pakoras).\n2. Make a kadhi using yogurt and spices.\n3. Add pakoras to the kadhi and cook until soft.'
            },
            'Rajma': {
                'ingredients': ['kidney beans', 'tomato', 'onion', 'spices'],
                'instructions': '1. Cook kidney beans with onions and spices.\n2. Add tomatoes and cook until soft.\n3. Serve with rice.'
            },
            'Kofta Curry': {
                'ingredients': ['paneer', 'potato', 'onion', 'spices'],
                'instructions': '1. Make koftas using paneer and potatoes.\n2. Prepare curry with onions and spices.\n3. Add koftas to the curry and simmer.'
            },
            'Pav Bhaji': {
                'ingredients': ['potato', 'tomato', 'onion', 'spices'],
                'instructions': '1. Mash potatoes and vegetables.\n2. Cook with onions and spices.\n3. Serve with pav (bread) toasted with butter.'
            },
            'Dhokla': {
                'ingredients': ['gram flour', 'yogurt', 'mustard seeds', 'spices'],
                'instructions': '1. Mix gram flour with yogurt and spices to form a batter.\n2. Steam the batter to cook the dhokla.'
            },
            'Khandvi': {
                'ingredients': ['gram flour', 'yogurt', 'mustard seeds', 'spices'],
                'instructions': '1. Prepare a smooth batter from gram flour and cook into thin layers.\n2. Roll up the cooked batter and season with mustard seeds.'
            },
            'Methi Malai Murg': {
                'ingredients': ['chicken', 'fenugreek', 'cream', 'spices'],
                'instructions': '1. Cook chicken with fenugreek and spices.\n2. Add cream and simmer.'
            },
            'Chana Masala': {
                'ingredients': ['chickpeas', 'onion', 'tomato', 'spices'],
                'instructions': '1. Cook chickpeas with onions and tomatoes.\n2. Add spices and cook until thick.'
            },
            'Tandoori Chicken': {
                'ingredients': ['chicken', 'yogurt', 'spices'],
                'instructions': '1. Marinate chicken in yogurt and spices.\n2. Cook in a tandoor or oven until crispy.'
            },
            'Aloo Tikki': {
                'ingredients': ['potato', 'onion', 'spices'],
                'instructions': '1. Mash potatoes and mix with spices.\n2. Shape into patties and shallow fry.'
            },
            'Mango Lassi': {
                'ingredients': ['mango', 'yogurt', 'milk', 'sugar'],
                'instructions': '1. Blend mango with yogurt, milk, and sugar until smooth.'
            },
            'Gulab Jamun': {
                'ingredients': ['milk powder', 'flour', 'sugar', 'ghee'],
                'instructions': '1. Make a dough from milk powder and flour.\n2. Shape into balls and deep fry.\n3. Soak in sugar syrup.'
            },
            'Jalebi': {
                'ingredients': ['flour', 'sugar', 'saffron', 'ghee'],
                'instructions': '1. Make a batter from flour and water.\n2. Shape into spirals and deep fry.\n3. Soak in sugar syrup.'
            },
            'Rava Kesari': {
                'ingredients': ['semolina', 'sugar', 'ghee', 'cardamom'],
                'instructions': '1. Roast semolina in ghee.\n2. Add sugar and water, cook until thick.\n3. Garnish with cardamom.'
            },
            'Payasam': {
                'ingredients': ['rice', 'milk', 'sugar', 'cardamom'],
                'instructions': '1. Cook rice in milk.\n2. Add sugar and cardamom, cook until creamy.'
            },
            'Lassi': {
                'ingredients': ['yogurt', 'water', 'sugar'],
                'instructions': '1. Blend yogurt with water and sugar until smooth.'
            },
            'Bhel Puri': {
                'ingredients': ['puffed rice', 'onion', 'tomato', 'tamarind chutney'],
                'instructions': '1. Mix puffed rice with vegetables and chutney.\n2. Serve immediately.'
            },
            'Pani Puri': {
                'ingredients': ['puri', 'chickpeas', 'tamarind chutney', 'spices'],
                'instructions': '1. Fill puris with chickpeas, chutney, and spices.\n2. Serve with tamarind water.'
            },
            'Sev Puri': {
                'ingredients': ['puri', 'potato', 'onion', 'sev', 'chutney'],
                'instructions': '1. Fill puris with potatoes, onions, and chutney.\n2. Garnish with sev.'
            },
            'Kachori': {
                'ingredients': ['flour', 'spices', 'dal'],
                'instructions': '1. Prepare dough and fill with spiced dal.\n2. Deep fry kachoris.'
            },
            'Misal Pav': {
                'ingredients': ['sprouted beans', 'onion', 'tomato', 'spices'],
                'instructions': '1. Cook sprouted beans with onions and spices.\n2. Serve with pav.'
            },
            'Samosa': {
                'ingredients': ['flour', 'potato', 'spices'],
                'instructions': '1. Make a filling of mashed potatoes and spices.\n2. Shape into triangles and deep fry.'
            },
            'Khichdi': {
                'ingredients': ['rice', 'dal', 'ghee', 'spices'],
                'instructions': '1. Cook rice and dal together with ghee and spices.\n2. Serve hot.'
            },
            'Dal Tadka': {
                'ingredients': ['dal', 'onion', 'tomato', 'garlic', 'spices'],
                'instructions': '1. Cook dal until soft.\n2. Prepare tadka with garlic, onion, tomatoes, and spices.\n3. Pour tadka over dal.'
            },
            'Pav Bhaji': {
                'ingredients': ['vegetables', 'bread', 'butter', 'spices'],
                'instructions': '1. Cook vegetables and mash.\n2. Serve with buttered bread.'
            }
        }

    def recommend_recipe(self, user_ingredients):
        recommended_dishes = []
        for dish, details in self.recipes.items():
            if all(ingredient in user_ingredients for ingredient in details['ingredients']):
                recommended_dishes.append(dish)
        return recommended_dishes

    def get_cooking_instructions(self, dish_name):
        if dish_name in self.recipes:
            return self.recipes[dish_name]['instructions']
        return "Recipe not found."

def main():
    system = RecipeRecommendationSystem()
    
    user_ingredients = input("Enter the ingredients you have (comma separated): ").lower().split(', ')
    recommended_dishes = system.recommend_recipe(user_ingredients)
    
    if recommended_dishes:
        print("\nWe recommend the following dishes based on your ingredients:")
        for dish in recommended_dishes:
            print(f"- {dish}")
        
        dish_choice = input("\nEnter the dish name for cooking instructions: ").title()
        instructions = system.get_cooking_instructions(dish_choice)
        print(f"\nCooking Instructions for {dish_choice}:\n{instructions}")
    else:
        print("Sorry, no recommendations available with the given ingredients.")

if __name__ == "__main__":
    main()
