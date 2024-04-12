from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError

class CategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Category Test')
        return super().setUp()
    
    def test_category_max_length_fields_65_chars(self):
        self.category.name = 'A' * 170
        with self.assertRaises(ValidationError): 
            self.category.full_clean()


    def test_category_string_representation(self):
        needed = 'Test category Representation'
        self.category.name = 'Test category Representation'
        self.category.full_clean()
        self.category.save()

        self.assertEqual(str(self.category), needed)