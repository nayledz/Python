from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant

decoration = DecorationRepository()
decoration1 = Ornament()
decoration2 = Plant()
decoration.add(decoration1)
decoration.add(decoration2)
print(decoration.find_by_type(Plant))



