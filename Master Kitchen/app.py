from flask import Flask, render_template, request, abort

app = Flask(__name__)

# -----------------------------------------
# Recipe Database
# -----------------------------------------

recipes = [

    {
        "id": 1,
        "name": "Chicken Biryani",
        "description": "Aromatic Indian chicken biryani made with basmati rice and flavorful spices.",
        "prep_time": "20 minutes",
        "cook_time": "40 minutes",
        "servings": "4",
        "image": "https://images.unsplash.com/photo-1563379091339-03246963d96c",
        "ingredients": [
            "500 g chicken",
            "2 cups basmati rice",
            "2 onions, sliced",
            "2 tomatoes, chopped",
            "1/2 cup yogurt",
            "2 tablespoons biryani masala",
            "1 tablespoon ginger-garlic paste",
            "3 tablespoons cooking oil",
            "Salt to taste",
            "Fresh coriander leaves",
            "Fresh mint leaves"
        ],
        "instructions": [
            "Wash and soak the basmati rice for 20 minutes.",
            "Marinate the chicken with yogurt, biryani masala, ginger-garlic paste and salt.",
            "Heat oil in a large pot and fry the onions until golden brown.",
            "Add tomatoes and cook until soft.",
            "Add the marinated chicken and cook for 15 minutes.",
            "Add partially cooked rice over the chicken.",
            "Cover the pot and cook on low heat for 20 minutes.",
            "Garnish with coriander and mint leaves and serve hot."
        ]
    },

    {
        "id": 2,
        "name": "Masala Dosa",
        "description": "Crispy South Indian dosa served with delicious spicy potato masala.",
        "prep_time": "15 minutes",
        "cook_time": "20 minutes",
        "servings": "3",
        "image": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976",
        "ingredients": [
            "2 cups dosa batter",
            "3 potatoes",
            "1 onion, sliced",
            "1 green chilli",
            "1/2 teaspoon mustard seeds",
            "1/2 teaspoon turmeric",
            "1 tablespoon oil",
            "Curry leaves",
            "Salt to taste"
        ],
        "instructions": [
            "Boil the potatoes and mash them.",
            "Heat oil and add mustard seeds and curry leaves.",
            "Add onions and green chilli and cook until soft.",
            "Add turmeric, salt and mashed potatoes.",
            "Mix everything and cook for 3 minutes.",
            "Heat a dosa pan and spread the dosa batter into a thin circle.",
            "Cook until crispy and place the potato masala inside.",
            "Fold and serve with chutney or sambar."
        ]
    },

    {
        "id": 3,
        "name": "Veg Fried Rice",
        "description": "Quick and tasty vegetable fried rice prepared with rice and fresh vegetables.",
        "prep_time": "10 minutes",
        "cook_time": "15 minutes",
        "servings": "3",
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b",
        "ingredients": [
            "3 cups cooked rice",
            "1 carrot, chopped",
            "1/2 cup green peas",
            "1/2 capsicum, chopped",
            "2 spring onions",
            "2 tablespoons soy sauce",
            "1 tablespoon cooking oil",
            "1/2 teaspoon black pepper",
            "Salt to taste"
        ],
        "instructions": [
            "Heat oil in a wok or large pan.",
            "Add carrots, peas and capsicum.",
            "Stir-fry the vegetables for 3 to 4 minutes.",
            "Add cooked rice.",
            "Add soy sauce, pepper and salt.",
            "Mix everything well on high heat.",
            "Add spring onions.",
            "Serve hot."
        ]
    },

    {
        "id": 4,
        "name": "Paneer Butter Masala",
        "description": "Creamy Indian paneer curry cooked in a rich tomato and butter gravy.",
        "prep_time": "15 minutes",
        "cook_time": "25 minutes",
        "servings": "4",
        "image": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7",
        "ingredients": [
            "250 g paneer",
            "3 tomatoes",
            "1 onion",
            "2 tablespoons butter",
            "1/2 cup cream",
            "1 teaspoon ginger-garlic paste",
            "1 teaspoon garam masala",
            "1/2 teaspoon chilli powder",
            "Salt to taste"
        ],
        "instructions": [
            "Heat butter in a pan.",
            "Add onions and cook until soft.",
            "Add ginger-garlic paste and cook for one minute.",
            "Add chopped tomatoes and cook until soft.",
            "Blend the cooked mixture into a smooth paste.",
            "Return the mixture to the pan.",
            "Add spices, salt and cream.",
            "Add paneer cubes and simmer for 5 minutes.",
            "Serve hot with naan or rice."
        ]
    },

    {
        "id": 5,
        "name": "Pasta Alfredo",
        "description": "Creamy Italian-style pasta prepared with cheese, butter and fresh cream.",
        "prep_time": "10 minutes",
        "cook_time": "20 minutes",
        "servings": "2",
        "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601",
        "ingredients": [
            "200 g pasta",
            "2 tablespoons butter",
            "1 cup fresh cream",
            "1/2 cup grated Parmesan cheese",
            "2 cloves garlic",
            "1/2 teaspoon black pepper",
            "Salt to taste"
        ],
        "instructions": [
            "Boil pasta according to the package instructions.",
            "Melt butter in a pan.",
            "Add chopped garlic and cook for one minute.",
            "Add fresh cream and simmer gently.",
            "Add Parmesan cheese.",
            "Add salt and black pepper.",
            "Add cooked pasta and mix well.",
            "Serve immediately."
        ]
    }

]


# -----------------------------------------
# Home Page + Search
# -----------------------------------------

@app.route("/")
def home():

    query = request.args.get("q", "").strip()

    if query:

        search_text = query.lower()

        filtered_recipes = [
            recipe
            for recipe in recipes
            if search_text in recipe["name"].lower()
            or search_text in recipe["description"].lower()
            or any(
                search_text in ingredient.lower()
                for ingredient in recipe["ingredients"]
            )
        ]

    else:
        filtered_recipes = recipes

    return render_template(
        "index.html",
        recipes=filtered_recipes,
        query=query
    )


# -----------------------------------------
# Recipe Details
# -----------------------------------------

@app.route("/recipe/<int:recipe_id>")
def recipe_detail(recipe_id):

    recipe = next(
        (recipe for recipe in recipes if recipe["id"] == recipe_id),
        None
    )

    if recipe is None:
        abort(404)

    return render_template(
        "recipe.html",
        recipe=recipe
    )


# -----------------------------------------
# Run Flask Server
# -----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)