from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipe_no_default_fields(self):
        recipe = Recipe(
            category=self.make_category(name='newcategory'),
            author=self.make_author(username='newusername'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug-xyz',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
        )
        recipe.full_clean()
        recipe.save()

        return recipe
    @parameterized.expand(
            [
                ('title', 65),
                ('description', 165),
                ('preparation_time_unit', 65),
                ('servings_unit', 65),    
            ]
    )
    def test_recipe_fields_max_lenght(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length+1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_step_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_default_fields()

        self.assertFalse(recipe.preparation_step_is_html)

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_default_fields()

        self.assertFalse(recipe.is_published)

    def test_recipe_string_representation(self):
        needed = 'Test Title Representation'
        self.recipe.title = 'Test Title Representation'
        self.recipe.full_clean()
        self.recipe.save()

        self.assertEqual(str(self.recipe), needed)