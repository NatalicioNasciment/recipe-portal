from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Recipe
from .test_recipe_base import RecipeTestBase

class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_return_status_code_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200 )
    
    def test_recipe_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_no_recipe_found_if_no_recipes(self):
        Recipe.objects.filter(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn( 'No recipes found',response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(author_data={
            'first_name': 'fran'
        })

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        context_recipes = response.context['recipes']
        
        self.assertIn('Recipe Title', content)
        self.assertIn('Recipe Description', content)
        self.assertIn('10  Minutos', content)
        self.assertIn('fran', content)
        self.assertEqual(len(context_recipes), 1)

    def test_recipe_home_template_dont_loads_recipes_not_published(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn( 'No recipes found', content)

    def test_recipe_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_return_404_if_no_recipes_founds(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_category_template_loads_recipes(self):
        needed_title= 'This title is required'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')
        context_recipes = response.context['recipes']
        
        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_loads_recipes_not_published(self):

        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:category', kwargs={'category_id': recipe.category.id}))
        self.assertEqual(response.status_code, 404)


    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_return_404_if_no_recipes_founds(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_load_one_recipe(self):
        needed_title= 'This title is required'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        
        self.assertIn(needed_title, content)
    
    def test_recipe_detail_template_dont_load_one_recipe_not_published(self):

        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_uses_correct_view_fuction(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

